#!/usr/bin/env python3
import copy,hashlib,json,sys
from pathlib import Path
from jsonschema import Draft202012Validator,FormatChecker
ROOT=Path(__file__).resolve().parents[2]
S=json.loads((ROOT/"schemas/encyclopedia/encyclopedia-evidence-contracts.v1.schema.json").read_text())
F=json.loads((ROOT/"examples/encyclopedias/encyclopedia-evidence-contracts.v1.json").read_text())
K={"source_record":"sourceRecord","ingestion_manifest":"ingestionManifest","citation_proof":"citationProof","coverage_report":"coverageReport","editorial_status":"editorialStatus","knowledge_asset":"knowledgeAsset","okf_export":"okfExport","evidence_bundle":"evidenceBundle","correction_event":"correctionEvent","answer_receipt":"answerReceipt"}
def valid(k,x): Draft202012Validator({"$schema":S["$schema"],"$defs":S["$defs"],"$ref":"#/$defs/"+K[k]},format_checker=FormatChecker()).validate(x)
def h(x): return hashlib.sha256(x).digest()
def canon(x): return json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(",",":"),allow_nan=False).encode()
def verify(p):
 raw=canon(p["payload"])
 if hashlib.sha256(raw).hexdigest()!=p["payload_digest"]: return False
 r=h(bytes([0])+raw)
 if r.hex()!=p["leaf_hash"]: return False
 fn=p["leaf_index"]; sn=p["tree_size"]-1
 if fn>=p["tree_size"]: return False
 for item in p["path"]:
  if sn==0: return False
  q=bytes.fromhex(item)
  if (fn&1)==1 or fn==sn:
   r=h(bytes([1])+q+r)
   if (fn&1)==0:
    while fn!=0 and (fn&1)==0: fn>>=1; sn>>=1
  else: r=h(bytes([1])+r+q)
  fn>>=1; sn>>=1
 return sn==0 and r.hex()==p["root_hash"]
def semantic(d):
 m=d["ingestion_manifest"]
 assert len({x["source_id"] for x in m["documents"]})==len(m["documents"])
 for doc in m["documents"]:
  for c in doc["chunks"]: assert c["end"]>c["start"] and c["end"]<=doc["byte_length"]
 assert verify(d["citation_proof"]["proof"]),"RFC 9162 inclusion proof failed"
 q=d["coverage_report"]
 assert q["verified"]+q["uncited"]+q["unverified"]+q["broken"]==q["total"]
 rate=q["verified"]/q["total"] if q["total"] else 1.0
 assert abs(rate-q["coverage"])<1e-9
 if q["result"]=="pass": assert rate>=q["threshold"] and q["broken"]==0
def main():
 for k,v in F.items(): valid(k,v)
 semantic(F)
 bad=[]
 x=copy.deepcopy(F); x["citation_proof"]["proof"]["root_hash"]="0"*64; bad.append(x)
 x=copy.deepcopy(F); x["citation_proof"]["proof"]["leaf_index"]=3; bad.append(x)
 x=copy.deepcopy(F); x["coverage_report"]["coverage"]=1; bad.append(x)
 x=copy.deepcopy(F); x["ingestion_manifest"]["documents"][1]["chunks"][0]["end"]=999999; bad.append(x)
 x=copy.deepcopy(F); x["citation_proof"]["truth_status"]="proven-true"; bad.append(x)
 x=copy.deepcopy(F); x["okf_export"]["entries"][0]["rights_status"]="unknown"; bad.append(x)
 for x in bad:
  try:
   for k,v in x.items(): valid(k,v)
   semantic(x)
  except Exception: continue
  raise AssertionError("negative fixture unexpectedly passed")
 print("PASS: 10 positive contract records, RFC 9162 Merkle proof, and 6 negative cases")
 print("LIMIT: no production ingest, editorial connector, signature service or corpus deployed")
if __name__=="__main__":
 try: main()
 except Exception as e: print("FAIL:",e,file=sys.stderr); raise SystemExit(1)
