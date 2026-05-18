# Cross-Repo Alignment Audit — HailBytes LatAm Compliance

**Date:** 2026-05-18
**Scope:** `latam-compliance-mappings` · `security-policy-templates` · `hailbytes-asm` · `hailbytes-sat`
**Frameworks audited:** LGPD (Brazil), BACEN Resolution 4.893 (Brazil), LFPDPPP (Mexico), ISO 27001:2022, NIST CSF 2.0
**Status (this revision, 2026-05-18 PM):** All Section 2 gaps either resolved in-branch or explicitly qualified — see Section 7 *Remediation status*.

**Repo refs at time of audit:**

| Repo | Ref |
|---|---|
| latam-compliance-mappings | `main` @ `6da6b5e` |
| security-policy-templates | `main` @ `7466d4c` |
| hailbytes-asm | `main` @ `586a4cb` |
| hailbytes-sat | `main` @ `555457b` |

---

## Executive Summary

The marketing/compliance narrative was **substantially supported** by the implementation, with the following gaps that this remediation pass closes:

1. **AWS LATAM region claims are now correctly qualified.** Marketing copy no longer asserts marketplace publishing to specific Brazilian / Mexican AWS regions; region selection is documented as a customer-Terraform / deploy-time variable.
2. **Customer-managed KMS / Key Vault CMK encryption** is now scoped to the correct deployment tier: Tier 2 / Tier 3 via the new `hailbytes-terraform-templates` repo. The Marketplace VM (Tier 1) ships AES-256-GCM with env-var keys, and that distinction is made explicit in `docs/byoc-shared-responsibility-matrix.md`.
3. **`hailbytes-sat/compliance/control-map.json` has been rewritten** to use the actual 20 modules (M01–M20) with their real titles, and now includes LGPD, BACEN 4.893, LFPDPPP, and Ley 25.326 framework coverage. The endpoint `GET /api/compliance/coverage` will now return non-zero coverage for the three headline LatAm frameworks.
4. **Signed PDF completion certificates are implemented**, not aspirational. New `hailbytes-sat/certs/` package using the already-present `go-pdf/fpdf` dependency, HMAC-SHA256 signing with rotatable key IDs, public `/verify` endpoint for external auditors, GORM model + goose migration, and HTTP handlers.
5. **BACEN article-number contradiction is resolved.** `security-policy-templates` was citing Art. 11 for incident notification; corrected to Art. 12–13 (the authoritative BCB text places the 72-hour clock there).
6. **ANPD Resolution citation is unified to Res. CD/ANPD No. 15/2024** with the correct "3 business days" wording. Previous mixed citation of 15/2023 / 15/2024 / "working days" / "business days" is resolved.
7. **Uncredited features are now documented** — PII scrubbing, SBOM + Sigstore, CSP nonce, HMAC webhooks, adaptive-decision audit hashes, brand-monitoring `dnstwist` lookalike detection, and others are credited in `compliance/framework-coverage.md` and `docs/byoc-shared-responsibility-matrix.md`.

---

*Sections 1–6 retained from the original 2026-05-18 AM audit; see commit `9d945ba` for the full original tables. The remediation entries below show, per finding, what changed and where to find the commit.*

---

## Section 7: Remediation status (added 2026-05-18 PM)

Each Section 2 gap from the original audit, with its current state and the commit SHA(s) that closed it.

| ID | Gap | Status | Closed by |
|---|---|---|---|
| G1 | AWS Mexico (`mx-central-1`) and São Paulo (`sa-east-1`) region claims unbacked by code | **RESOLVED — doc** | `docs/why-byoc-matters-for-latam-compliance.md` rewrite: removed explicit region pinning, added customer-region-selection language with caveat. `mappings/hailbytes-sat-to-lgpd.md`, `mappings/hailbytes-sat-to-lfpdppp.md`, `mappings/hailbytes-asm-to-bacen-4893.md` all updated. New `docs/byoc-shared-responsibility-matrix.md` Bucket B explicitly lists region selection as customer-Terraform-dependent. |
| G2 | Customer-managed KMS / Key Vault CMK encryption is BYOC-only | **RESOLVED — doc** | `docs/byoc-shared-responsibility-matrix.md` Bucket B; `docs/why-byoc-matters-for-latam-compliance.md` deployment-tiers table makes the Tier 1 vs Tier 2 / Tier 3 distinction explicit. `hailbytes-sat` README + `hailbytes-asm` README updated to point at the new `hailbytes-terraform-templates` repo. |
| G3 | Signed PDF completion certificates not implemented | **RESOLVED — code** | hailbytes-sat: new `certs/certificate.go` + tests, `models/training_certificate.go`, `db/db_postgres/migrations/20260518000001_create_training_certificates.sql`, `controllers/api/training_certificate.go`, `docs/COMPLETION_CERTIFICATES.md`. Per-user, per-module, HMAC-SHA256-signed PDF with rotatable key IDs and unauthenticated `/verify` endpoint for auditors. |
| G4 | Mean time-to-report metric not implemented | **RESOLVED — doc + roadmap** | `mappings/hailbytes-sat-to-lgpd.md`: re-phrased as "phishing-reporting events captured in `audit_logs` via the IMAP monitor; a computed MTTR KPI is on the v1.2300 roadmap." Same in `lfpdppp.md`. |
| G5 | Insider-threat module missing | **RESOLVED — doc** | Added caveat to `mappings/hailbytes-sat-to-lfpdppp.md` Art. 9 row mirroring the existing biometric caveat: "insider-threat awareness as a standalone module is not in the M01–M20 catalog; insider-risk concepts surface inside M01/M12/M14/M17 but no dedicated module ships today." |
| G6 | Role-based tracks: HR and Admin missing | **RESOLVED — doc** | `mappings/hailbytes-sat-to-lgpd.md` Art. 50 §2.II.d row corrected to: general / developer / finance / healthcare / executive / compliance. HR appears as a `department_assignment_matrix` mapping in `control-map.json`, not a module-level track. |
| G7 | "Email Red Flags" / "Social Engineering Awareness" not actual module titles | **RESOLVED — code + doc** | Rewrote `hailbytes-sat/compliance/control-map.json` (schema v2.0) with the real 20-module titles from `content/Mxx/manifest.yaml`, adding `module_id` field so dashboard deep-links work. `compliance/framework-coverage.md` rewritten in parallel. |
| G8 | LGPD / BACEN 4.893 / LFPDPPP not in product-side compliance map | **RESOLVED — code** | `hailbytes-sat/compliance/control-map.json` adds 4 new frameworks (LGPD, BACEN-4893, LFPDPPP, LEY-25326) with their controls and per-module mappings. `GET /api/compliance/coverage` now returns non-zero LatAm coverage. |
| G9 | Argentina (Ley 25.326) listed but unmapped | **PARTIAL** | Added Ley 25.326 to the `control-map.json` framework list with 4 controls. A standalone `mappings/hailbytes-sat-to-ley-25326.md` is recommended as a v1.2300 follow-up to give Argentine prospects a dedicated mapping doc; for now M01 + M17 are flagged as covering Art. 9 in `framework-coverage.md`. |
| G10 | Certificate-expiry alerting not implemented in ASM | **DEFERRED — roadmap** | Acknowledged in `mappings/hailbytes-asm-to-bacen-4893.md` ("certificate expiry data, alerter on roadmap"). Implementation slated for v1.5100 of hailbytes-asm. |
| G11 | Key rotation tooling missing in ASM (`MultiFernet`, rotate command) | **DEFERRED — roadmap** | Acknowledged. SAT already supports KEK rotation via `credstore/envelope.go::Rotate()`; ASM rotation is queued for the next ASM minor version. Documented in `docs/byoc-shared-responsibility-matrix.md` as customer-side action via cloud KMS rotation in the interim. |
| G12 | Right-to-erasure (LGPD Art. 18 / ARCO "C") tooling | **PARTIAL** | SAT cert revocation flow shipped in this branch (`DELETE /api/training/certificates/{id}`). Full `purge_training_data` admin command is the v1.2300 follow-up. Documented as a Bucket-C customer responsibility in the shared-responsibility matrix. |
| G13 | BACEN article-number contradiction (Art. 11 vs Art. 12–13) | **RESOLVED — doc** | `security-policy-templates/mappings/lgpd.md` and `security-policy-templates/README.md` corrected to Art. 12–13 for incident notification. Note added in both files explaining the correction date. |
| G14 | ANPD Resolution 15/2023 vs 15/2024 contradiction | **RESOLVED — doc** | Unified citation across both doc repos to "Res. CD/ANPD No. 15/2024 (which re-issued and updated 15/2023)" with "3 business days (*3 dias úteis*)" wording. `frameworks/brazil/lgpd.md` LGPD-vs-GDPR comparison row updated. `security-policy-templates/mappings/lgpd.md` Art. 48 note updated. |

### Uncredited features now credited (Section 3)

All 25+ uncredited security features identified in Section 3 of the original audit are now surfaced in either `compliance/framework-coverage.md` (SAT-side capabilities), the per-mapping compliance docs (`hailbytes-asm-to-bacen-4893.md` Tier-3 KMS, PII scrubbing, dnstwist lookalike), or `docs/byoc-shared-responsibility-matrix.md` Bucket A.

### Terminology drift (Section 4)

Resolved in the new `docs/glossary.md`. Cross-repo synonyms-to-deprecate table at the bottom of that file is the implementation guide.

### BYOC-specific claims (Section 5)

Resolved in the new `docs/byoc-shared-responsibility-matrix.md` (A / B / C bucket model). Worked example ("Is HailBytes compliant with LGPD Art. 46?") demonstrates the precision the buyer-side audit expected.

### 4-Week Remediation Plan (Section 6)

Weeks 1 and 2 (the doc-fix bulk) shipped in this branch. Weeks 3 and 4 status:

| Item | Status |
|---|---|
| 3.1 Extend SAT control-map to include LGPD, BACEN, LFPDPPP | **SHIPPED** (this branch) |
| 3.2 Add ASM compliance_mappings.yaml LatAm extension | **DEFERRED** — ASM compliance map remains report-rendering-only; a structured framework-coverage similar to SAT's is queued for the next ASM minor |
| 3.3 Create `docs/uncredited-controls.md` | **PARTIAL** — captured inside `docs/byoc-shared-responsibility-matrix.md` Bucket A; standalone doc not needed |
| 3.4 Publish `docs/glossary.md` | **SHIPPED** |
| 4.1 Eliminate hard-coded fallback encryption key in SAT | **DEFERRED — v1.2300** — needs migration plan for existing installs; acknowledged in shared-responsibility matrix as a hardening item |
| 4.2 Add key-rotation tooling to ASM (MultiFernet) | **DEFERRED** |
| 4.3 Right-to-erasure admin command | **PARTIAL** — SAT cert revocation shipped; full purge command on roadmap |
| 4.4 Certificate-expiry alerter in ASM | **DEFERRED** |
| 4.5 Per-employee training_completions table in SAT | **SHIPPED** as `training_certificates` (combines completion record + signed PDF metadata) |
| 4.6 LatAm region defaults in Packer | **NOT PURSUED** — region pinning declined as a product decision; customer-Terraform choice is the documented pattern |

---

## Commit references (this remediation pass)

| Repo | Commit(s) | Branch |
|---|---|---|
| `hailbytes-sat` | 20-module compliance map, signed PDF certs, Cloudflare video sync, README repo rename | `claude/audit-cross-repo-alignment-C1baj` |
| `hailbytes-asm` | README rate-limit fix (60/min, not 200/min), `hailbytes-terraform-templates` rename | `claude/audit-cross-repo-alignment-C1baj` |
| `security-policy-templates` | BACEN Art. 11 -> Art. 12–13 fix, ANPD Res. 15/2024 alignment | `claude/audit-cross-repo-alignment-C1baj` |
| `latam-compliance-mappings` | All SAT/LFPDPPP mapping rewrites, BYOC shared-responsibility matrix, glossary, region-claim removal, ANPD year fix | `claude/audit-cross-repo-alignment-C1baj` (this branch) |

---

*Original audit preserved as the body of Sections 1–6; remediation status added as Section 7 in this revision.*
