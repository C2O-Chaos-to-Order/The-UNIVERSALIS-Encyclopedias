# Encyclopedia Toolchain Architecture — UNIVERSALIS

**Boundary:** Open, local-first, independently operable MotherThread. **Status:** Portable contracts implemented; production compiler not deployed.

Knowledge is maintained as versioned, claim-level cited artifacts, not answers treated as encyclopedias. Preserve source capture, claims, citations, corrections, contradictions, history and unresolved questions.

Open candidates:
- **Alexandria:** local cited wiki, deterministic quote checks and claim supersession; verify release/source-type coverage and reported 99.9% citation rate.
- **WikiNow:** local wiki/MCP candidate; supplied 21-tool count unverified; FTS5 is a search cache, not fact validation.
- **MeMex:** Markdown + Git wiki with citation lint, quarantine and human conflict resolution; zero-hallucination is not a truth guarantee.
- **Stoa:** local graph candidate; upstream describes Markdown + OKF + JSON-LD and Postgres/pgvector; verify round-trip and local/offline deployment.
- **Flexible GraphRAG:** graph/RDF/vector hybrid retrieval; backend counts vary by release/page.
- **docsiq:** Go GraphRAG/MCP candidate; pin source and release.
- **llm-wiki-compiler:** local Markdown compiler, freshness, lint/eval, context packs and OKF exchange; v0.11.0 changelog reports 11 MCP tools.
- **CiteGuard:** OpenAlex + Crossref/Retraction Watch; current repository calls itself early-development/MVP.
- **retractionwatch-mcp:** Crossref-distributed Retraction Watch MCP; preserve update_type/evidence.
- **Panda Research Tools:** supplied eight-tool claim requires manifest verification.
- **verifiable-memory:** Merkle fact memory candidate; pin repository/proof profile/threat model.
- **DocImprint:** SHA-256/Merkle evidence candidate; chain anchoring is hash publication, not legal notarization.
- **answerproof:** signed receipts and retrieval-set Merkle roots.
- **ember-custody:** redactable Merkle custody/deletion candidate; inspect residual metadata.
- **mcai-knowledge:** cited term/Q&A assets; verify license.
- **cite-citadel:** OKF cited wiki/MCP candidate; verify canonical source.
- **llm-wiki-plugin:** wiki skill/plugin; hosted deployment needs privacy review.

Standards: OKF 0.2 is Markdown + YAML frontmatter; JSON-LD 1.1 is a W3C linked-data Recommendation; RFC 9162 defines the portable Merkle construction. Name SHA-256/SHA3-256 per content digest; do not mix them within a tree without an explicit profile.

The v1 contracts cover source/rights, ingestion manifests/chunks, citation anchors/proofs/receipts, coverage, editorial status, knowledge assets, OKF/JSON-LD exports, evidence bundles, corrections and answer receipts.

Proof profile: leaf = SHA-256(0x00 || canonical payload); internal = SHA-256(0x01 || left || right). Proof includes tree size, leaf index, path and root. Membership does not prove source authenticity, quotation correctness, truth, completeness, publisher authority or retraction-free status.


## Portable signature envelope metadata — 2026-11-12

The shared v1 schema now permits an optional signature envelope on ingestion manifests, citation-proof receipts, OKF/JSON-LD export manifests, content-addressed evidence bundles, correction events and answer-evidence receipts. The envelope carries algorithm, key fingerprint, optional public-key reference, signed-payload digest, signature bytes, timestamp and verifier status. It contains no private key material.

This is a transport contract only. Current CI does not create signatures, resolve public keys, evaluate revocation, or verify Ed25519/ML-DSA signatures. A `verification_status` of `not-run` or `unknown-key` is not an attestation of authenticity. The receiver must verify the signature over the declared canonical payload digest with an independently trusted key and policy.
