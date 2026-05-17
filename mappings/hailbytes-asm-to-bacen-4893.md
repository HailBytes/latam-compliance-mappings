# HailBytes ASM → BACEN 4.893 Compliance Mapping

**Product:** HailBytes Attack Surface Management (ASM)
**Framework:** Resolução BCB No. 4.893/2021 (Banco Central do Brasil)
**Applicable to:** Banks, fintechs, payment institutions, credit unions under BCB supervision
**Last Updated:** 2024

---

## About This Mapping

HailBytes ASM is a BYOC (Bring Your Own Cloud) attack surface management platform providing continuous external asset discovery, vulnerability identification, and exposure monitoring. This document maps ASM capabilities to the cybersecurity requirements of BACEN Resolution 4.893/2021.

**Deployment model:** HailBytes ASM is deployed in the customer's own AWS or Azure account. Scan results, asset inventory, and findings data are stored in the customer's cloud environment — directly satisfying BCB's requirement that data remain accessible for audit.

**AWS Marketplace:** [HailBytes on AWS Marketplace](https://aws.amazon.com/marketplace/seller-profile?id=company_hailbytes)
**Azure Marketplace:** [HailBytes on Azure Marketplace](https://azuremarketplace.microsoft.com/en-us/marketplace/apps?search=hailbytes)

---

## Compliance Mapping Table

| BACEN 4.893 Article | Requirement | HailBytes ASM Feature | Evidence / Output |
|---|---|---|---|
| **Art. 4 — Cybersecurity Policy** | Policy must address procedures for information classification, access control, and vulnerability management | ASM provides continuous data to feed vulnerability management procedures and asset classification | Asset inventory exports; vulnerability trend reports; data to inform classification decisions |
| **Art. 4 §1(IV) — Vulnerability Testing** | Cybersecurity policy must include procedures for testing and monitoring for vulnerabilities | ASM performs continuous external vulnerability scanning — identifying open ports, unpatched services, misconfigurations, and exposed credentials | Scheduled scan reports; vulnerability finding history; remediation tracking; testing schedule evidence |
| **Art. 6 — Testing and Monitoring** | Institutions must implement mechanisms for testing and monitoring systems for vulnerability, including penetration testing on schedule | ASM's continuous external monitoring supplements scheduled penetration tests with real-time coverage — catching new exposures between test cycles | Continuous scan data showing discovery of new assets and vulnerabilities between pen test dates |
| **Art. 7 — Third-Party Risk** | Institutions must assess and monitor cybersecurity risk from third-party service providers and partners | ASM monitors the external footprint of third-party domains and suppliers associated with the institution — identifying risk from vendors' exposed attack surface | Third-party domain monitoring reports; supplier risk scores; timeline of new exposures from vendor domains |
| **Art. 11 — Cloud Service Oversight** | Institutions using cloud must assess and monitor cloud service providers' security posture | ASM discovers and monitors cloud assets (public-facing S3 buckets, misconfigured cloud services, exposed APIs) across the institution's cloud footprint | Cloud asset discovery reports; misconfiguration findings; API exposure inventory |
| **Art. 12–13 — Incident Notification** | Relevant cybersecurity incidents must be reported to BCB within 72 hours | ASM's real-time alerting for critical exposures supports rapid detection — reducing the window between exposure creation and institutional awareness | Time-to-detect metrics; alert history; evidence that monitoring was active at time of incident |
| **Art. 14 — Third-Party Contracts** | Contracts with technology service providers must include security standards and audit rights | HailBytes ASM is deployed in the customer's own account (BYOC) — the customer controls the data, meets BCB audit rights requirements without depending on vendor cooperation | Customer is the data controller; all scan data and reports are in the customer's BCB-auditable account |
| **Art. 17 — Annual Board Report** | Annual cybersecurity report to Board must include testing results and vulnerability status | ASM provides board-ready reporting: annual attack surface trend analysis, total vulnerabilities discovered/remediated, risk posture over time | Annual summary reports; risk trend dashboards; management-ready exposure metrics |

---

## Fintech and Payment Institution Applicability

Resolution 4.893 applies to all BCB-licensed entities, including:

| Institution Type | BACEN 4.893 Applicability | Key ASM Use Cases |
|---|---|---|
| **Commercial banks** (*bancos comerciais*) | Full scope | External perimeter monitoring, M&A due diligence, branch IP exposure |
| **Payment institutions** (*instituições de pagamento*) | Full scope | API exposure monitoring, payment gateway surface, third-party aggregator risk |
| **Fintechs** (*financeiras / SEP / SCD*) | Full scope | Cloud asset discovery, rapid growth asset tracking, API security |
| **Credit unions** (*cooperativas de crédito*) | Full scope (simplified for smaller entities) | Domain monitoring, certificate expiry, basic perimeter coverage |
| **Currency exchanges** (*distribuidoras de câmbio*) | Full scope | Domain monitoring, phishing lookalike detection |

---

## BYOC Data Sovereignty Benefits for BACEN 4.893

| BACEN 4.893 Concern | How BYOC Addresses It |
|---|---|
| **Art. 14 — BCB Audit Rights** | All ASM data is in the customer's own AWS/Azure account — BCB can audit it directly without requiring vendor cooperation |
| **Art. 16 — Cloud Data Access** | Customer controls the cloud account; no shared tenancy; data is logically and physically isolated |
| **Concentration Risk** | Customer does not depend on a single SaaS vendor for attack surface visibility — they own the platform |
| **Exit Strategy** | Customer can retain full historical scan data even if they stop using HailBytes, because data is in their account |

---

## Mapping to BACEN 4.893 Annual Report Sections

The BACEN 4.893 annual board report should include cybersecurity testing and monitoring results. ASM generates data for:

| Report Section | ASM Data Source |
|---|---|
| Vulnerability testing results | Continuous scan findings; remediation rates; critical/high/medium breakdown |
| New risks identified during the year | Timeline of newly discovered assets and first-seen vulnerabilities |
| Third-party risk assessment | Supplier domain monitoring results |
| Cloud security posture | Cloud asset misconfiguration findings |
| Improvement plan progress | Year-over-year attack surface reduction metrics |

---

## Key Takeaways

- BACEN 4.893 Art. 4 and Art. 6 explicitly require vulnerability testing and monitoring — ASM directly satisfies both with continuous, documented coverage
- The 72-hour incident notification clock (Art. 12) makes real-time detection critical; ASM reduces time-to-awareness for new exposures
- Third-party risk (Art. 7) and cloud oversight (Art. 11) are areas where financial institutions frequently have coverage gaps — ASM addresses both
- BYOC deployment means the BCB can audit all ASM data in the customer's own account, satisfying Art. 14 audit rights requirements without any dependency on HailBytes
- ASM data feeds every major section of the BACEN 4.893 annual board report
