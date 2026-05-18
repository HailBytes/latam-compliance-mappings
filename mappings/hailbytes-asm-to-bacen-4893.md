# HailBytes ASM → BACEN 4.893 Compliance Mapping

**Product:** HailBytes Attack Surface Management (ASM)
**Framework:** Resolução BCB No. 4.893/2021 (Banco Central do Brasil)
**Applicable to:** Banks, fintechs, payment institutions, credit unions under BCB supervision
**Last Updated:** 2026-05-18

---

## About This Mapping

HailBytes ASM is a continuous attack surface management platform providing external asset discovery, vulnerability identification, and exposure monitoring. This document maps ASM capabilities to the cybersecurity requirements of BACEN Resolution 4.893/2021.

**Deployment model:** HailBytes ASM is deployed in the customer's own AWS or Azure account, either via the published Marketplace VM (Docker Compose on a single hardened Ubuntu VM, defaults `us-east-1` / Azure `centralus` but operator may choose any region the cloud provider supports) or via the Terraform modules in [`hailbytes-terraform-templates`](https://github.com/HailBytes/hailbytes-terraform-templates) (Single / HA / Auto-Scaling-Group topologies with managed RDS, customer-managed KMS CMK encryption, ALB / App Gateway in front). Scan results, asset inventory, and findings are stored in the customer's cloud environment — directly satisfying BCB's requirement that data remain accessible for audit.

**AWS Marketplace:** [HailBytes on AWS Marketplace](https://aws.amazon.com/marketplace/seller-profile?id=company_hailbytes)
**Azure Marketplace:** [HailBytes on Azure Marketplace](https://azuremarketplace.microsoft.com/en-us/marketplace/apps?search=hailbytes)

> **Region pinning:** No HailBytes marketplace image is pinned to a Brazilian
> region. Customers electing a sa-east-1 / brazilsouth deployment specify
> the region in their Terraform variables (`hailbytes-terraform-templates`)
> or at marketplace-launch time.

---

## Compliance Mapping Table

| BACEN 4.893 Article | Requirement | HailBytes ASM Feature | Evidence / Output |
|---|---|---|---|
| **Art. 4** — Cybersecurity Policy | Policy must address procedures for information classification, access control, and vulnerability management | ASM provides continuous data feeding the vulnerability-management procedures and asset-classification decisions referenced by the policy | Asset inventory exports (TAXII / STIX 2.1 at `/api/v1/taxii/2.1/`); vulnerability trend reports; data to inform classification |
| **Art. 4 §1(IV)** — Vulnerability Testing | Cybersecurity policy must include procedures for testing and monitoring for vulnerabilities | ASM performs continuous external vulnerability scanning via 30+ tools (nuclei auto-updating templates, dalfox, naabu/nmap, s3scanner, crlfuzz, tlsx) — identifying open ports, unpatched services, misconfigurations, and exposed credentials | Scheduled scan reports; vulnerability finding history; testing-schedule evidence; `web/startScan/migrations/0073_changeevent.py` ChangeEvent timeline |
| **Art. 6** — Testing and Monitoring | Institutions must implement mechanisms for testing and monitoring systems for vulnerability, including periodic penetration testing | ASM's continuous external monitoring supplements scheduled penetration tests with real-time coverage — catching new exposures between test cycles | Continuous scan data; newly-discovered-asset timeline; ScanHistory rows |
| **Art. 7** — Third-Party Risk | Institutions must assess and monitor cybersecurity risk from third-party service providers and partners | ASM monitors the external footprint of third-party domains and suppliers associated with the institution via per-Project scoping. The cloud-asset webhook (`web/cloudConnectors/webhook_views.py`, HMAC-signed, 24-hour replay protection) ingests vendor-supplied asset inventories. | Third-party domain monitoring reports; new-exposure alerts for monitored vendor domains; vendor-Project per-tenant scoping |
| **Art. 11** — Cloud Service Oversight | Institutions using cloud must assess and monitor cloud service providers' security posture | ASM's cloudConnectors discover and monitor cloud assets across AWS (`web/cloudConnectors/connectors/aws.py`), Azure, GCP, and Cloudflare — including public S3 buckets, misconfigured cloud services, exposed APIs, and `0.0.0.0/0` security-group ingress (`aws.py:131`) | Cloud asset discovery reports; misconfiguration findings; API exposure inventory |
| **Art. 12–13** — Incident Classification & Notification | Relevant cybersecurity incidents must be classified as such (Art. 12) and reported to BCB within 72 hours (Art. 13) | ASM's real-time alerting for critical exposures supports rapid detection. SIEM dispatch (Splunk HEC, Sentinel HMAC, CrowdStrike LogScale, Wiz, Syslog CEF, Jira, ServiceNow) auto-fans every AuditLog event (`web/dashboard/signals.py:35`). Per-asset `found_at` timestamp supports `incidente relevante` window calculation. | Time-to-detect metrics; SIEM event audit trail; AuditLog timeline at `web/dashboard/models.py::AuditLog` |
| **Art. 14** — Third-Party Contracts (Audit Rights) | Contracts with technology service providers must include security standards and audit rights | HailBytes ASM is deployed in the customer's own account — the customer controls the data and meets BCB audit-rights requirements without depending on vendor cooperation | Customer is the data controller; all scan data and reports are in the customer's BCB-auditable account |
| **Art. 17** — Annual Board Report | Annual cybersecurity report to Board must include testing results and vulnerability status | ASM provides board-ready WeasyPrint PDF reports via `web/startScan/views.py::create_report` and scheduled deliveries via `web/dashboard/views_scheduled_report.py`: annual attack-surface trend analysis, total vulnerabilities discovered/remediated, risk posture over time | Annual summary reports; risk-trend dashboards; management-ready exposure metrics |

---

## Fintech and Payment Institution Applicability

Resolution 4.893 applies to all BCB-licensed entities, including:

| Institution Type | BACEN 4.893 Applicability | Key ASM Use Cases |
|---|---|---|
| **Commercial banks** (*bancos comerciais*) | Full scope | External perimeter monitoring, M&A due diligence, branch IP exposure |
| **Payment institutions** (*instituições de pagamento*) | Full scope | API exposure monitoring, payment gateway surface, third-party aggregator risk |
| **Fintechs** (*financeiras / SEP / SCD*) | Full scope | Cloud asset discovery, rapid-growth asset tracking, API security |
| **Credit unions** (*cooperativas de crédito*) | Full scope (simplified for smaller entities) | Domain monitoring, certificate expiry data (alerter on roadmap), basic perimeter coverage |
| **Currency exchanges** (*distribuidoras de câmbio*) | Full scope | Domain monitoring, phishing-lookalike detection via `web/brandMonitoring/` (dnstwist) |

---

## BYOC Data Sovereignty Benefits for BACEN 4.893

| BACEN 4.893 Concern | How BYOC Addresses It |
|---|---|
| **Art. 14** — BCB Audit Rights | All ASM data is in the customer's own AWS/Azure account — BCB can audit it directly without requiring vendor cooperation |
| **Art. 11** — Cloud Data Access | Customer controls the cloud account; no shared tenancy; data is logically and physically isolated |
| **Concentration Risk** | Customer does not depend on a single SaaS vendor for attack-surface visibility — they own the deployed instance |
| **Exit Strategy** | Customer can retain full historical scan data even if they stop using HailBytes, because data is in their PostgreSQL |
| **Customer-Managed Keys (KMS / Key Vault CMK)** | **Tier-3 customer-managed encryption keys are configured via [`hailbytes-terraform-templates`](https://github.com/HailBytes/hailbytes-terraform-templates).** The Marketplace VM ships with Fernet field-encryption using an env-var key; the Terraform modules wire AWS KMS / Azure Key Vault CMK against RDS, EBS, and S3. |

> **Note:** The previously-referenced `byoc-security-architecture-templates`
> repository is deprecated in favour of `hailbytes-terraform-templates`,
> which uses the same published Marketplace AMI in Single / HA / ASG
> topologies rather than cloud-native managed services.

---

## Mapping to BACEN 4.893 Annual Report Sections

The BACEN 4.893 annual board report should include cybersecurity testing and monitoring results. ASM generates data for:

| Report Section | ASM Data Source |
|---|---|
| Vulnerability testing results | Continuous scan findings; critical/high/medium breakdown |
| New risks identified during the year | Timeline of newly discovered assets and first-seen vulnerabilities (`Subdomain.found_at`, `ChangeEvent`) |
| Third-party risk assessment | Vendor-domain monitoring results and new-exposure alerts |
| Cloud security posture | Cloud asset misconfiguration findings (`web/cloudConnectors/`) |
| Improvement plan progress | Year-over-year attack-surface reduction metrics |

---

## Key Takeaways

- BACEN 4.893 Art. 4 and Art. 6 explicitly require vulnerability testing and monitoring — ASM directly satisfies both with continuous, documented coverage.
- The 72-hour incident-notification clock (**Art. 12–13**) makes real-time detection critical; ASM reduces time-to-awareness for new exposures via SIEM dispatch.
- Third-party risk (Art. 7) and cloud oversight (Art. 11) are areas where financial institutions frequently have coverage gaps — ASM addresses both via cloudConnectors and per-Project tenant scoping.
- BYOC deployment means the BCB can audit all ASM data in the customer's own account, satisfying Art. 14 audit-rights requirements without any dependency on HailBytes.
- Customer-managed key custody (KMS / Key Vault CMK) is available via the Terraform Tier-3 deployment in `hailbytes-terraform-templates`, **not** by default on the Marketplace VM — verify your chosen deployment tier with your security architect.
- ASM data feeds every major section of the BACEN 4.893 annual board report.
