# HailBytes SAT → LFPDPPP Compliance Mapping

**Product:** HailBytes Security Awareness Training (SAT)
**Framework:** Ley Federal de Protección de Datos Personales en Posesión de los Particulares (LFPDPPP) — Mexico
**Last Updated:** 2024

---

## About This Mapping

HailBytes SAT is a BYOC (Bring Your Own Cloud) security awareness training and phishing simulation platform. This document maps SAT features to the LFPDPPP articles that a documented security training program helps satisfy.

**Deployment model:** HailBytes SAT is deployed in the customer's own AWS or Azure account. Training records and simulation data never leave the customer's cloud environment — directly supporting LFPDPPP's security measure and cross-border transfer requirements.

**AWS Marketplace:** [HailBytes on AWS Marketplace](https://aws.amazon.com/marketplace/seller-profile?id=company_hailbytes)
**Azure Marketplace:** [HailBytes on Azure Marketplace](https://azuremarketplace.microsoft.com/en-us/marketplace/apps?search=hailbytes)

---

## Compliance Mapping Table

| LFPDPPP Article | Requirement | HailBytes SAT Feature | Evidence Generated |
|---|---|---|---|
| **Art. 8 — Consent** | Processing requires consent; employees and agents must understand what data is processed and why | SAT training modules covering employee data rights and organizational data processing practices | Training completion records; consent mechanism documentation |
| **Art. 9 — Sensitive Data** | Sensitive data (*datos sensibles*) requires express written consent and heightened care; employees handling such data require specific training | SAT provides dedicated training tracks for employees handling sensitive data categories (health, biometric, financial) | Role-based training completion records for sensitive data handlers; separate curriculum evidence |
| **Art. 19 — Security Measures** | *Responsables* must implement security measures (*medidas de seguridad*) — administrative, technical, and physical — proportional to data sensitivity | SAT fulfils the **administrative security measure** requirement: documented, regular employee training is a recognized organizational control under LFPDPPP Reglamento Art. 48 | Training policy document; curriculum aligned to data sensitivity; completion records by role and data type |
| **Art. 21 — Security Breach** | *Responsables* must take immediate action when a security incident occurs; employees must be trained to recognize and report incidents | Phishing simulation trains employees to recognize attacks before they succeed; incident reporting modules train the escalation path | Simulation click-rate reduction over time; incident reporting procedure training completion; mean time-to-report metrics |
| **Art. 36 — Third-Party Transfers** | When transferring data to *encargados* (processors), *responsables* must ensure processors implement equivalent security measures | SAT vendor (HailBytes) is deployed in the customer's own account — customer is the processor of their own training data; no third-party data transfer occurs with BYOC | BYOC architecture documentation demonstrating no outbound data transfer to HailBytes |
| **Art. 37 — International Transfers** | International transfers require consent or legal basis; recipient must provide equivalent protection | BYOC deployment keeps all training data in Mexico (AWS Mexico or Azure Mexico regions) — no international transfer occurs | Cloud deployment documentation showing data residency in Mexican cloud region |
| **Art. 48 — INAI Enforcement** | INAI may audit compliance; organizations must be able to demonstrate security measures implemented | SAT generates an audit trail showing security training as an active, ongoing organizational control | Audit-ready reports: training policy, completion rates, phishing simulation results, trend analysis; all stored in customer's own account |
| **Reglamento Art. 48(II) — Administrative Measures** | Security program must include administrative measures; training is explicitly cited in INAI guidance | SAT is the administrative security measure; the Reglamento and INAI enforcement guidance explicitly recognize employee training as a qualifying control | Training program documentation that directly maps to Reglamento Art. 48(II) |

---

## Mexico-Specific Context

### INAI Enforcement Priorities

INAI has consistently prioritized enforcement in sectors that handle large volumes of personal data with direct consumer impact:

| INAI Priority Sector | SAT Relevance |
|---|---|
| **Financial services** (*servicios financieros*) | Phishing is the primary attack vector for financial credential theft; SAT directly reduces this risk |
| **Healthcare** (*salud*) | Sensitive health data requires heightened employee training; SAT provides dedicated sensitive data modules |
| **Telecommunications** | Large employee bases with customer data access; SAT provides scalable training delivery |
| **HR and recruitment** (*recursos humanos*) | HR personnel process sensitive data categories; role-based SAT tracks address this |
| **Retail and e-commerce** | Customer payment data; SAT covers PCI-adjacent awareness content |

### INAI Audit Evidence Requirements

When INAI investigates a *responsable*, investigators look for evidence of:
1. An *Aviso de Privacidad* — not SAT-related, but the training program should include a module on how to present and explain privacy notices
2. Security measures implemented — SAT records are direct evidence
3. Employee awareness of data protection obligations — SAT completion records prove this
4. Response to prior incidents — simulation reports show proactive breach prevention

---

## BYOC Data Sovereignty Benefits for LFPDPPP

| LFPDPPP Concern | How BYOC Addresses It |
|---|---|
| **Art. 37 — International Transfers** | Training data stays in Mexico; no transfer mechanism (consent, SCCs) required |
| **Art. 19 — Security Measures** | Customer controls encryption, access, and network controls for all SAT data |
| **Art. 36 — Processor Accountability** | Customer is the processor of their own data; HailBytes does not process customer employee data |
| **INAI Audit Response** | All evidence is in customer's account; can be produced to INAI directly without HailBytes involvement |

---

## Key Takeaways

- LFPDPPP Art. 19 requires administrative security measures — SAT is the clearest, most documentable way to satisfy this for the human/people dimension
- INAI specifically recognizes employee training as an administrative security measure under the Reglamento; SAT provides this with an audit trail
- Sensitive data training (Art. 9) requires demonstrable extra care — SAT's role-based tracks let you prove differentiated treatment for employees handling sensitive categories
- BYOC keeps all training data in Mexico, eliminating the international transfer burden (Art. 37) entirely
- SAT's phishing simulation capability directly reduces the Art. 21 breach risk INAI enforcement actions focus on
