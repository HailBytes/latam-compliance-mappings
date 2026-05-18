# HailBytes SAT → LGPD Compliance Mapping

**Product:** HailBytes Security Awareness Training (SAT)
**Framework:** Lei Geral de Proteção de Dados — Law 13.709/2018 (Brazil)
**Last Updated:** 2026-05-18
**Product version mapped:** v1.2200 (20 built-in training modules; signed PDF completion certificates)

---

## About This Mapping

HailBytes SAT is a phishing simulation and security awareness training platform that ships as a hardened virtual machine on AWS and Azure Marketplace. This document maps SAT features to the LGPD articles that a documented security training program helps satisfy.

**Deployment model:** Customers deploy HailBytes SAT into their own AWS or Azure account, either via the published Marketplace VM (Docker Compose) or via the Terraform modules in [`hailbytes-terraform-templates`](https://github.com/HailBytes/hailbytes-terraform-templates) (Single / HA / Auto-Scaling-Group topologies with managed RDS). Training records, simulation results, and signed PDF certificates remain in the customer's cloud environment.

**AWS Marketplace:** [HailBytes on AWS Marketplace](https://aws.amazon.com/marketplace/seller-profile?id=company_hailbytes)
**Azure Marketplace:** [HailBytes on Azure Marketplace](https://azuremarketplace.microsoft.com/en-us/marketplace/apps?search=hailbytes)

> **Shared responsibility:** Compliance claims that depend on customer
> configuration (region choice, customer-managed KMS keys, encryption-key
> custody) are flagged below. See
> [`docs/byoc-shared-responsibility-matrix.md`](../docs/byoc-shared-responsibility-matrix.md)
> for the full A / B / C breakdown.

---

## Compliance Mapping Table

| LGPD Article | Requirement | HailBytes SAT Feature | Evidence Generated |
|---|---|---|---|
| **Art. 6** — Principles | Good faith and accountability in data processing; prevention of harm; non-discrimination | M01 *Security Foundations for Everyone*, M17 *GDPR & Data Protection Basics*. Phishing-template library (`training_templates/`) reinforces good-faith data handling across 19 industry verticals. | Per-employee signed PDF certificates; training-completion audit-log entries (`audit/events.go::EventCompleted`); aggregate completion dashboard |
| **Art. 6, VIII** — Prevention | Adopt measures to prevent harm from personal data processing | Phishing simulation campaigns (M07 *Credential Phishing Defenses*, M08 *MFA Fatigue & Push Bombing*, M11 *Quishing*) identify employees who need remediation before a real attack succeeds | Simulation results with click/submit/report rates; remediation training assignments; trend over time |
| **Art. 11** — Sensitive personal data | Heightened care when processing sensitive data categories (health, biometric, etc.) | M04 *Healthcare & PHI Handling* and M14 *HIPAA Essentials for Non-Clinical Staff* cover health-data scenarios. **Biometric-specific training content is not a current built-in module** — organizations processing biometric data should supplement with custom content. | Role-restricted distribution of M04/M14; per-user signed PDF certificate is the audit-defensible record |
| **Art. 18** — Data subject rights | Operationalize access, rectification, deletion, portability | M17 *GDPR & Data Protection Basics* covers data-subject rights conceptually. Operational ARCO/right-to-erasure tooling is provided via SAT's `DELETE /api/training/certificates/{id}` (revokes; preserves audit trail) plus the planned `purge_training_data` admin command. | M17 completion records; revocation entries in `training_certificates.revoked_*` columns |
| **Art. 37** — Records of Processing | Controllers must maintain records of processing activities | SAT records every training and simulation event in `audit_logs` (single-tenant PostgreSQL inside the customer's cloud account) and generates a per-(user, module, attempt) signed certificate row in `training_certificates`. | Audit log + `training_certificates` table; both included in the Evidence Pack ZIP at `GET /api/compliance/evidence` |
| **Art. 39** — Operator (processor) accountability | When processors are used, they must implement equivalent security | M12 *Vendor Risk & Compromise* trains employees to vet vendor risk and recognize OAuth/SaaS compromise patterns | M12 completion certificate + linked supplier-risk register entries |
| **Art. 46** — Security Measures | Controllers and processors must adopt technical and administrative security measures to protect personal data | SAT itself **is** the documented administrative/organizational measure. Core 5 modules for all employees: M01, M07, M08, M19, M20 plus optional M06, M09, M10, M11, M13, M18 | Per-employee signed PDF certificates; training program policy doc; per-role assignment matrix in `compliance/control-map.json` |
| **Art. 47** — Confidentiality | Persons involved in processing must maintain confidentiality | M01 *Security Foundations* lesson on data-handling and reporting obligations | M01 signed PDF certificate + employee acknowledgement record |
| **Art. 48** — Incident Response | Controller must notify ANPD within the timeframe set by Res. CD/ANPD No. 15/2024 (3 business days for preliminary notification of a high-risk incident) | M18 *Incident Reporting Done Right* (recognition, reporting threshold, evidence preservation). IMAP monitor (`imap/monitor.go`) captures user-forwarded phishing reports for triage; **a computed mean-time-to-report KPI is on the roadmap** — current installs derive it from `audit_logs` filtered by `EventReportedPhish`. | M18 signed PDF certificate + IMAP-report audit entries + IR-runbook evidence |
| **Art. 50** — Privacy Governance | Controllers may implement governance programs demonstrating ongoing LGPD compliance | SAT is a formal, measurable component of the privacy governance program. M16 *SOC 2 for Everyone* and M17 *GDPR & Data Protection Basics* form the governance-curriculum baseline. | Program-level reporting dashboard; board-ready compliance report; signed PDF certificates as evidence artefacts |
| **Art. 50 §2.II.d** — Training | Privacy governance programs *should include training programs for employees and administrators* | SAT directly fulfils this requirement with role-based tracks: **general, developer, finance, healthcare, executive, compliance**. (Administrative-staff and HR-specific tracks are recommended via the `department_assignment_matrix` in `control-map.json` but are not module-level tracks themselves — they reuse general + role-relevant modules.) | Per-track curriculum + per-employee signed PDF certificates by department |

---

## The 20-module Catalog

The full SAT training-module catalog is in [`hailbytes-sat/content/`](https://github.com/HailBytes/hailbytes-sat/tree/main/content) (M01–M20) with framework mappings in [`hailbytes-sat/compliance/framework-coverage.md`](https://github.com/HailBytes/hailbytes-sat/blob/main/compliance/framework-coverage.md). For LGPD-relevant modules:

| Module | Title | Primary LGPD anchor |
|---|---|---|
| M01 | Security Foundations for Everyone | Art. 46, 47, 50 |
| M03 | Finance & Wire-Fraud Defense | Art. 46 |
| M04 | Healthcare & PHI Handling | Art. 11 |
| M06 | Anatomy of a BEC | Art. 46 |
| M07 | Credential Phishing Defenses | Art. 46 |
| M08 | MFA Fatigue & Push Bombing | Art. 46 |
| M09 | Vishing | Art. 46 |
| M10 | Mid-Commute Smishing Trap | Art. 46 |
| M11 | Quishing — The Invisible Link | Art. 46 |
| M12 | Vendor Risk & Compromise | Art. 39 |
| M13 | Deepfake Impersonation | Art. 46 |
| M14 | HIPAA Essentials for Non-Clinical Staff | Art. 11 |
| M17 | GDPR & Data Protection Basics | Art. 6, 18, 46 |
| M18 | Incident Reporting Done Right | Art. 48 |
| M19 | Password Hygiene & Passkeys | Art. 46 |
| M20 | Secure Hybrid Work | Art. 46 |

The remaining four modules (M02 Secure Coding, M05 Executive Whaling, M15 PCI-DSS Awareness, M16 SOC 2 for Everyone) map to LGPD only indirectly via Art. 50 governance.

---

## BYOC Data Sovereignty Benefits for LGPD

| LGPD Concern | How BYOC Addresses It |
|---|---|
| **Art. 33** — International Transfers | The HailBytes SAT VM runs in the customer's chosen AWS or Azure region. Customers operating Brazilian data subjects typically select an in-region deployment via their cloud account. **Region selection is a customer-Terraform / customer-deploy-time variable, not a HailBytes-shipped capability.** No marketplace image is pinned to a specific LatAm region. |
| **Art. 46** — Security Measures | Customer controls encryption keys (CMK via `hailbytes-terraform-templates` Tier-2/Tier-3 modules), access policies, and network controls for all SAT data. The Marketplace VM ships AES-256-GCM with an env-var key (`HAILBYTES_ENCRYPTION_KEY`); the Terraform modules wire AWS KMS / Azure Key Vault CMK. |
| **Art. 37** — Processing Records | `audit_logs` and `training_certificates` are in the customer's PostgreSQL; ANPD audit requests can be fulfilled directly by the controller via the Evidence Pack ZIP. |
| **Art. 50** — Accountability | Customer can demonstrate full visibility and control of the processing environment in any ANPD investigation. Signed PDF certificates are individually verifiable at `/api/training/certificates/{id}/verify` without HailBytes-side involvement. |

See [`docs/byoc-shared-responsibility-matrix.md`](../docs/byoc-shared-responsibility-matrix.md) for the full A / B / C boundary of HailBytes-shipped vs customer-configured vs customer-organizational responsibilities.

---

## Evidence Package for ANPD Audit

When using HailBytes SAT, the following artefacts support an LGPD compliance defense:

1. **Training policy document** — defines SAT as a required administrative control under Art. 46
2. **Curriculum documentation** — the 20-module catalog at `compliance/control-map.json` (schema v2.0), mapped to LGPD Articles 6/11/18/39/46/47/48/50
3. **Per-employee signed PDF certificates** — one per (user, module, attempt) issued from `hailbytes-sat/certs`, HMAC-SHA256 signed, verifiable at `/api/training/certificates/{id}/verify` *without authentication* so ANPD inspectors can confirm authenticity directly. Stored in the `training_certificates` table.
4. **Completion records (CSV)** — `training-completions.csv` in the Evidence Pack; per-employee, per-module, timestamped
5. **Phishing simulation reports** — baseline click rate, remediation training completion, trend over time
6. **Board / management reporting** — periodic reports demonstrating active governance program under Art. 50
7. **DPO (Encarregado) oversight documentation** — sign-off on training program design and annual review
8. **xAPI completion statements** — IEEE 9274.1.1 JSON, one per completion event (for customers using an external LRS)

All artefacts are produced by `GET /api/compliance/evidence?framework=LGPD&from=...&to=...` as a single ZIP.

---

## Key Takeaways

- A documented, regular SAT program is the most direct way to satisfy LGPD Art. 47 (employee confidentiality obligations) and Art. 50 §2.II.d (training requirement in governance programs).
- The signed PDF completion certificate is the canonical evidence artefact for ANPD audits — one per (user, module, attempt), HMAC-SHA256 signed, externally verifiable.
- BYOC deployment means your employees' training data never leaves your cloud account; HailBytes ships the binary, you choose the region and the encryption-key custody model.
- Phishing simulation results create measurable risk-reduction evidence that supports the prevention principle (Art. 6, VIII).
- The 20-module catalog spans all 10 LGPD Chapter VII obligations either directly or indirectly. The 4 LATAM-frameworks-coverage table at `compliance/framework-coverage.md` is the auditor-facing summary.
