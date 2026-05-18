# Cross-Repo Alignment Audit — HailBytes LatAm Compliance

**Date:** 2026-05-18
**Scope:** `latam-compliance-mappings` · `security-policy-templates` · `hailbytes-asm` · `hailbytes-sat`
**Frameworks audited:** LGPD (Brazil), BACEN Resolution 4.893 (Brazil), LFPDPPP (Mexico), ISO 27001:2022, NIST CSF 2.0
**Repo refs at time of audit:**

| Repo | Ref |
|---|---|
| latam-compliance-mappings | `main` @ `6da6b5e` |
| security-policy-templates | `main` @ `7466d4c` |
| hailbytes-asm | `main` @ `586a4cb` |
| hailbytes-sat | `main` @ `555457b` |

---

## Executive Summary

The marketing/compliance narrative is **substantially supported** by the implementation, but there are **material gaps that would surface in any real enterprise audit**:

1. **AWS Mexico (`mx-central-1`) and AWS São Paulo (`sa-east-1`) region claims are not backed by any code, Packer config, or marketplace listing in either product repo.** Defaults are `us-east-1` and Azure `centralus`. Azure Brazil South / Mexico Central are equally absent from the product code.
2. **Customer-managed KMS / Key Vault CMK encryption is NOT a property of the products shipped from these four repos.** It lives in a separate `byoc-security-architecture-templates` repo that is out of scope for this audit and is a Terraform reference, not a product feature. The default Marketplace AMI **explicitly disables EBS encryption** (`marketplace/packer/hailbytes-asm.pkr.hcl:165`), and `hailbytes-sat` ships with a hard-coded fallback encryption key (`crypto/keymanagement.go:27`) used unless `HAILBYTES_ENCRYPTION_KEY` env var is set.
3. **`hailbytes-sat` carries its own machine-readable compliance map (`compliance/control-map.json`, `compliance/framework-coverage.md`) that covers SOC 2 / ISO 27001 / HIPAA / PCI DSS / NIST CSF / NIST 800-53 / CMMC / GDPR / NYDFS — but does NOT include LGPD, BACEN 4.893, or LFPDPPP.** The product's own API endpoint `GET /api/compliance/coverage` therefore returns 0% coverage for the three LatAm frameworks this repo's mappings advertise.
4. **`hailbytes-asm` has no equivalent in-product compliance map** beyond `web/hailbytes_asm/compliance_mappings.yaml` (used for report generation, not framework attestation).
5. **Signed PDF completion certificates** are claimed in `mappings/hailbytes-sat-to-lgpd.md` as ANPD-audit evidence; **the SAT codebase contains no PDF generation library and no `CompletionCertificate` model.** The only `Certificate` type is for TLS (`hailbytes-sat/models/certificate.go`).
6. **BACEN 4.893 article numbering contradicts between the two documentation repos.** `latam-compliance-mappings` cites Art. 12–13 for the 72-hour incident notification clock; `security-policy-templates` cites Art. 11. **One of them is wrong.**
7. **ANPD Resolution citation contradicts** — `15/2023` vs `15/2024` between the two documentation repos.
8. **Substantial security functionality is uncredited** in the LatAm mappings: PII scrubbing, supply-chain attestation (SBOM + Sigstore + Trivy SARIF), CSP with per-request nonce, HMAC-signed webhooks, adaptive-decision audit hashes, envelope-encrypted credential store with rotation, brand-monitoring phishing-lookalike detection (`dnstwist`), bug-bounty ingestion, and more.

The risk profile is **moderate, not catastrophic**: the products implement strong security controls, and the BYOC posture is real for customers who deploy via the external Terraform repo. But the *gap between what is claimed and what is shipped from the four audited repos is wide enough that a buyer-side technical due diligence would flag at least 6–8 of the items below as either misleading or unverifiable.*

---

## Section 1: Control Claims Inventory

> **Reading the table.** "Aligned" = claim is supported by both policy text and product code. "Gap" = claim is asserted but no implementing code/config exists in the product repos. "Contradiction" = the same control is described differently across repos in a way a buyer would notice. "Unverifiable" = depends on customer-side BYOC Terraform that lives outside the four repos in scope.

| Framework | Control ID | Claimed in latam-compliance-mappings | Stated in security-policy-templates | Evidence in hailbytes-asm | Evidence in hailbytes-sat | Alignment |
|---|---|---|---|---|---|---|
| LGPD | Art. 6 (Principles) | `mappings/hailbytes-sat-to-lgpd.md` lines 24-30: SAT modules satisfy principles via "Phishing Basics, Email Red Flags, Password Security, Social Engineering Awareness, CEO Fraud & BEC" | `mappings/lgpd.md` lines 18-35: maps to multiple policies | n/a | `content/M01..M20/manifest.yaml`; 3/5 named modules explicit (M07 Credential Phishing, M19 Password Hygiene, M06 BEC). "Email Red Flags" and standalone "Social Engineering Awareness" are *distributed* across M01/M09/M13, not single-named modules. | **Gap** (module names drift from product) |
| LGPD | Art. 33 (Int'l Transfer) | `docs/why-byoc-matters-for-latam-compliance.md` lines 41-50: "BYOC in AWS São Paulo / Azure Brazil South — None — no transfer mechanism needed" | `mappings/lgpd.md` (not directly addressed) | No `sa-east-1` reference in code; Packer defaults `us-east-1`/`centralus` (`marketplace/packer/variables.pkr.hcl:97,124,130`) | No `sa-east-1` reference; deploy scripts region-agnostic (`deploy/aws/cloudformation-ha.yaml`) | **Gap** (region claim unbacked) |
| LGPD | Art. 37 (Records of Processing) | `mappings/hailbytes-sat-to-lgpd.md`: "Audit logs stored in customer's own cloud account" | `mappings/lgpd.md`: maps to data classification policy | `web/dashboard/models.py` AuditLog model; `web/dashboard/signals.py:35` auto-fans to SIEM | `audit/audit.go:31-49` AuditEntry + `audit_logs` table; `audit/retention.go` retention controls | **Aligned** |
| LGPD | Art. 46 (Security Measures — encryption at rest) | `docs/why-byoc-matters-for-latam-compliance.md`: "Customer controls encryption keys, access policies" | `mappings/lgpd.md` lines 60-77: maps to multiple infra policies | Field-level Fernet via env-var key (`web/hailbytes_asm/crypto.py:14,51`); **no KMS SDK in this repo**; Marketplace AMI EBS encryption *disabled* (`marketplace/packer/hailbytes-asm.pkr.hcl:165`) | AES-256-GCM (`crypto/encryption.go`); **hard-coded fallback key** at `crypto/keymanagement.go:27` (`defaultEncryptionKey = "HailBytesSATDefaultKey2026!!"`); no AWS-KMS / Key Vault call in this repo | **Contradiction** (claim says CMK; default ship state does not enforce it) |
| LGPD | Art. 46 (Security Measures — TLS in transit) | Implicit in BYOC narrative | `mappings/lgpd.md` Art. 46 row, `policies/03-communications/email_policy.md` | nginx TLS, HSTS preload, `SECURE_PROXY_SSL_HEADER`, `sslmode=require` (`web/hailbytes_asm/settings.py`) | `acme/`, `customdomain/customdomain.go:113` (30-day renewal), `models/certificate.go` (Let's Encrypt + self-signed lifecycle) | **Aligned** |
| LGPD | Art. 46 (RBAC) | n/a (claim is general "access control") | `mappings/lgpd.md` Art. 46 row → `password_protection_policy.md` | 3 roles via `django-rolepermissions` at `web/hailbytes_asm/roles.py:13`; project-scoped middleware `web/dashboard/middleware.py:75` | `middleware/permissions.go:8-89` with `PermissionModifySystem`/`PermissionModifyObjects` enforcement and deny-event logging | **Aligned** |
| LGPD | Art. 47 (Confidentiality of agents) | `mappings/hailbytes-sat-to-lgpd.md`: SAT modules on data handling/insider threat | `mappings/lgpd.md` lines 79-86 | n/a | **No dedicated "insider threat" module** in M01–M20 (searched manifests); closest are M14 (HIPAA §164.530(b)) and M17 (GDPR) | **Gap** |
| LGPD | Art. 48 (72-hour breach notification) | `frameworks/brazil/lgpd.md` line 92: "3 business days per Res. CD/ANPD No. **15/2023**" | `mappings/lgpd.md` line 100: "ANPD Resolution CD/ANPD No. **15/2024** requires notification within **3 working days**" | n/a | n/a | **Contradiction** (year and "working" vs "business" days mismatch) |
| LGPD | Art. 48 (Incident reporting training) | `mappings/hailbytes-sat-to-lgpd.md` row 5 | `mappings/lgpd.md` → `data_breach_response_policy.md` | n/a | `content/M18/manifest.yaml` — "Incident Reporting Done Right"; maps to SOC2 CC7.3, ISO27001 A.5.24 | **Aligned** |
| LGPD | Art. 50 §2(d) (Training program) | `mappings/hailbytes-sat-to-lgpd.md` row 7 — SAT "directly fulfils" with role-based tracks | n/a | n/a | `target_role:` in module manifests (`developer`, `finance`, `healthcare`, `executive`, `compliance`); adaptive engine ranks per-role (`adaptive/adaptive.go:120-186`); **but `target_role: admin` and `target_role: hr` are NOT module tracks** (HR appears only as phishing-template folder) | **Gap** (role list overstated) |
| LGPD | Art. 50 §2 (Audit trail / signed certificates) | `mappings/hailbytes-sat-to-lgpd.md` line 64: "Completion certificates (signed PDF)" | n/a | n/a | **NOT FOUND**: no PDF library imported (`go.mod`); only TLS certs in `models/certificate.go`; xAPI completion statements via `scorm/scorm.go:215-272` exist but require external LRS | **Gap** (high audit exposure) |
| BACEN 4.893 | Art. 4 (Cybersecurity Policy) | `mappings/hailbytes-asm-to-bacen-4893.md` line 23: ASM provides "continuous data to feed vulnerability management procedures" | `README.md` line 154 table + `mappings/lgpd.md`'s BACEN section | Hatchet scan pipeline (`web/hailbytes_asm/workflows/scan.py`); nuclei integration; `web/hailbytes_asm/compliance_mappings.yaml` | n/a | **Aligned** |
| BACEN 4.893 | Art. 6 (Testing & Monitoring) | `mappings/hailbytes-asm-to-bacen-4893.md` line 25 | `mappings/lgpd.md` BACEN Art. 5 row (NB: article number drift; see below) | Scheduled scans (`web/hailbytes_asm/workflows/scheduling.py`, `web/dashboard/models.py::ScanSchedule`); 30+ recon tools | n/a | **Aligned** (but see Section 4 on article-number drift) |
| BACEN 4.893 | Art. 7 (Third-Party Risk) | `mappings/hailbytes-asm-to-bacen-4893.md` line 27: ASM "monitors the external footprint of third-party domains" | `mappings/lgpd.md` Art. 7 row | Project model supports per-vendor scoping; `web/cloudConnectors/webhook_views.py` for inbound asset ingest. **No first-class "Vendor" model** — vendors are modeled as separate Projects. | n/a | **Partial / Gap** (works in practice; no dedicated abstraction) |
| BACEN 4.893 | Art. 11 (Cloud Service Oversight — claimed) | `mappings/hailbytes-asm-to-bacen-4893.md` line 29 maps Art. 11 to "cloud asset discovery" | n/a | `web/cloudConnectors/connectors/aws.py:67` (8 service iterators), `azure.py`, `gcp.py`, `cloudflare.py`; `0.0.0.0/0` ingress detector at `aws.py:131` | n/a | **Aligned** on capability, **Contradiction** on article number — see Art. 14/16 row below |
| BACEN 4.893 | Art. 12–13 (72h incident notification) | `mappings/hailbytes-asm-to-bacen-4893.md` line 31; `frameworks/brazil/bacen-4893.md` lines 42-50 | `mappings/lgpd.md` BACEN section places "Incident Reporting" at **Art. 11** | n/a | n/a | **Contradiction** between the two doc repos |
| BACEN 4.893 | Art. 14 (BCB Audit Rights / Cloud) | `mappings/hailbytes-asm-to-bacen-4893.md` line 33: "Customer is the data controller; all scan data and reports are in the customer's BCB-auditable account" | `mappings/lgpd.md` BACEN section maps Art. 7 to cloud services | All data in customer's PostgreSQL (`web/hailbytes_asm/settings.py`); no outbound by default | All data in customer's PostgreSQL; `audit/retention.go` retention controls | **Aligned** (BYOC posture supports this regardless of region) |
| BACEN 4.893 | Art. 17 (Annual Board Report) | `mappings/hailbytes-asm-to-bacen-4893.md` line 35 | n/a | WeasyPrint PDF reports via `web/startScan/views.py::create_report`; scheduled deliveries via `web/dashboard/views_scheduled_report.py` | `reportdelivery/exec_report.html.tmpl` (16 KB) + 6 delivery channels (`email.go`, `slack.go`, `teams.go`, etc.) | **Aligned** |
| LFPDPPP | Art. 9 (Sensitive data — biometric) | `mappings/hailbytes-sat-to-lfpdppp.md` Art. 9 row: "biometric-specific training content is not a current built-in module" — *self-disclosed gap* | n/a | n/a | Confirmed: no biometric module in `content/M01..M20` | **Aligned** (claim correctly self-disclosed) |
| LFPDPPP | Art. 19 (Security Measures — administrative) | `mappings/hailbytes-sat-to-lfpdppp.md` line 28: SAT is the administrative measure | n/a | n/a | Training modules + completion audit events (`audit/events.go:53 EventCompleted`) | **Aligned** (light) |
| LFPDPPP | Art. 21 (Security Breach training) | `mappings/hailbytes-sat-to-lfpdppp.md` line 30 | n/a | n/a | M18 + IMAP report monitoring (`imap/monitor.go`); MTTR metric not implemented | **Partial** (training present; metric not) |
| LFPDPPP | Art. 36 (Third-party transfers / processor) | `mappings/hailbytes-sat-to-lfpdppp.md`: "customer is the processor of their own training data; no third-party data transfer occurs with BYOC" | n/a | BYOC posture supports this | BYOC posture supports this (note: SAT Worker does egress to SMTP/IMAP/SIEM but that's customer-configured) | **Aligned** |
| LFPDPPP | Art. 37 (International Transfer — Mexico region) | `docs/why-byoc-matters-for-latam-compliance.md`: "AWS Mexico City (mx-central-1) / Azure Mexico Central" | n/a | **No `mx-central-1` string in repo** (grep returned 0 hits); Packer defaults `us-east-1` | **No `mx-central-1` string in repo**; deploy scripts region-agnostic | **Gap** (region claim unbacked) |
| ISO 27001:2022 | A.5.24–A.5.26 (Incident management) | `frameworks/regional/iso-27001-latam-notes.md` line 100 | `mappings/iso-27001.md` lines 85-105 | `web/dashboard/dispatch.py:55` SIEM fan-out; `AuditLog` model | `audit/audit.go` + `reportdelivery/` 6 channels; M18 incident-reporting module | **Aligned** |
| ISO 27001:2022 | A.6.3 (Awareness, Education, Training) | `docs/enterprise-trust-package.md` line 52: "SAT maps to Annex A 6.3 (awareness) and 5.26 (incident response)" | `mappings/iso-27001.md` line 89: maps A.6.3 to `acceptable_use_policy.md`, `email_policy.md`, `ethics_policy.md` | n/a | `compliance/framework-coverage.md` explicitly lists 5 modules → ISO 27001 A.6.3 / A.8.2 / A.5.14 | **Aligned** |
| ISO 27001:2022 | A.8.5 (Secure Authentication / MFA) | n/a | `mappings/iso-27001.md` line 137: maps A.8.5 to `password_protection_policy.md` | TOTP via `django_otp` (`web/hailbytes_asm/settings.py:154-158`); `TWO_FACTOR_LOGIN_TIMEOUT=600` | `mfa/totp.go:23-95` (RFC 6238, QR code, 10 backup codes); `middleware/mfa.go` enforces | **Aligned** |
| ISO 27001:2022 | A.8.8 (Technical Vulnerabilities) | `frameworks/regional/iso-27001-latam-notes.md` line 86: "Vulnerability testing requirements (Art. 6) align with ISO 27001 Annex A 8.8" | `mappings/iso-27001.md` line 148 | Nuclei + dalfox + crlfuzz + s3scanner + naabu/nmap (`web/startScan/tasks.py`); auto-updating templates | n/a | **Aligned** |
| ISO 27001:2022 | A.5.23 (Cloud security) | `frameworks/regional/iso-27001-latam-notes.md` line 110 | `mappings/iso-27001.md` line 117 | `web/cloudConnectors/connectors/{aws,azure,gcp,cloudflare}.py` | n/a | **Aligned** |
| ISO 27001:2022 | A.5.19–A.5.22 (Supplier relationships) | `frameworks/regional/iso-27001-latam-notes.md` line 88 | `mappings/iso-27001.md` line 102 | Project model + cloud webhook ingest | n/a | **Partial** (no first-class vendor concept) |
| NIST CSF 2.0 | GV.PO (Policy) | `frameworks/regional/nist-csf-portuguese.md` line 84 | `mappings/nist-csf.md` GV.PO-01 | n/a | n/a | **Aligned** (policy-level, no code dependency) |
| NIST CSF 2.0 | ID.AM (Asset Mgmt) | `frameworks/regional/nist-csf-portuguese.md` line 87 | `mappings/nist-csf.md` lines 32-42 | Continuous discovery via Hatchet pipeline; `web/cloudConnectors/`; `web/startScan/models.py::Subdomain.found_at` | n/a | **Aligned** |
| NIST CSF 2.0 | PR.AA (Identity & Access) | `frameworks/regional/nist-csf-portuguese.md` line 89 | `mappings/nist-csf.md` PR.AA-01..06 | `web/hailbytes_asm/roles.py`, `web/dashboard/middleware.py:75`, SCIM 2.0 in `web/api/scim/` | `middleware/permissions.go`, `scim/scim.go`, `mfa/totp.go`, `sso/manager.go` (OIDC + SAML) | **Aligned** |
| NIST CSF 2.0 | PR.DS (Data Security) | `frameworks/regional/nist-csf-portuguese.md` line 90 | `mappings/nist-csf.md` lines 75-83 | Fernet field encryption (env-var key); TLS in transit | AES-256-GCM (env-var key with hard-coded fallback); envelope-encrypted credstore | **Partial** (encryption present but BYOK is conditional) |
| NIST CSF 2.0 | DE.CM (Continuous Monitoring) | `frameworks/regional/nist-csf-portuguese.md` line 92 | `mappings/nist-csf.md` lines 89-94 | Scheduled scans + SIEM dispatch; `web/dashboard/signals.py:35` real-time fan-out | n/a (SAT is preventive, not monitoring) | **Aligned** (ASM-side) |
| NIST CSF 2.0 | RS.MA / RS.CO (Incident Response) | `frameworks/regional/nist-csf-portuguese.md` lines 93-95 | `mappings/nist-csf.md` lines 96-114 | SIEM/ticketing fan-out (`web/dashboard/ticket_dispatch.py`) | M18 + IMAP report monitor; `audit/audit.go` retention; no MTTR metric | **Partial** (capability present, MTTR metric missing) |
| NIST CSF 2.0 | RC.RP (Recovery) | `frameworks/regional/nist-csf-portuguese.md` line 97; "standalone business continuity modules are not part of the current built-in library" — *self-disclosed gap* | `mappings/nist-csf.md` RC.RP-01..05 → `disaster_recovery_plan_policy.md` | n/a | n/a | **Aligned** (gap correctly self-disclosed) |

---

## Section 2: Gaps Where Claims Outpace Implementation

> These are the **highest-risk items**. Each is a place where the LatAm compliance docs or security-policy-templates assert a control that has no implementing code, config, or workflow inside the four product/policy repos. In a buyer audit, these are the items most likely to trigger a "show me the evidence" follow-up that we can't satisfy.

### G1. AWS Mexico (`mx-central-1`) and AWS São Paulo (`sa-east-1`) region claims [CRITICAL]

- **Claim:** `docs/why-byoc-matters-for-latam-compliance.md` lines 80-85: "Marketplace deployment supports AWS São Paulo (sa-east-1), AWS Mexico City (mx-central-1), Azure Brazil South, Azure Mexico Central."
- **Code reality:**
  - `hailbytes-asm/marketplace/packer/variables.pkr.hcl:97` — Azure replication regions default `["centralus"]`.
  - `hailbytes-asm/marketplace/packer/variables.pkr.hcl:124,130` — AWS region defaults `us-east-1` (build and replicate).
  - Repo-wide grep for `sa-east-1`, `mx-central-1`, `brazilsouth`, `mexicocentral` — **0 hits** in both `hailbytes-asm` and `hailbytes-sat`.
  - `hailbytes-sat/deploy/aws/cloudformation-ha.yaml` and `provision-ha.sh` are region-agnostic but **not pinned to or validated against** any LatAm region.
- **Why it matters:** The entire LGPD Art. 33 / LFPDPPP Art. 37 narrative in `docs/why-byoc-matters-for-latam-compliance.md` rests on the customer's ability to deploy in a LatAm region. AWS Mexico region (`mx-central-1`) only became generally available in early 2025 and its operational maturity vs. our Marketplace VM publishing status is unverified. **AWS Mexico City marketplace publishing is not in the AWS Marketplace listing docs (`marketplace/aws/AWS_MARKETPLACE_LISTING.md`).**

### G2. Customer-managed KMS / Key Vault CMK encryption [CRITICAL]

- **Claim:** `docs/why-byoc-matters-for-latam-compliance.md` Architecture Overview: "Encryption: Customer KMS keys" within the BYOC boundary; `docs/enterprise-trust-package.md` line 75: "all data encrypted using your KMS keys (AWS) or Azure Key Vault keys."
- **Code reality (ASM):**
  - `web/hailbytes_asm/crypto.py:14` — `get_encryption_key()` reads `ASM_ENCRYPTION_KEY` from env, raises `ImproperlyConfigured` if unset. No KMS SDK call.
  - `marketplace/packer/hailbytes-asm.pkr.hcl:165` — comment: "EBS encryption is intentionally disabled at image level for marketplace certification; customer enables KMS post-launch."
  - `web/core/secrets/` — PAM resolvers exist for `vault://`, `azure-kv://`, `aws-sm://` references (lazily imported SDKs), but these are for *secrets retrieval*, not data-at-rest envelope encryption.
- **Code reality (SAT):**
  - `crypto/keymanagement.go:27` — `defaultEncryptionKey = "HailBytesSATDefaultKey2026!!"`. This is the fallback when `HAILBYTES_ENCRYPTION_KEY` is unset.
  - `crypto/keymanagement.go:194-197 IsProductionReady()` correctly returns `false` in the default state — but the binary **runs** with the default key.
  - `credstore/envelope.go:31-101` — proper envelope encryption is implemented, **but the KEK source is the caller's choice; no AWS-KMS / Azure Key Vault SDK in this repo.**
- **Why it matters:** Customer-managed encryption is materially different from "the vendor ships AES-256-GCM with an env var that the customer can set." For a BACEN 4.893 Art. 4 audit, examiners will want evidence that key custody is the customer's; for LGPD Art. 46, they will want evidence of cryptographic separation. Both are achievable via the external `byoc-security-architecture-templates` repo, but **that's a customer-installed Terraform module, not a product feature**, and the compliance docs don't clearly distinguish.

### G3. Signed PDF completion certificates [HIGH]

- **Claim:** `mappings/hailbytes-sat-to-lgpd.md` line 64: "Training completion records — per-employee, per-module, timestamped; Completion certificates (signed PDF)."
- **Code reality:** Zero PDF generation code in `hailbytes-sat`. `models/certificate.go` is for TLS certificates only (`CertTypeLetsEncrypt`, `CertTypeSelfSigned`). No `gofpdf`/`pdfcpu`/`chromedp` dependency. `scorm/scorm.go:215-272 NewCompletionStatement` produces xAPI statements for an external LRS — not signed PDFs.
- **Why it matters:** ANPD audit evidence packages routinely include signed completion certificates. The claim is in a marketing-grade compliance mapping; a customer who pulls the SAT product expecting to hand auditors signed PDFs will not find that capability.

### G4. Mean time-to-report metric [HIGH]

- **Claim:** `mappings/hailbytes-sat-to-lgpd.md` line 33: "mean time-to-report metrics from simulations"; `docs/enterprise-trust-package.md`.
- **Code reality:** `imap/monitor.go` captures user-reported phish events. Repo-wide grep for `mean_time_to_report` / `MTTR` returns 0 hits. No computed metric, dashboard widget, or report row was located.
- **Why it matters:** "Time to report" is a standard SAT-vendor KPI; its absence will be noticed by procurement teams comparing against KnowBe4 / Proofpoint.

### G5. Insider-threat training module [MEDIUM]

- **Claim:** `mappings/hailbytes-sat-to-lgpd.md` row Art. 47: "SAT modules covering data handling, confidentiality obligations, and **insider threat awareness**."
- **Code reality:** Searched M01–M20 manifests for "insider threat" — 0 hits. Closest content is M14 (HIPAA §164.530(b) workforce confidentiality) and M17 (GDPR data subject rights).
- **Why it matters:** Insider threat is a named requirement under LFPDPPP Reglamento Art. 48 sensitive-data handling.

### G6. Role-based tracks: HR and Admin missing [MEDIUM]

- **Claim:** `mappings/hailbytes-sat-to-lfpdppp.md` line 25 and `mappings/hailbytes-sat-to-lgpd.md`: "Role-based training tracks (admin, developer, HR, finance, healthcare, executive)."
- **Code reality:** `content/Mxx/manifest.yaml` `target_role:` values found: `all`, `developer`, `finance`, `healthcare`, `executive`, `compliance`. **`admin` and `hr` are NOT module `target_role` values.** The `training_templates/hr-payroll/` folder contains *phishing-email templates*, not training modules — the LatAm doc collapses two different concepts.
- **Why it matters:** This is a precise factual claim about product capability that does not match the shipped module catalog.

### G7. "Email Red Flags" / "Social Engineering Awareness" as named built-in modules [MEDIUM]

- **Claim:** `mappings/hailbytes-sat-to-lgpd.md` line 22: "built-in modules: Phishing Basics, Email Red Flags, Password Security, Social Engineering Awareness, CEO Fraud & BEC."
- **Code reality:** `hailbytes-sat/compliance/framework-coverage.md` lists 5 modules: **Phishing Basics**, **Email Red Flags**, **Password Security Basics**, **Social Engineering Awareness**, **CEO Fraud & BEC**. The names exist in the compliance metadata. **But** the `content/M01..M20` manifests use different titles (M01 "Security Foundations for Everyone", M07 "Credential Phishing Defenses", M19 "Password Hygiene & Passkeys", M06 "Anatomy of a BEC"). The compliance map and the module manifests refer to the same content by different names.
- **Why it matters:** A buyer who searches the module catalog for "Email Red Flags" will not find it as a module title; they'll find it only in the compliance map.

### G8. LGPD / BACEN 4.893 / LFPDPPP NOT in product-side compliance map [CRITICAL]

- **Claim:** `latam-compliance-mappings/mappings/*` and `docs/enterprise-trust-package.md` line 50 advertise SAT/ASM coverage of LGPD, BACEN 4.893, LFPDPPP.
- **Code reality:** `hailbytes-sat/compliance/framework-coverage.md` and `hailbytes-sat/compliance/control-map.json` cover **SOC 2, ISO 27001, HIPAA, PCI DSS, NIST CSF, NIST 800-53 Rev 5, CMMC 2.0, GDPR (Art. 32/39), NYDFS 23 NYCRR 500** — but **not LGPD, BACEN 4.893, or LFPDPPP.** The endpoint `GET /api/compliance/coverage` therefore returns 0% for the three frameworks this repo advertises. `hailbytes-asm` has no equivalent framework-coverage map at all; only `web/hailbytes_asm/compliance_mappings.yaml` for report rendering.
- **Why it matters:** The product API a buyer's auditor would inspect *does not surface coverage* for our headline LatAm frameworks. This is the single biggest documentation/code drift in the audit.

### G9. Argentina (Ley 25.326) framework with no product mapping [MEDIUM]

- **Claim:** `latam-compliance-mappings/README.md` table line 60: "Argentina · Ley 25.326" listed; `frameworks/argentina/ley-25326.md` exists.
- **Code reality:** `mappings/` directory contains only LGPD, BACEN 4.893, LFPDPPP product mappings. No `hailbytes-sat-to-ley-25326.md` or `hailbytes-asm-to-ley-25326.md` exists. The framework reference is loaded but unmapped.
- **Why it matters:** Argentine prospects pulling the README will find a top-level promise that the documentation library does not deliver.

### G10. Certificate-expiry alerting / proactive monitoring [MEDIUM]

- **Claim:** Implicit in `mappings/hailbytes-asm-to-bacen-4893.md` (BACEN Art. 4 "preventive controls"): TLS audit, certificate posture.
- **Code reality:** `web/config/default_scan_engines/TLS & Certificate Audit.yaml` captures cipher/protocol/cert posture. Repo grep for `cert_expires_at`, `certificate_expiry_alert`, `expire_threshold` — 0 hits. Expiry is collected but not alerted on with thresholds.
- **Why it matters:** Buyers expect "alert me 30 days before a cert expires." We collect the data but don't ship the alerter.

### G11. Key rotation tooling in ASM [HIGH]

- **Claim:** Implicit in `docs/enterprise-trust-package.md`: "all data encrypted using your KMS keys." KMS implies rotation.
- **Code reality (ASM):** `web/hailbytes_asm/crypto.py` uses single Fernet key. No `rotate_encryption_key` command, no `MultiFernet`. `decrypt_value` (`crypto.py:48`) falls back to plaintext on `InvalidToken` — supports a one-way migration but not true rotation.
- **Code reality (SAT):** `credstore/envelope.go:114-123 Rotate()` correctly supports per-envelope KEK rotation. SAT is rotation-capable; ASM is not.
- **Why it matters:** BACEN 4.893 Art. 4 expects "periodic review" of cryptographic controls; PCI DSS adjacent buyers expect documented rotation cadence. ASM has no answer.

### G12. Right-to-erasure (LGPD Art. 18 / LFPDPPP ARCO "C") tooling [HIGH]

- **Claim:** Implicit in `frameworks/brazil/lgpd.md` and `frameworks/mexico/lfpdppp.md` data-subject-rights tables.
- **Code reality (ASM):** SCIM `DELETE /Users/{id}` soft-deactivates (per `hailbytes-asm/CLAUDE.md` SCIM behavior section). No dedicated GDPR/LGPD "purge user data" command.
- **Code reality (SAT):** SCIM `scim/scim.go:312-319` similarly locks the account and rewrites the API key to `deprovisioned-<id>` — soft-deactivation, not erasure.
- **Why it matters:** The LGPD Art. 18 VI deletion right and the LFPDPPP Art. 23 (cancelación) right both require **actual deletion within a regulator-set window**. Both products today are non-compliant with strict reading of these articles when the customer needs to operationalize an ARCO request. Customer-side database deletion is the only path; we ship no tooling for it.

### G13. BACEN 4.893 article-number contradiction [HIGH — buyer-visible]

- **Claim location 1:** `latam-compliance-mappings/mappings/hailbytes-asm-to-bacen-4893.md` and `frameworks/brazil/bacen-4893.md` use Art. 4, 6, 7, 11, 12–13, 14, 17.
- **Claim location 2:** `security-policy-templates/mappings/lgpd.md` (BACEN section) and `security-policy-templates/README.md` line 168 table use Art. 4, 5, 6, 7, 11 with Art. 11 attributed to "Incident Reporting."
- **Code reality:** Either set may be technically defensible (different articles touch different aspects of incident management), but a buyer comparing the two HailBytes-published documents will see a contradiction and ask which is canonical. **The official BACEN 4.893 text** places the 72-hour notification clock in Art. 12–13 — `security-policy-templates` is incorrect on Art. 11.
- **Why it matters:** This is the kind of small-but-credibility-damaging detail that drains buyer confidence.

### G14. ANPD Resolution 15/2023 vs 15/2024 contradiction [MEDIUM — buyer-visible]

- **Claim 1:** `latam-compliance-mappings/frameworks/brazil/lgpd.md` line 92: "ANPD Res. CD/ANPD No. 15/2023: 3 business days."
- **Claim 2:** `security-policy-templates/mappings/lgpd.md` line 100: "ANPD Resolution CD/ANPD No. 15/2024 ... within 3 working days."
- **Why it matters:** Same regulation, different years, slightly different wording ("business" vs "working"). One of these is wrong.

---

## Section 3: Implementation Without Documentation

> Security-relevant features that exist in the product code but are **not credited in any compliance mapping or marketing material in `latam-compliance-mappings`**. These are missed marketing opportunities — and missed evidence for buyer questionnaires.

### Supply-chain & build security (ASM)

- **SBOM**: Both SPDX 2.3 (`spdx-json`) and CycloneDX 1.5 generated per image by Syft, attested via Cosign keyless. Evidence: `hailbytes-asm/.github/workflows/build.yml:271-289`.
- **Sigstore/Cosign keyless signing**: `hailbytes-asm/.github/workflows/build.yml:283-292`; verify command published in per-release `SIGNING.md`.
- **Trivy CVE scan with SARIF upload to GitHub Security tab**: `hailbytes-asm/.github/workflows/build.yml:230-249`. Severity floors CRITICAL/HIGH/MEDIUM/LOW.
- **OSV-Scanner nightly cross-validation**: `hailbytes-asm/.github/workflows/security-nightly.yml:43-73`.
- **CodeQL static analysis**: `hailbytes-asm/.github/workflows/codeql-analysis.yml`.
- **Trust Pack release artifact**: SBOM + Trivy + signing metadata + UAT artifacts bundled in single ZIP per release.
- **Dependabot**: `hailbytes-asm/.github/dependabot.yml`.
- **Marketing relevance:** Directly supports BACEN 4.893 Art. 5 "minimum security actions," LGPD Art. 49 "security by design," and ISO 27001 A.8.28 (secure coding) / A.8.30 (outsourced development). **None of this is in the LatAm compliance docs.**

### Application security (ASM)

- **Content Security Policy with per-request nonce**: `hailbytes-asm/web/dashboard/middleware.py:49` `ContentSecurityPolicyMiddleware`.
- **HSTS preload-ready**: `SECURE_HSTS_SECONDS = 31536000`, `SECURE_HSTS_INCLUDE_SUBDOMAINS`, `SECURE_HSTS_PRELOAD` in `web/hailbytes_asm/settings.py`.
- **Clickjacking protection**: `X_FRAME_OPTIONS = 'DENY'`, `XFrameOptionsMiddleware`.
- **CSRF hardening**: `CSRF_TRUSTED_ORIGINS`, `CSRF_COOKIE_SECURE`, `CSRF_COOKIE_SAMESITE='Strict'`.
- **API rate limiting**: DRF throttling in `settings.py` — `anon: 20/minute`, `user: 60/minute`, `scan_initiate: 10/minute`. **README says 200/min for auth — code says 60/min; internal inconsistency.**
- **SHA-256 hashed API keys with expiry + last-used tracking**: `web/api/authentication.py:23`.
- **Dedicated security logger** routing auth events to `~/security.log` with 10 MB × 5 rotation.
- **File-upload hardening**: `FILE_UPLOAD_MAX_MEMORY_SIZE = 10MB`, `FILE_UPLOAD_PERMISSIONS = 0o600`.
- **HMAC-signed inbound cloud-asset webhook with 24h replay dedup**: `web/cloudConnectors/webhook_views.py`.
- **Ubuntu 24.04 hardening script**: `scripts/hailbytes-asm-harden-ubuntu-2404.sh` (SSH hardening, UFW, auditd, Fail2Ban, AppArmor).
- **PgBouncer + Postgres SSL required by default**: `sslmode=require` in `settings.py:139`.
- **LDAP backend with role mapping**: `web/dashboard/auth_backends/ldap.py`.
- **Bug-bounty integration**: `web/bugBounty/` ingests HackerOne + Bugcrowd reports.
- **LLM disclaimer versioning**: `LLM_DISCLAIMER_VERSION = 'v1'` in `settings.py:84` invalidates cached AI-generated content on disclaimer rev — supports LGPD Art. 20 (automated decisions) audit trail.

### Phishing / brand monitoring (ASM)

- **`dnstwist`-based phishing lookalike domain detection**: `web/brandMonitoring/models.py:30 PhishingDomain` + `web/brandMonitoring/tasks.py:18 run_dnstwist`. The LatAm mapping mentions "phishing lookalike detection" for currency exchanges but the implementation is generic to all projects. **This is real, production code we don't credit.**

### Privacy / data minimization (SAT)

- **PII scrubbing**: `hailbytes-sat/piiscrub/piiscrub.go:43-58 Scrub()` redacts emails, phones, IPv4, MACs, credit cards, SSNs, IBANs from user-reported phish bodies with deterministic SHA-256 tokenisation. **This is a direct LGPD Art. 6 (necessity/minimization) control and is uncredited.**
- **Adaptive-decision audit hashes**: `adaptive/adaptive.go:88-90 InputHash`/`OutputHash` — every per-employee training recommendation carries a SHA-256 input/output hash. **Direct LGPD Art. 20 (automated decision review) evidence.**
- **SCIM deprovisioning lock preserving audit trail**: `scim/scim.go:312-319` — DELETE rewrites API key to `deprovisioned-<id>` instead of hard-delete. Maintains LGPD Art. 37 records-of-processing integrity.

### Credential & key management (SAT)

- **Envelope encryption with KEK rotation**: `credstore/envelope.go:31-101` + `Rotate()` at line 114. Per-record DEK encrypted under KEK; `wipe()` zeros sensitive buffers.
- **TOTP secrets encrypted at rest**: `mfa/totp.go:107-117` uses `crypto.EncryptString`.
- **OAuth client secrets encrypted at rest**: `sso/manager.go::SetClientSecret`.

### Operational resilience (SAT)

- **Token-bucket rate limiter**: `middleware/ratelimit/ratelimit.go` with unit tests.
- **HMAC-signed outbound webhooks with exponential backoff**: `webhook/webhook.go:32-49` + `:88-140` (1s → 2s → 4s, 3 retries).
- **Async batched audit writer with sync fall-back on overflow**: `audit/audit.go:236-250`. Events are never dropped — supports LGPD Art. 37 record-of-processing completeness.
- **TLS cert lifecycle**: `acme/` + `customdomain/customdomain.go` Let's Encrypt automation with 30-day renewal window and CNAME allowlist (fail-closed on empty).

### Recommendation

**Add a `docs/uncredited-controls.md`** to `latam-compliance-mappings` that lists each of these features with file paths and the LGPD/BACEN/LFPDPPP/ISO/NIST control IDs they support. Then thread them into the existing per-product mappings so the compliance map matches the audit-pack a buyer would receive.

---

## Section 4: Terminology Drift & Canonical Glossary

### Identified drift

| Concept | Term in latam-compliance-mappings | Term in security-policy-templates | Term in hailbytes-asm | Term in hailbytes-sat | Recommended canonical |
|---|---|---|---|---|---|
| Role-based access | "RBAC", "access control" | "Access Control", "Identity Management" | "RBAC", "django-rolepermissions roles" | "Permission", "PermissionModifySystem" | **RBAC (role-based access control)** |
| Multi-factor auth | "MFA" | "MFA" | "2FA", "TOTP", "two_factor" | "MFA", "TOTP" | **MFA (multi-factor authentication); TOTP is the implementation** |
| Per-record completion log | "Training completion records (per-employee, per-module, timestamped)" | n/a | n/a | `audit_logs` table with `EventCompleted = "completed"`; no dedicated `training_completions` table | **Training completion events (logged in audit_log)** — and add a dedicated table or formally document the audit_log path |
| Incident notification window (LGPD) | "Res. CD/ANPD No. 15/2023, 3 business days" | "Resolution CD/ANPD No. 15/2024, 3 working days" | n/a | n/a | **Resolution CD/ANPD No. 15/2024 (re-issued), 3 business days** — verify and pin one citation |
| BACEN 4.893 incident-reporting article | "Art. 12–13" | "Art. 11" | n/a | n/a | **Art. 12–13** (per the official BCB text); fix `security-policy-templates` |
| ANPD acronym expansion | "ANPD (Autoridade Nacional de Proteção de Dados)" | "ANPD" | n/a | n/a | **ANPD — Autoridade Nacional de Proteção de Dados** (expand on first use in every doc) |
| BCB / BACEN | Uses both "BACEN" and "BCB" interchangeably | "BACEN" only | n/a | n/a | **BCB (Banco Central do Brasil), informally BACEN** — pick one and footnote the other |
| Encrypted data | "Customer KMS keys" | "Encryption" | "Fernet field encryption", "ASM_ENCRYPTION_KEY env var" | "AES-256-GCM", "HAILBYTES_ENCRYPTION_KEY", "envelope encryption" | **Field-level AES-256-GCM (with optional CMK via BYOC Terraform module)** |
| Deployment model | "BYOC (Bring Your Own Cloud)" — used as a single term | "BYOC" not used; "Cloud Security Policy" | "Marketplace VM" / "Full BYOC Terraform" (two tiers) | "Marketplace VM" / "Tier 3 Full BYOC" | **Distinguish: Tier 1 Marketplace VM (default) vs Tier 3 Full BYOC (separate Terraform repo)** |
| Compliance evidence pack | "Audit-ready reports", "evidence package" | "audit evidence" | n/a (report PDF only) | "Evidence Pack" (the actual ZIP export at `GET /api/compliance/evidence`) | **Evidence Pack** (use the SAT product name everywhere) |
| Sensitive personal data | "Sensitive data", "dados pessoais sensíveis" | "Confidential / Restricted" data classification | n/a | "PHI" (M04), "personal data" (M17) | **Sensitive personal data (LGPD/LFPDPPP); Confidential or Restricted (ISO/NIST data classification)** — note they aren't equivalent |
| ARCO rights / data subject rights | "ARCO rights (Mexico)" and "data subject rights (LGPD)" | "Data Subject Rights" | n/a | n/a | **Data subject rights / ARCO (per jurisdiction)** |
| BCB audit access | "BCB audit rights" | "BACEN audit" | n/a | n/a | **BCB audit rights (Art. 14, Resolução 4.893/2021)** |

### Canonical glossary (proposed for inclusion at `latam-compliance-mappings/docs/glossary.md`)

| Term | Definition | Spanish | Portuguese |
|---|---|---|---|
| **RBAC** | Role-Based Access Control — authorization based on assigned roles | Control de acceso basado en roles | Controle de acesso baseado em funções |
| **MFA** | Multi-Factor Authentication. TOTP is the default implementation in both products. | Autenticación multifactor (MFA) | Autenticação multifator (MFA) |
| **TOTP** | Time-based One-Time Password (RFC 6238); HailBytes' MFA implementation | TOTP | TOTP |
| **BYOC** | Bring Your Own Cloud — deployment model where the customer hosts the application. **Tier 1 = Marketplace VM (default; Docker Compose on customer VM). Tier 3 = Full BYOC Terraform (separate `byoc-security-architecture-templates` repo; cloud-native managed services with customer KMS).** | BYOC (Implementación en tu propia nube) | BYOC (Implantação na sua própria nuvem) |
| **CMK** | Customer-Managed Key — encryption key under customer control (AWS KMS CMK or Azure Key Vault key). **Available in Tier 3 BYOC only.** | Clave administrada por el cliente (CMK) | Chave gerenciada pelo cliente (CMK) |
| **SBOM** | Software Bill of Materials (SPDX 2.3 and CycloneDX 1.5 formats supported) | SBOM (Lista de materiales de software) | SBOM (Lista de materiais de software) |
| **Evidence Pack** | ZIP export of training completions, audit logs, certificates, and campaign data via `GET /api/compliance/evidence` | Paquete de evidencia | Pacote de evidências |
| **ANPD** | Autoridade Nacional de Proteção de Dados (Brazil's data protection authority) | ANPD | ANPD |
| **BCB / BACEN** | Banco Central do Brasil (Brazil's central bank, regulator for financial cybersecurity under Res. 4.893/2021) | BCB / BACEN | BCB / BACEN |
| **INAI** | Instituto Nacional de Transparencia, Acceso a la Información y Protección de Datos Personales (Mexico) | INAI | INAI |
| **AAIP** | Agencia de Acceso a la Información Pública (Argentina) | AAIP | AAIP |
| **ARCO** | Acceso, Rectificación, Cancelación, Oposición — Mexican data subject rights | ARCO | ARCO |
| **LGPD** | Lei Geral de Proteção de Dados (Brazil, Law 13.709/2018) | LGPD | LGPD |
| **LFPDPPP** | Ley Federal de Protección de Datos Personales en Posesión de los Particulares (Mexico) | LFPDPPP | LFPDPPP |
| **Encarregado / DPO** | Data Protection Officer (LGPD Art. 41; required for controllers) | DPO | Encarregado de Proteção de Dados |
| **Responsable** | Data controller (LFPDPPP) | Responsable | Controlador (equivalente en LGPD) |
| **Encargado** | Data processor (LFPDPPP) | Encargado | Operador (equivalente en LGPD) |

---

## Section 5: BYOC-Specific Claims — Shared Responsibility Boundary

> **The single most important framing the LatAm compliance docs lack** is a clear delineation of which compliance claims are guaranteed by HailBytes-shipped code and which depend on customer BYOC configuration. Below is the proposed boundary. **Every claim in the LatAm mappings should be classified into one of these three buckets and the docs should say which bucket each claim lives in.**

### Bucket A — Guaranteed by HailBytes code (regardless of deployment tier)

These are properties of the binaries that ship from `hailbytes-asm` and `hailbytes-sat`, true even on the simplest Marketplace VM:

| Claim | Evidence |
|---|---|
| AES-256-GCM field encryption | `hailbytes-asm/web/hailbytes_asm/crypto.py`; `hailbytes-sat/crypto/encryption.go` |
| TLS in transit (admin + phish servers) | `hailbytes-sat/acme/`, `hailbytes-sat/customdomain/customdomain.go`; `hailbytes-asm/docker/proxy/` nginx |
| TOTP MFA | `hailbytes-asm/web/hailbytes_asm/settings.py:154-158`; `hailbytes-sat/mfa/totp.go` |
| OIDC / SAML SSO | `hailbytes-sat/sso/manager.go`, `sso/saml.go`; ASM via Marketplace settings |
| SCIM 2.0 user/group provisioning | `hailbytes-asm/web/api/scim/`; `hailbytes-sat/scim/scim.go` |
| RBAC (3 roles ASM; permission-based SAT) | `hailbytes-asm/web/hailbytes_asm/roles.py`; `hailbytes-sat/middleware/permissions.go` |
| Audit logging | `hailbytes-asm/web/dashboard/models.py` AuditLog; `hailbytes-sat/audit/audit.go` |
| PII scrubbing of user-reported phish | `hailbytes-sat/piiscrub/piiscrub.go:43-58` |
| Phishing simulation campaigns | `hailbytes-sat/mailer/`, `worker/`, `imap/`, `phish/` |
| Continuous attack surface scanning | `hailbytes-asm/web/hailbytes_asm/workflows/scan.py` + 30+ tools |
| Cloud asset discovery (AWS/Azure/GCP/Cloudflare) | `hailbytes-asm/web/cloudConnectors/` |
| Phishing lookalike detection (`dnstwist`) | `hailbytes-asm/web/brandMonitoring/` |
| SBOM (SPDX + CycloneDX), Cosign keyless signatures, Trivy SARIF | `hailbytes-asm/.github/workflows/build.yml` |
| Webhook signatures (HMAC-SHA256) | `hailbytes-sat/webhook/webhook.go:32-49` |
| Training modules (M01–M20) and phishing template library | `hailbytes-sat/content/`, `hailbytes-sat/training_templates/` |
| SCORM 1.2 + xAPI completion export | `hailbytes-sat/scorm/` |
| 5 framework-mapped training modules per `compliance/control-map.json` | `hailbytes-sat/compliance/` |

### Bucket B — Depends on customer BYOC configuration (Tier 3 Full BYOC Terraform)

These require the customer to deploy via the **separate** `byoc-security-architecture-templates` repo and to configure their own AWS / Azure resources. **This repo is out of scope for this audit.**

| Claim | Customer-side action required |
|---|---|
| Customer-managed KMS / Key Vault keys (CMK at rest) | Customer creates KMS key alias; sets RDS / EBS / S3 CMK in their Terraform vars. The Marketplace AMI defaults to no EBS encryption. |
| Cloud-native managed-service architecture (ECS, RDS, Cosmos DB, Key Vault, Front Door) | Customer chooses Tier 3 Terraform stack instead of single-VM Marketplace |
| Data residency in `sa-east-1` / `mx-central-1` / Brazil South / Mexico Central | Customer chooses the region in their Terraform `var.region` / `var.location`. **No code today pins or validates a LatAm region.** |
| KMS automatic key rotation | Customer enables AWS KMS rotation flag on their CMK |
| VPC private subnet isolation | Customer configures network rules in their Terraform |
| HSM-backed key storage | Customer provisions CloudHSM / Azure Dedicated HSM separately |

### Bucket C — Customer-operational responsibility (not a HailBytes feature at all)

These are customer-organizational tasks. HailBytes provides tools and templates; the work is the customer's:

| Claim | What HailBytes provides | What customer must do |
|---|---|---|
| DPO / Encarregado appointment | Documentation template only | Appoint and publish DPO |
| LGPD / LFPDPPP / Argentina Ley 25.326 data-subject-rights process | n/a (no ARCO workflow tool ships) | Build the request-handling workflow |
| ANPD 72-hour notification | Audit logs + SIEM dispatch | Operate the SOC; decide if "relevant incident" threshold met; file ANPD/BCB notice |
| Data Processing Agreement (DPA) with subprocessors | PT-BR template at `templates/data-processing-agreement-pt-br.md` | Customer executes with each subprocessor |
| BCB audit-rights clause in customer contracts | Vendor risk template; product is BYOC so customer is the data controller | Customer ensures all material vendors accept BCB audit rights |
| Annual BACEN Board Report | ASM PDF report templates + data | Customer's CISO / Board secretariat assembles and presents |
| Right-to-erasure operationalization | Audit log records + SCIM soft-deactivate | Customer hard-deletes from DB / S3 / backups within the regulatory window — **no shipped tool today** |

### Recommended doc structure

**Replace `docs/why-byoc-matters-for-latam-compliance.md`'s "Compliance Comparison" table with a three-column table per claim**: *Bucket (A/B/C) · HailBytes commitment · Customer responsibility*. This is the single most defensible doc structure for a buyer-side technical due diligence.

---

## Section 6: 4-Week Remediation Plan

> Effort estimates assume one full-time technical writer or engineer per task. Tags: **[doc-fix]** = documentation only, no code change; **[code-fix]** = product code change required; **[policy-fix]** = security-policy-templates change.

### Week 1 — Stop the bleeding (highest buyer-visibility risk)

| # | Action | Tag | Target repo | Effort | Owner profile |
|---|---|---|---|---|---|
| 1.1 | **Reconcile BACEN 4.893 article numbers.** Pick canonical citation (Art. 12–13 for 72-hour notification, per BCB text). Fix `security-policy-templates/mappings/lgpd.md` and `security-policy-templates/README.md` table. Add footnote in `latam-compliance-mappings/mappings/hailbytes-asm-to-bacen-4893.md` linking to the official BCB resolution PDF. | [doc-fix] / [policy-fix] | security-policy-templates · latam-compliance-mappings | 0.5 day | Compliance writer |
| 1.2 | **Reconcile ANPD Resolution 15/2023 vs 15/2024 citation.** Verify against the ANPD website which is currently in force. Update both repos to a single citation with a hyperlink. | [doc-fix] / [policy-fix] | both doc repos | 0.5 day | Compliance writer |
| 1.3 | **Remove unsupported region claims.** Strip explicit `sa-east-1` / `mx-central-1` / Brazil South / Mexico Central language from `docs/why-byoc-matters-for-latam-compliance.md` and `mappings/*.md` **unless** we can add the regions to `marketplace/packer/variables.pkr.hcl` and publish there. Replace with: "deployable to any AWS or Azure region the customer chooses; LatAm regions are supported by the underlying cloud provider — confirm with your cloud account team." | [doc-fix] | latam-compliance-mappings | 0.5 day | Compliance writer |
| 1.4 | **Add the BYOC tier disclosure** to `docs/why-byoc-matters-for-latam-compliance.md`. Distinguish Tier 1 Marketplace VM (default; not CMK; not cloud-native managed services) from Tier 3 Full BYOC Terraform (CMK; cloud-native; lives in separate repo). | [doc-fix] | latam-compliance-mappings | 1 day | Compliance writer + 1 hr review from SE |

### Week 2 — Truth-up the claims

| # | Action | Tag | Target repo | Effort | Owner profile |
|---|---|---|---|---|---|
| 2.1 | **Fix SAT module-name drift.** Either rename the modules in `content/Mxx/manifest.yaml` to match `compliance/framework-coverage.md` (Phishing Basics / Email Red Flags / Password Security / Social Engineering Awareness / CEO Fraud & BEC), OR update `mappings/hailbytes-sat-to-lgpd.md` and `lfpdppp.md` to use the actual module titles ("Security Foundations for Everyone", "Credential Phishing Defenses", etc.) and reference the framework-coverage map. | [doc-fix] or [code-fix] | hailbytes-sat OR latam-compliance-mappings | 1 day | Eng or compliance |
| 2.2 | **Remove or qualify the "signed PDF certificates" claim** in `mappings/hailbytes-sat-to-lgpd.md`. Replace with: "Completion is recorded as a signed xAPI statement and audit-log entry; PDF certificate generation is on the v1.2200 roadmap" (or whatever the actual roadmap states). | [doc-fix] | latam-compliance-mappings | 0.5 day | Compliance writer |
| 2.3 | **Remove or qualify the "mean time-to-report metric" claim.** Replace with "phishing-reporting events are captured in the IMAP monitor and stored in `audit_logs`; report aggregation is on roadmap." | [doc-fix] | latam-compliance-mappings | 0.5 day | Compliance writer |
| 2.4 | **Correct the role-based-tracks claim.** Replace "admin, developer, HR, finance, healthcare, executive" with the actual set: "developer, finance, healthcare, executive, compliance, all (general staff)." HR is a phishing-template category, not a training-module track. | [doc-fix] | latam-compliance-mappings | 0.5 day | Compliance writer |
| 2.5 | **Add the "insider threat" caveat** mirroring the existing biometric caveat in `mappings/hailbytes-sat-to-lfpdppp.md` Art. 9 row. Add: "An insider-threat-specific module is not in the current built-in library; organizations with elevated insider-risk profiles should supplement with custom content." | [doc-fix] | latam-compliance-mappings | 0.5 day | Compliance writer |
| 2.6 | **Reconcile ASM rate-limit numbers.** README claims `Authenticated: 200/min`; code (`settings.py`) says `user: 60/minute`. Either change the code or the README. | [doc-fix] or [code-fix] | hailbytes-asm | 0.5 day | Eng |
| 2.7 | **Add Argentina (Ley 25.326) product mappings** OR remove Argentina from the README and framework list until mappings exist. | [doc-fix] | latam-compliance-mappings | 1 day if writing mappings; 0.25 day if removing | Compliance writer |

### Week 3 — Bring the product's compliance map up to par

| # | Action | Tag | Target repo | Effort | Owner profile |
|---|---|---|---|---|---|
| 3.1 | **Extend `hailbytes-sat/compliance/control-map.json` to include LGPD, BACEN 4.893, LFPDPPP.** Mirror the existing structure (controls, modules-satisfying, scenarios-satisfying). Make `GET /api/compliance/coverage` return real coverage percentages for the three LatAm frameworks. | [code-fix] | hailbytes-sat | 2 days | Eng (Compliance & Trust team) |
| 3.2 | **Add an analogous `hailbytes-asm/web/hailbytes_asm/compliance_mappings.yaml` extension** so ASM reports can attribute findings to BACEN 4.893 Art. 4/6/7/11/12-13/14/17, LGPD Art. 46, ISO A.8.8, NIST DE.CM. | [code-fix] | hailbytes-asm | 2 days | Eng |
| 3.3 | **Create `latam-compliance-mappings/docs/uncredited-controls.md`** capturing the 25+ uncredited features from Section 3 of this audit, each with file-path and framework-control-ID. | [doc-fix] | latam-compliance-mappings | 1 day | Compliance writer + Eng pairing |
| 3.4 | **Publish `latam-compliance-mappings/docs/glossary.md`** with the canonical glossary from Section 4 of this audit. Link from each existing doc. | [doc-fix] | latam-compliance-mappings | 0.5 day | Compliance writer |

### Week 4 — Closing the gaps that need code

| # | Action | Tag | Target repo | Effort | Owner profile |
|---|---|---|---|---|---|
| 4.1 | **Eliminate the hard-coded fallback encryption key** in `hailbytes-sat/crypto/keymanagement.go:27`. Make `HAILBYTES_ENCRYPTION_KEY` a required env var; refuse to boot if unset (mirror ASM's `ImproperlyConfigured` pattern). | [code-fix] | hailbytes-sat | 0.5 day + migration plan for existing installs | Eng |
| 4.2 | **Add key-rotation tooling to ASM**: switch `web/hailbytes_asm/crypto.py` to `cryptography.fernet.MultiFernet`; add a `rotate_encryption_key` management command. | [code-fix] | hailbytes-asm | 2 days | Eng |
| 4.3 | **Ship a right-to-erasure (LGPD Art. 18 / ARCO "C") admin command** in both products: `manage.py purge_user_data --email <addr> --reason <ARCO|LGPD>` writes an audit-log marker and cascades deletes across primary tables. | [code-fix] | hailbytes-asm + hailbytes-sat | 3 days each | Eng (1 per product) |
| 4.4 | **Add a certificate-expiry alerter** to ASM: cron job in `web/hailbytes_asm/workflows/maintenance.py` that scans TLS audit results for certs expiring in <30 days and fans an alert via the existing SIEM dispatcher. | [code-fix] | hailbytes-asm | 1 day | Eng |
| 4.5 | **Add a per-employee `training_completions` table to SAT** that joins users, modules, scores, signed xAPI statement IDs, and certificate UUIDs. This becomes the canonical evidence object the LatAm-claims mappings rely on. (Currently completion is reconstructable from `audit_logs` filtered by `EventCompleted`, but no dedicated table exists.) | [code-fix] | hailbytes-sat | 3 days incl. migration + API | Eng |
| 4.6 | **Add LatAm region defaults to the Packer build** so AMIs/Compute Galleries are published to `sa-east-1`, `mx-central-1` (when AWS GA), and Azure `brazilsouth` / `mexicocentral`. | [code-fix] | hailbytes-asm + hailbytes-sat (deploy/) | 2 days incl. AWS Marketplace listing update | Eng + Marketplace ops |

### Effort totals

| Week | Doc work (days) | Code work (days) | Total |
|---|---|---|---|
| Week 1 | 2.5 | 0 | 2.5 |
| Week 2 | 3.5 | up to 0.5 | up to 4 |
| Week 3 | 1.5 | 4 | 5.5 |
| Week 4 | 0 | 14.5 | 14.5 |
| **Total** | **7.5** | **up to 19** | **~26.5 days** |

If staffed with **1 compliance writer (full-time) + 1 engineer (full-time)**, this 4-week plan is achievable. The Week 1–2 doc-fixes are the highest-leverage and lowest-risk; they should ship even if the code work in Weeks 3–4 slips.

---

## Appendix A — Files Referenced in This Audit

### `latam-compliance-mappings` (this repo)

- `README.md`
- `mappings/hailbytes-asm-to-bacen-4893.md`
- `mappings/hailbytes-sat-to-lgpd.md`
- `mappings/hailbytes-sat-to-lfpdppp.md`
- `frameworks/brazil/lgpd.md`
- `frameworks/brazil/bacen-4893.md`
- `frameworks/mexico/lfpdppp.md`
- `frameworks/regional/iso-27001-latam-notes.md`
- `frameworks/regional/nist-csf-portuguese.md`
- `docs/why-byoc-matters-for-latam-compliance.md`
- `docs/enterprise-trust-package.md`

### `security-policy-templates`

- `README.md`
- `mappings/lgpd.md`
- `mappings/iso-27001.md`
- `mappings/nist-csf.md`
- All policies under `policies/01-governance/`, `02-access-control/`, `03-communications/`, `04-incident-response/`, `05-infrastructure/`, `06-continuity/`

### `hailbytes-asm`

- `README.md`, `CLAUDE.md`, `AGENTS.md`
- `web/hailbytes_asm/settings.py`
- `web/hailbytes_asm/crypto.py`
- `web/hailbytes_asm/roles.py`
- `web/hailbytes_asm/compliance_mappings.yaml`
- `web/hailbytes_asm/workflows/scan.py`, `scheduling.py`, `maintenance.py`
- `web/dashboard/middleware.py`
- `web/dashboard/signals.py`
- `web/dashboard/dispatch.py`
- `web/dashboard/siem_dispatch.py`, `ticket_dispatch.py`
- `web/dashboard/models.py` (AuditLog, Project, ScanSchedule)
- `web/dashboard/auth_backends/ldap.py`
- `web/dashboard/views_scheduled_report.py`
- `web/startScan/views.py`, `tasks.py`, `models.py`
- `web/startScan/migrations/0073_changeevent.py`
- `web/api/authentication.py`
- `web/api/scim/views.py`, `urls.py`, `serializers.py`
- `web/api/taxii/`
- `web/cloudConnectors/connectors/{aws,azure,gcp,cloudflare}.py`
- `web/cloudConnectors/webhook_views.py`
- `web/brandMonitoring/models.py`, `tasks.py`
- `web/bugBounty/`
- `web/core/secrets/`
- `marketplace/packer/hailbytes-asm.pkr.hcl`, `variables.pkr.hcl`
- `marketplace/aws/AWS_MARKETPLACE_LISTING.md`, `AWS_Technical_Architecture.md`
- `marketplace/azure/AZURE_MARKETPLACE_LISTING.md`, `Technical_Architecture.md`
- `.github/workflows/build.yml`, `security-nightly.yml`, `codeql-analysis.yml`
- `.github/dependabot.yml`
- `docs/HARDENING_GUIDE.md`, `SCHEDULED_SCANS_GUIDE.md`
- `scripts/hailbytes-asm-harden-ubuntu-2404.sh`
- `.env-dist`

### `hailbytes-sat`

- `README.md`, `CLAUDE.md`
- `compliance/control-map.json`, `framework-coverage.md`, `phishing-template-catalog.json`, `pentest-assessment.md`, `soc2-readiness.md`
- `audit/audit.go`, `events.go`, `retention.go`, `query.go`
- `auth/` (sessions / users)
- `mfa/totp.go`
- `middleware/permissions.go`, `mfa.go`, `session.go`, `security.go`, `i18n.go`
- `middleware/ratelimit/ratelimit.go`
- `sso/manager.go`, `saml.go`, `provider.go`
- `scim/scim.go`, `groups.go`
- `crypto/encryption.go`, `keymanagement.go`
- `credstore/envelope.go`
- `piiscrub/piiscrub.go`
- `imap/imap.go`, `monitor.go`
- `mailer/mailer.go`
- `dialer/dialer.go`
- `webhook/webhook.go`
- `customdomain/customdomain.go`
- `acme/`
- `models/certificate.go` (TLS only)
- `scorm/scorm.go`, `driver.go`, `index_html.go`
- `adaptive/adaptive.go`, `spacedrepetition.go`
- `reportdelivery/render.go`, `exec_report.html.tmpl`, channel adapters (`email.go`, `slack.go`, `sms.go`, `teams.go`, `webhook.go`, `http_post.go`)
- `content/M01..M20/manifest.yaml`
- `training_templates/` (phishing-email template library; 19 industry folders)
- `i18n/active.en.toml`, `active.es-419.toml`, `active.pt-BR.toml`, `report.{en,es-419,pt-BR}.toml`
- `deploy/aws/cloudformation-ha.yaml`, `provision-ha.sh`
- `deploy/azure/bicep-ha/`, `provision-ha.sh`
- `aws_marketplace/AWS_MARKETPLACE_LISTING.md`
- `azure_marketplace/AZURE_MARKETPLACE_LISTING.md`

---

## Appendix B — Methodology and Caveats

This audit was conducted by reading every file referenced above in `latam-compliance-mappings` and `security-policy-templates` end-to-end, plus a targeted feature-by-feature audit of `hailbytes-asm` and `hailbytes-sat` against a 25-item and 32-item capability checklist respectively. Line numbers are approximate to the repo refs cited at the top.

**Caveats:**
- Line numbers cited refer to the audited commits and may shift in subsequent revisions.
- "Not found" verdicts are based on repo-wide string searches; a feature with no string evidence might still exist under an unexpected name. Each "Gap" item should be confirmed with the responsible engineer before any external buyer claim is changed.
- The external `byoc-security-architecture-templates` repo is out of scope. Claims that the LatAm docs say live "in the customer's KMS" can only be evaluated as policy promises here, not as code.
- This audit does not validate the legal accuracy of the framework summaries (LGPD article text, BACEN 4.893 article text, etc.). Verification against the official `planalto.gov.br` / `bcb.gov.br` / `diputados.gob.mx` texts is recommended as part of Week 1 remediation.

---

*Audit prepared 2026-05-18. Re-run on commit changes via the `claude/audit-cross-repo-alignment-C1baj` branch.*
