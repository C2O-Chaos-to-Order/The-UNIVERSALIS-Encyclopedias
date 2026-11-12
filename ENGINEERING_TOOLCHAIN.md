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

## Cross-repository architecture register — 2026-11-12

The following are the canonical working records for the latest owner-supplied toolchain proposals. This repository records the references and boundary rules; implementation belongs in the domain-owning repositories.

### Human Knowledge
- [C2O Human Knowledge architecture](https://github.com/C2O-Chaos-to-Order/The-C2O-Human-Knowledge/blob/implementation/repository-foundation-2026-11-12/HUMAN_KNOWLEDGE_ARCHITECTURE.md), [shared MCP interface contracts](https://github.com/C2O-Chaos-to-Order/The-C2O-Human-Knowledge/blob/implementation/repository-foundation-2026-11-12/MCP_INTERFACE_CONTRACTS.md), and [validation evidence](https://github.com/C2O-Chaos-to-Order/The-C2O-Human-Knowledge/blob/implementation/repository-foundation-2026-11-12/HUMAN_KNOWLEDGE_VALIDATION.md).
- [UNIVERSALIS Human Knowledge architecture](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Human-Knowledge/blob/implementation/repository-foundation-2026-11-12/HUMAN_KNOWLEDGE_ARCHITECTURE.md), [shared MCP interface contracts](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Human-Knowledge/blob/implementation/repository-foundation-2026-11-12/MCP_INTERFACE_CONTRACTS.md), and [validation evidence](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Human-Knowledge/blob/implementation/repository-foundation-2026-11-12/HUMAN_KNOWLEDGE_VALIDATION.md).

### OS provisioning and virtualization
- [C2O private provisioning architecture](https://github.com/C2O-Chaos-to-Order/The-C2O-Ecosystem/blob/implementation/repository-foundation-2026-11-12/OS_PROVISIONING_ARCHITECTURE.md).
- [UNIVERSALIS open provisioning architecture](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Ecosystem/blob/implementation/repository-foundation-2026-11-12/OS_PROVISIONING_ARCHITECTURE.md).

### UNIVERSALIN Grid, Guardian, and Golden Compass
- [C2O boundary and verifier architecture](https://github.com/C2O-Chaos-to-Order/The-C2O-Ecosystem/blob/implementation/repository-foundation-2026-11-12/UNIVERSALIN_GUARDIAN_GOLDEN_COMPASS.md).
- [UNIVERSALIS Grid / Guardian / Compass architecture](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Ecosystem/blob/implementation/repository-foundation-2026-11-12/UNIVERSALIN_GUARDIAN_GOLDEN_COMPASS.md).

### Boundary and evidence status
C2O-private credentials, policies, identity state, authority tokens, private source text, and operational evidence remain inside authorized C2O environments. UNIVERSALIS remains public, local-first, inspectable, and independently operable. Only versioned, explicitly approved interface schemas and evidence packages may cross the boundary; an interface does not grant authority.

All named external tools remain owner-supplied candidates or reference patterns pending canonical-source, license, maintainer, release, security, compatibility, and claim verification. No candidate is represented as installed or adopted merely because it appears in these records.

## Powers energy architecture register — 2026-11-12

Powers treat energy efficiency as a measurable, enforceable, auditable capacity—not only a permission or evaluation. In the current UNIVERSALIS repository set, the canonical implementation is maintained in the Intelligence Powers repository.

- **Canonical open architecture:** [UNIVERSALIS Powers energy architecture](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Intelligence-Powers/blob/implementation/repository-foundation-2026-11-12/POWERS_ENERGY_ARCHITECTURE.md).
- **Shared v1 contract:** [Powers energy schema](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Intelligence-Powers/blob/implementation/repository-foundation-2026-11-12/schemas/powers/powers-energy-contracts.v1.schema.json).
- **Executed checks and limitations:** [Powers validation record](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Intelligence-Powers/blob/implementation/repository-foundation-2026-11-12/POWERS_ENERGY_VALIDATION.md).

The open implementation is local-first and independently operable. Measurement, forecasting, receipts, and synergy calculation do not require a central database or truth authority. It keeps actual workload telemetry and local policy in the operator's chosen environment. The shared contract excludes private credentials and policy values. PDU/RAPL/Kepler/GPU layers require overlap reconciliation; synergy comparisons require matched workload cohorts and SLO profiles. External tools and their advertised savings remain candidates until independently verified.

## Four-document source coverage — 2026-11-12

The complete owner-supplied tool inventory and status matrix for Human Knowledge, Powers, Human Capabilities, and Mapping/Matrix/Organization/Ecosystem Mapping is maintained in the UNIVERSALIS research register: https://github.com/C2O-Chaos-to-Order/Research-for-the-UNIVERSALIS-Ecosystem/blob/implementation/repository-foundation-2026-11-12/FOUR_DOCUMENT_TOOLCHAIN_COVERAGE.md.

Treat every third-party name in that register as a proposed candidate/reference pattern until canonical source, license, maintenance, security, compatibility, and behavior are reviewed. The register distinguishes documented tools, basic contracts, passing CI, and actual integrations. This repository owns only the parts assigned to its domain. No C2O-private repository links or policy values are part of this public register.

## Master toolchain coverage register — 2026-11-12

The current public inventory for the original four toolchain documents plus the Intelligence Capabilities source is maintained in the UNIVERSALIS research register: https://github.com/C2O-Chaos-to-Order/Research-for-the-UNIVERSALIS-Ecosystem/blob/implementation/repository-foundation-2026-11-12/TOOLCHAIN_COVERAGE_REGISTER.md. It distinguishes documentation, basic contracts, passing CI, and actual integrations. This public register contains no links to C2O-private owner repositories or policy values.


## Encyclopedia toolchain — tenth owner-supplied source — 2026-11-12

- [Open UNIVERSALIS encyclopedia architecture](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Encyclopedias/blob/implementation/repository-foundation-2026-11-12/ENCYCLOPEDIA_TOOLCHAIN_ARCHITECTURE.md)
- [Portable evidence contracts](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Encyclopedias/blob/implementation/repository-foundation-2026-11-12/schemas/encyclopedia/encyclopedia-evidence-contracts.v1.schema.json)
- [Synthetic evidence fixtures](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Encyclopedias/blob/implementation/repository-foundation-2026-11-12/examples/encyclopedias/encyclopedia-evidence-contracts.v1.json)
- [Validation evidence](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Encyclopedias/blob/implementation/repository-foundation-2026-11-12/ENCYCLOPEDIA_TOOLCHAIN_VALIDATION.md)

Candidate inventory covers Alexandria, WikiNow, MeMex, Stoa, Flexible GraphRAG, docsiq, llm-wiki-compiler, CiteGuard, retractionwatch-mcp, Panda Research Tools, verifiable-memory, DocImprint, answerproof, ember-custody, mcai-knowledge, cite-citadel and llm-wiki-plugin. All remain candidates pending exact source/license/release/security/compatibility and data-flow checks. No corpus/compiler/source connector is claimed deployed.

See the [UNIVERSALIS ten-source master toolchain coverage register](https://github.com/C2O-Chaos-to-Order/Research-for-the-UNIVERSALIS-Ecosystem/blob/implementation/repository-foundation-2026-11-12/TOOLCHAIN_COVERAGE_REGISTER.md). The public register contains only public contracts and synthetic examples, not C2O-private ontology or corpus material.
