# Engineering Toolchain and Initial Build Plan

**Repository:** `C2O-Chaos-to-Order/The-UNIVERSALIS-Encyclopedias`  
**Responsibility:** UNIVERSALIS Encyclopedias  
**Status:** Initial executable foundation in this branch; specialized candidates remain proposed pending verification.  
**Boundary:** Open UNIVERSALIS. Do not include C2O-private credentials, policies, authority state, or private operational data.

## Universal engineering foundation

- Least-privilege GitHub Actions CI, automated tests, and JSON contract/config validation.
- CodeQL/static analysis, secret scanning, dependency review, Dependabot, actionlint, and SBOM generation after settings and alert ownership are confirmed.
- CycloneDX/SPDX, OSV-Scanner, Trivy/Grype, Gitleaks, SLSA provenance, in-toto attestations, cosign signing, immutable releases, and reproducible-build comparison as staged controls.
- Pin toolchain versions and action references; retain specifications, fixtures, execution logs, provenance, and explicit limitations.

**Foundation candidates:** Secure SDLC Evidence Collector; repo-assurance; Chainguard Actions; cnspec SBOM Cataloger; CodeQL; actionlint; OSV-Scanner; Trivy/Grype; Gitleaks; SLSA/in-toto; cosign. Not yet verified as installed.

## Domain-specific candidate tools

olo-commons for open, license-aware facts with provenance and time; Flexible GraphRAG for document processing and hybrid graph retrieval; myKG for mixed-format confidence-scored graph induction; llmwiki for citation-traced Markdown wiki pages. stoa is a private-context candidate only and must not be used to expose C2O-private context. Require source licenses, claim-level citations, correction propagation, and provenance.

Verify source, license, maintainer, release activity, security, compatibility, data flow, source licensing, and evidence semantics before adoption. Extracted claims and confidence scores require independent validation.

## Initial executable implementation

- `.github/workflows/repository-quality.yml` runs on pushes and pull requests with read-only repository permissions.
- `.github/scripts/repository_quality_baseline.py` provides a dependency-free self-test and validates JSON in schema/manifest/contract/capability/skill directories plus `package.json` and `tsconfig.json`.
- This does not yet perform document ingestion, source verification, citation checking, graph reasoning, privacy review, or correction propagation.

## Next increments

1. Inventory current content formats, source metadata, licenses, schemas, and citation conventions.
2. Add claim/source/evidence/provenance record schemas and valid/invalid fixtures.
3. Add ingestion and citation-integrity tests before enabling autonomous updates.
4. Evaluate domain candidates and data-locality requirements before integration.
5. Preserve original source fragments, version hashes, correction events, and unresolved claims.

## Evidence status

| Item | Status |
|---|---|
| Tool candidates recorded | Documented |
| Baseline validator and CI authored | Implemented in this branch |
| GitHub Actions execution | Pending |
| Domain candidate verification | Pending |
| Specialized integration | Not yet implemented |
