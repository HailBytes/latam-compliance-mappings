# HailBytes SAT → LGPD Compliance Mapping

**Product:** HailBytes Security Awareness Training (SAT)
**Framework:** Lei Geral de Proteção de Dados — Law 13.709/2018 (Brazil)
**Last Updated:** 2024

---

## About This Mapping

HailBytes SAT is a BYOC (Bring Your Own Cloud) security awareness training and phishing simulation platform. This document maps SAT features to the LGPD articles that a documented security training program helps satisfy.

**Deployment model:** HailBytes SAT is deployed in the customer's own AWS or Azure account. Training records, simulation results, and employee data never leave the customer's cloud environment — directly supporting LGPD's data minimization and security principles.

**AWS Marketplace:** [HailBytes on AWS Marketplace](https://aws.amazon.com/marketplace/seller-profile?id=company_hailbytes)
**Azure Marketplace:** [HailBytes on Azure Marketplace](https://azuremarketplace.microsoft.com/en-us/marketplace/apps?search=hailbytes)

---

## Compliance Mapping Table

| LGPD Article | Requirement | HailBytes SAT Feature | Evidence Generated |
|---|---|---|---|
| **Art. 6 — Principles** | Good faith and accountability in data processing; prevention of harm; non-discrimination | General security culture training; phishing and social engineering awareness; security hygiene content (built-in modules: Phishing Basics, Email Red Flags, Password Security, Social Engineering Awareness, CEO Fraud & BEC) | Training completion records demonstrating organizational commitment to data protection principles |
| **Art. 6, VIII — Prevention** | Adopt measures to prevent occurrence of harm from personal data processing | Phishing simulation campaigns identify employees who need remediation before a real attack occurs | Simulation results showing risk reduction over time; remediation training completion logs |
| **Art. 46 — Security Measures** | Controllers and processors must adopt technical and administrative security measures to protect personal data from unauthorized access | SAT provides the documented administrative/organizational security measure of employee training | Training curriculum documentation; completion certificates; program policy documentation |
| **Art. 47 — Confidentiality** | Persons involved in processing must maintain confidentiality of personal data; controllers must ensure agents/employees comply | SAT modules covering data handling, confidentiality obligations, and insider threat awareness | Training completion certificates (signed PDF); module completion per employee |
| **Art. 48 — Incident Response** | Controller must notify ANPD and affected data subjects of security incidents within reasonable timeframe | Phishing simulation and incident response training modules prepare employees to recognize and report security events promptly | Phishing simulation records showing recognition and reporting behavior; incident recognition training completion; mean time-to-report metrics from simulations |
| **Art. 50 — Privacy Governance** | Controllers may implement governance programs, policies, and procedures demonstrating ongoing compliance with LGPD | SAT is a formal, measurable component of the privacy governance program; demonstrates accountability (*responsabilização*) | Program-level reporting dashboard; trend analysis across campaigns; board-ready compliance reports |
| **Art. 50 §2(d) — Training** | Privacy governance programs should include training programs for employees and administrators | SAT directly fulfils this requirement with role-based training tracks | Curriculum aligned to role (admin, developer, HR, finance); completion rates by department |
| **Art. 37 — Records of Processing** | Controllers must maintain records of processing activities | SAT generates and retains processing activity records for all training and simulation data | Audit logs stored in customer's own cloud account; available for ANPD audit on demand |

---

## BYOC Data Sovereignty Benefits for LGPD

| LGPD Concern | How BYOC Addresses It |
|---|---|
| **Art. 33 — International Transfers** | SAT data (employee training records, simulation results) stays in the customer's Brazilian cloud region — no international transfer occurs |
| **Art. 46 — Security Measures** | Customer controls encryption keys, access policies, and network controls for all SAT data |
| **Art. 37 — Processing Records** | All logs are in the customer's account; ANPD audit requests can be fulfilled directly by the controller |
| **Art. 50 — Accountability** | Customer can demonstrate full visibility and control of the processing environment in any ANPD investigation |

---

## Evidence Package for ANPD Audit

When using HailBytes SAT, the following evidence supports an LGPD compliance defense:

1. **Training policy document** — defines SAT as a required administrative control under Art. 46
2. **Curriculum documentation** — mapped to LGPD requirements (data handling, confidentiality, incident reporting)
3. **Completion records** — per-employee, per-module, timestamped; stored in customer's cloud account
4. **Phishing simulation reports** — baseline click rate, remediation training completion, trend over time
5. **Board/management reporting** — periodic reports demonstrating active governance program under Art. 50
6. **DPO oversight documentation** — *Encarregado* sign-off on training program design and annual review

---

## Key Takeaways

- A documented, regular SAT program is the most direct way to satisfy LGPD Art. 47 (employee confidentiality obligations) and Art. 50 §2(d) (training requirement in governance programs)
- BYOC deployment means your employees' training data never leaves your environment — satisfying Art. 46 security requirements without relying on a shared SaaS vendor's security posture
- Phishing simulation results create measurable risk reduction evidence that directly supports the prevention principle (Art. 6, VIII)
- All evidence is retained in your own cloud account, making ANPD audits straightforward
