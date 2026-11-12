#!/usr/bin/env python3
"""Validate encyclopedia evidence contracts and RFC 9162 Merkle inclusion proofs."""
from __future__ import annotations
import copy, hashlib, json, sys
from pathlib import Path
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[2]
SCHEMA = json.loads((ROOT / "schemas/encyclopedia/encyclopedia-evidence-contracts.v1.schema.json").read_text())
FIXTURES = json.loads((ROOT / "examples/encyclopedias/encyclopedia-evidence-contracts.v1.json").read_text())
KEYS = {
    "source_record": "sourceRecord",
    "ingestion_manifest": "ingestionManifest",
    "citation_proof": "citationProof",
    "coverage_report": "coverageReport",
    "editorial_status": "editorialStatus",
    "citation_integrity_sweep": "citationIntegritySweep",
    "knowledge_asset": "knowledgeAsset",
    "okf_export": "okfExport",
    "evidence_bundle": "evidenceBundle",
    "correction_event": "correctionEvent",
    "answer_receipt": "answerReceipt",
}

def validate_record(key: str, value: dict) -> None:
    view = {"$schema": SCHEMA["$schema"], "$defs": SCHEMA["$defs"], "$ref": "#/$defs/" + KEYS[key]}
    Draft202012Validator(view, format_checker=FormatChecker()).validate(value)

def sha256(data: bytes) -> bytes:
    return hashlib.sha256(data).digest()

def check_jcs_subset(value) -> None:
    """Restrict the proof payload to the RFC 8785-compatible subset this stdlib encoder can reproduce."""
    if value is None or isinstance(value, (str, bool)):
        return
    if isinstance(value, int) and not isinstance(value, bool):
        if abs(value) > 9007199254740991:
            raise ValueError("JCS integer exceeds interoperable IEEE-754 safe range")
        return
    if isinstance(value, float):
        raise ValueError("JCS proof payload profile excludes floating-point numbers")
    if isinstance(value, list):
        for item in value:
            check_jcs_subset(item)
        return
    if isinstance(value, dict):
        for key, item in value.items():
            if not isinstance(key, str) or not key.isascii():
                raise ValueError("JCS proof payload profile requires ASCII object keys")
            check_jcs_subset(item)
        return
    raise ValueError("unsupported JCS proof payload value")

def canonical_payload(value: dict) -> bytes:
    check_jcs_subset(value)
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False).encode("utf-8")

def verify_rfc9162(proof: dict) -> bool:
    raw = canonical_payload(proof["payload"])
    if hashlib.sha256(raw).hexdigest() != proof["payload_digest"]:
        return False
    node = sha256(bytes([0]) + raw)
    if node.hex() != proof["leaf_hash"]:
        return False
    fn = proof["leaf_index"]
    sn = proof["tree_size"] - 1
    if fn >= proof["tree_size"]:
        return False
    path = proof["path"]
    for sibling_hex in path:
        if sn == 0:
            return False
        sibling = bytes.fromhex(sibling_hex)
        if (fn & 1) == 1 or fn == sn:
            node = sha256(bytes([1]) + sibling + node)
            if (fn & 1) == 0:
                while fn != 0 and (fn & 1) == 0:
                    fn >>= 1
                    sn >>= 1
        else:
            node = sha256(bytes([1]) + node + sibling)
        fn >>= 1
        sn >>= 1
    return sn == 0 and node.hex() == proof["root_hash"]

def semantic_checks(data: dict) -> None:
    manifest = data["ingestion_manifest"]
    source_ids = [item["source_id"] for item in manifest["documents"]]
    assert len(source_ids) == len(set(source_ids)), "duplicate source IDs"
    for document in manifest["documents"]:
        chunk_ids = [chunk["id"] for chunk in document["chunks"]]
        assert len(chunk_ids) == len(set(chunk_ids)), "duplicate chunk IDs"
        sequences = [chunk["sequence"] for chunk in document["chunks"]]
        assert sequences == sorted(sequences), "chunk sequence is not ordered"
        for chunk in document["chunks"]:
            assert chunk["end"] > chunk["start"], "empty or reversed chunk range"
            assert chunk["end"] <= document["byte_length"], "chunk extends beyond source byte length"

    assert verify_rfc9162(data["citation_proof"]["proof"]), "RFC 9162 Merkle inclusion proof failed"
    assert data["citation_proof"]["truth_status"] == "not-established-by-inclusion-proof"

    report = data["coverage_report"]
    total = report["total"]
    categorized = report["verified"] + report["uncited"] + report["unverified"] + report["broken"]
    assert categorized == total, "citation coverage categories do not partition total claims"
    calculated = report["verified"] / total if total else 1.0
    assert abs(calculated - report["coverage"]) < 1e-9, "citation coverage rate does not match counts"
    if report["result"] == "pass":
        assert calculated >= report["threshold"] and report["broken"] == 0, "coverage pass contradicts threshold or broken citations"

    sweep = data["citation_integrity_sweep"]
    assert sweep["references_checked"] >= len(sweep["records"]), "sweep record count exceeds checked references"
    if sweep["unresolved"] or sweep["disagreements"]:
        assert sweep["result"] in {"review-required", "incomplete"}, "unresolved sweep cannot be clean"
    for record in sweep["records"]:
        adverse = {"retraction", "withdrawn", "expression-of-concern", "removal", "correction"}
        if record["update_type"] in adverse:
            assert record["resolution"] in {"flag-for-review", "status-found", "source-disagreement"}, "adverse editorial status cannot be hidden as no-flag"

    for entry in data["okf_export"]["entries"]:
        assert entry["rights_status"] in {"verified", "public-domain-verified"}, "public export requires rights-cleared entry"
    assert data["knowledge_asset"]["rights_status"] in {"verified", "public-domain-verified"}, "fixture asset is not rights-cleared"

def main() -> None:
    for key, record in FIXTURES.items():
        validate_record(key, record)
    semantic_checks(FIXTURES)

    negatives = []
    item = copy.deepcopy(FIXTURES); item["citation_proof"]["proof"]["root_hash"] = "0" * 64; negatives.append(("tampered Merkle root", item))
    item = copy.deepcopy(FIXTURES); item["citation_proof"]["proof"]["leaf_index"] = 3; negatives.append(("out-of-range Merkle leaf index", item))
    item = copy.deepcopy(FIXTURES); item["coverage_report"]["coverage"] = 1; negatives.append(("incorrect citation coverage rate", item))
    item = copy.deepcopy(FIXTURES); item["ingestion_manifest"]["documents"][1]["chunks"][0]["end"] = 999999; negatives.append(("chunk beyond source byte length", item))
    item = copy.deepcopy(FIXTURES); item["citation_proof"]["truth_status"] = "proven-true"; negatives.append(("Merkle proof cannot assert claim truth", item))
    item = copy.deepcopy(FIXTURES); item["okf_export"]["entries"][0]["rights_status"] = "unknown"; negatives.append(("rights-uncleared entry cannot be exported", item))
    item = copy.deepcopy(FIXTURES); item["citation_integrity_sweep"]["records"][0]["update_type"] = "retraction"; item["citation_integrity_sweep"]["records"][0]["resolution"] = "no-flag-found"; negatives.append(("retraction cannot be silently cleared", item))
    item = copy.deepcopy(FIXTURES); item["citation_proof"]["proof"]["payload"]["citation_id"] = "forged"; negatives.append(("altered Merkle leaf payload", item))

    for label, candidate in negatives:
        try:
            for key, record in candidate.items():
                validate_record(key, record)
            semantic_checks(candidate)
        except Exception:
            continue
        raise AssertionError("negative fixture unexpectedly passed: " + label)

    print(f"PASS: {len(KEYS)} positive records, RFC 9162 SHA-256 proof verification, and {len(negatives)} negative cases")
    print("LIMIT: no production ingestion engine, editorial connector, signature service, private corpus or correction pipeline deployed")

if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print("FAIL:", exc, file=sys.stderr)
        raise SystemExit(1)
