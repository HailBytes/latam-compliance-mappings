# HailBytes SAT → LFPDPPP Compliance Mapping

**Product:** HailBytes Security Awareness Training (SAT)
**Framework:** Ley Federal de Protección de Datos Personales en Posesión de los Particulares (LFPDPPP) — Mexico
**Last Updated:** 2026-05-18
**Product version mapped:** v1.2200 (20 built-in training modules; signed PDF completion certificates)

---

## About This Mapping

HailBytes SAT is a phishing simulation and security awareness training platform delivered as a hardened virtual machine on AWS and Azure Marketplace. This document maps SAT features to the LFPDPPP articles that a documented security training program helps satisfy.

**Deployment model:** Customers deploy HailBytes SAT into their own AWS or Azure account, either via the published Marketplace VM (Docker Compose on a customer-managed VM) or via the Terraform modules in [`hailbytes-terraform-templates`](https://github.com/HailBytes/hailbytes-terraform-templates) (Single / HA / Auto-Scaling-Group topologies with managed RDS and customer-managed KMS keys). Training records and simulation data remain in the customer's cloud environment.

**AWS Marketplace:** [HailBytes on AWS Marketplace](https://aws.amazon.com/marketplace/seller-profile?id=company_hailbytes)
**Azure Marketplace:** [HailBytes on Azure Marketplace](https://azuremarketplace.microsoft.com/en-us/marketplace/apps?search=hailbytes)

> **Shared responsibility:** Region selection, KMS key custody, and ARCO
> deletion timelines depend on customer configuration. See
> [`docs/byoc-shared-responsibility-matrix.md`](../docs/byoc-shared-responsibility-matrix.md).

---

## Compliance Mapping Table

| LFPDPPP Article | Requirement | HailBytes SAT Feature | Evidence Generated |
|---|---|---|---|
| **Art. 8** — Consent | Processing requires consent; employees and agents must understand what data is processed and why | M17 *GDPR & Data Protection Basics* (covers lawful-basis and consent concepts) | M17 signed PDF certificate per employee |
| **Art. 9** — Sensitive Data (*datos sensibles*) | Sensitive data (health, biometric, religious, political, sexual preference, etc.) requires express written consent and heightened care; employees handling such data require specific training | M04 *Healthcare & PHI Handling* and M14 *HIPAA Essentials for Non-Clinical Staff* cover health-data scenarios in depth. **Biometric-specific training content is not a current built-in module**; organizations processing biometric data should supplement with custom content. **Insider-threat awareness as a standalone module is also not in the M01–M20 catalog**; insider-risk concepts surface inside M01 / M12 / M14 / M17 but no dedicated insider-threat module ships today. | Role-restricted distribution of M04/M14; per-user signed PDF certificate; documented gap notes in the audit packet for the two areas not directly covered |
| **Art. 19** — Security Measures | *Responsables* must implement security measures (*medidas de seguridad*) — administrative, technical, and physical — proportional to data sensitivity | SAT itself fulfils the **administrative** security measure dimension. The 20-module catalog spans phishing, BEC, vishing, smishing, quishing, MFA, supply chain, deepfake, incident reporting, password hygiene, and hybrid work. Recognized as a qualifying control under LFPDPPP Reglamento Art. 48(II). | Training policy document; curriculum aligned to data sensitivity (general vs role-restricted tracks); per-employee signed PDF certificates |
| **Art. 21** — Security Breach | *Responsables* must take immediate action when a security incident occurs; employees must be trained to recognize and report incidents | M18 *Incident Reporting Done Right*. IMAP monitor (`hailbytes-sat/imap/monitor.go`) captures user-forwarded phishing reports for SOC triage; a computed mean-time-to-report KPI is on the v1.2300 roadmap and is currently derivable from `audit_logs`. | M18 signed PDF certificate; phishing-simulation click-rate trend; IMAP-report audit entries |
| **Art. 36** — Third-Party Transfers | When transferring data to *encargados* (processors), *responsables* must ensure processors implement equivalent security measures | M12 *Vendor Risk & Compromise* (recognising vendor-compromise patterns, OAuth abuse, SaaS supply-chain risk). SAT vendor (HailBytes) is itself deployed in the customer's own account — customer is the processor of their own training data; no third-party transfer to HailBytes occurs. | M12 signed PDF certificate; BYOC architecture documentation demonstrating no outbound transfer |
| **Art. 37** — International Transfers | International transfers require consent or a legal basis; recipient must provide equivalent protection | BYOC deployment keeps all training data in the customer's chosen AWS or Azure region. **Region selection is a customer Terraform variable / Marketplace deploy choice, not a HailBytes-shipped capability.** Customers deploying to AWS or Azure regions inside Mexico avoid the Art. 37 international-transfer issue entirely. | Cloud deployment documentation showing the customer's chosen region; no HailBytes-side data egress |
| **Art. 48** — INAI Enforcement | INAI may audit compliance; organizations must demonstrate security measures implemented | SAT generates an audit trail showing security training as an active, ongoing organizational control — the per-employee signed PDF certificate is the canonical record. Evidence Pack ZIP delivers the full set on one API call. | Audit-ready reports: training policy, completion rates, phishing simulation results, signed certificates, trend analysis; all stored in the customer's own account |
| **Reglamento Art. 48(II)** — Administrative Measures | Security program must include administrative measures; training is explicitly cited in INAI guidance | SAT is the administrative security measure; the Reglamento and INAI enforcement guidance explicitly recognize employee training as a qualifying control | Training program documentation; per-employee signed PDF certificate batch |

---

## The 20-module Catalog — LFPDPPP-relevant modules

| Module | Title | Primary LFPDPPP anchor |
|---|---|---|
| M01 | Security Foundations for Everyone | Art. 19; Reglamento Art. 48(II) |
| M04 | Healthcare & PHI Handling | Art. 9 |
| M12 | Vendor Risk & Compromise | Art. 36 |
| M14 | HIPAA Essentials for Non-Clinical Staff | Art. 9 |
| M17 | GDPR & Data Protection Basics | Art. 8, 19 |
| M18 | Incident Reporting Done Right | Art. 21 |

The remaining 14 modules support LFPDPPP only indirectly via the Art. 19 administrative-measure obligation (i.e. *any* documented training reinforces the measure).

---

## Mexico-Specific Context

### INAI Enforcement Priorities

INAI has consistently prioritized enforcement in sectors that handle large volumes of personal data with direct consumer impact:

| INAI Priority Sector | SAT Relevance |
|---|---|
| **Financial services** (*servicios financieros*) | Phishing is the primary attack vector for financial credential theft; M03, M06, M07, M15 directly reduce this risk |
| **Healthcare** (*salud*) | Sensitive health data requires heightened employee training; M04 + M14 provide healthcare-tier role-based content |
| **Telecommunications** | Large employee bases with customer data access; SAT scales via SCIM-driven role assignment |
| **HR and recruitment** (*recursos humanos*) | HR personnel process sensitive data; recommended modules per `department_assignment_matrix` |
| **Retail and e-commerce** | Customer payment data; M15 PCI-DSS Awareness + retail phishing-template library |

### INAI Audit Evidence Requirements

When INAI investigates a *responsable*, investigators look for evidence of:
1. An *Aviso de Privacidad* — not SAT-related, but the training program should include a module on how to present and explain privacy notices (M17 covers this conceptually)
2. Security measures implemented — SAT records are direct evidence; the **signed PDF completion certificate** is the artefact INAI auditors will be handed
3. Employee awareness of data protection obligations — SAT completion records prove this per-employee, per-module
4. Response to prior incidents — simulation reports + M18 completion records show proactive breach prevention

---

## BYOC Data Sovereignty Benefits for LFPDPPP

| LFPDPPP Concern | How BYOC Addresses It |
|---|---|
| **Art. 37** — International Transfers | Customer chooses an in-region AWS or Azure deployment, eliminating cross-border transfer concerns. Region pinning is a customer Terraform variable. |
| **Art. 19** — Security Measures | Customer controls encryption (CMK via `hailbytes-terraform-templates` Tier-2/Tier-3), access, and network controls for all SAT data |
| **Art. 36** — Processor Accountability | Customer is the processor of their own training data; HailBytes does not process customer employee data |
| **INAI Audit Response** | All evidence (signed certificates, completion CSVs, audit logs) is in the customer's account and producible to INAI directly without HailBytes involvement |

---

## Key Takeaways

- LFPDPPP Art. 19 requires administrative security measures — SAT is the clearest, most documentable way to satisfy this for the human/people dimension.
- INAI specifically recognizes employee training as an administrative security measure under the Reglamento; SAT provides this with a verifiable per-employee signed PDF audit trail.
- Sensitive data training (Art. 9) requires demonstrable extra care — SAT's role-restricted distribution of M04/M14 lets you prove differentiated treatment for employees handling sensitive categories. Organizations processing biometric data and high-insider-risk environments should supplement with custom training content for those specific gaps.
- BYOC keeps all training data in the customer's chosen region, eliminating the international transfer burden (Art. 37) entirely — provided the customer selects an in-region deployment.
- SAT's phishing simulation capability directly reduces the Art. 21 breach risk INAI enforcement actions focus on.
