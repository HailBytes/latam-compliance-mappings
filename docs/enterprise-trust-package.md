# HailBytes Enterprise Trust Package — LatAm Edition

**For:** Procurement teams, Legal, DPOs, and Compliance Officers evaluating HailBytes for enterprise deployment in Brazil, Mexico, or Argentina

---

## At a Glance

| | |
|---|---|
| **Products** | HailBytes SAT (Security Awareness Training) · HailBytes ASM (Attack Surface Management) |
| **Deployment Model** | BYOC — Bring Your Own Cloud (AWS or Azure, your account, your region) |
| **Data Residency** | Customer-controlled — data never leaves your cloud account |
| **Marketplace** | [AWS Marketplace](https://aws.amazon.com/marketplace/seller-profile?id=company_hailbytes) · [Azure Marketplace](https://azuremarketplace.microsoft.com/en-us/marketplace/apps?search=hailbytes) |
| **Contact** | [hailbytes.com/contact](https://hailbytes.com/contact) |

---

## Architecture Overview

HailBytes operates on a **BYOC (Bring Your Own Cloud)** model. This is the foundational fact for your compliance and procurement review:

- HailBytes software is deployed **into your AWS or Azure subscription** via Marketplace
- All data — training records, simulation results, vulnerability findings, employee information — resides **in your account**
- HailBytes does not operate shared multi-tenant infrastructure for customer data
- You control encryption keys, network access, data retention policies, and audit logs

**What this means for your procurement team:**
- No data processing agreement required for HailBytes to access your data — we don't access it
- BCB/ANPD/INAI audit requests are satisfied from your own cloud account, not through vendor cooperation
- Your security team can audit the deployed infrastructure directly — it's in your account

---

## Compliance Posture

### Frameworks Addressed

| Framework | Jurisdiction | How HailBytes Supports It |
|---|---|---|
| **LGPD** — Lei Geral de Proteção de Dados | Brazil | SAT satisfies Art. 46, 47, 50 security and training requirements; BYOC eliminates Art. 33 transfer concerns |
| **BACEN 4.893** | Brazil (Financial) | ASM satisfies Art. 4/6 vulnerability testing; BYOC satisfies Art. 14 audit rights |
| **LFPDPPP** | Mexico | SAT satisfies Art. 19 administrative security measures; BYOC satisfies Art. 37 transfer requirements |
| **ISO 27001:2022** | Regional | SAT maps to Annex A 6.3 (awareness) and 5.26 (incident response); ASM maps to 8.8 (vulnerability management) |
| **NIST CSF 2.0** | Regional | Products cover all six CSF functions; see [nist-csf-portuguese.md](../frameworks/regional/nist-csf-portuguese.md) |

### Compliance Documentation Available

| Document | Location |
|---|---|
| LGPD control mapping (SAT) | [mappings/hailbytes-sat-to-lgpd.md](../mappings/hailbytes-sat-to-lgpd.md) |
| BACEN 4.893 control mapping (ASM) | [mappings/hailbytes-asm-to-bacen-4893.md](../mappings/hailbytes-asm-to-bacen-4893.md) |
| LFPDPPP control mapping (SAT) | [mappings/hailbytes-sat-to-lfpdppp.md](../mappings/hailbytes-sat-to-lfpdppp.md) |
| Data Processing Agreement template (PT-BR) | [templates/data-processing-agreement-pt-br.md](../templates/data-processing-agreement-pt-br.md) |
| Incident Response Runbook (PT-BR) | [templates/incident-response-runbook-pt-br.md](../templates/incident-response-runbook-pt-br.md) |
| Vendor Risk Assessment (PT-BR) | [templates/vendor-risk-assessment-pt-br.md](../templates/vendor-risk-assessment-pt-br.md) |
| Why BYOC matters for LatAm compliance | [docs/why-byoc-matters-for-latam-compliance.md](why-byoc-matters-for-latam-compliance.md) |

---

## Security and Operational Standards

### Deployment Security

- Marketplace-based deployment: software distributed via AWS and Azure Marketplace into your subscription; deployment configurations are version-controlled and auditable
- Least-privilege IAM: HailBytes components operate with minimum necessary permissions in your account
- Encryption at rest and in transit: all data encrypted using your KMS keys (AWS) or Azure Key Vault keys
- Network isolation: deployed within your VPC with configurable private subnet options
- No outbound data: HailBytes software does not transmit customer data to HailBytes systems

### Marketplace Security

HailBytes products are distributed via AWS and Azure Marketplace, providing:
- Verified publisher status on both platforms
- Software bill of materials (SBOM) available on request
- Container images signed and verifiable
- Regular security updates distributed via marketplace channels

### Update and Patch Management

- Security patches are released on a defined schedule and available through marketplace update mechanisms
- Customers control when updates are applied to their deployment
- Release notes document security-relevant changes

---

## SLA and Support Commitments

| Tier | Response Time (Critical) | Response Time (Standard) | Availability |
|---|---|---|---|
| Enterprise | 4 hours (24/7/365) | 8 business hours | 99.9% uptime SLA for HailBytes-managed components |
| Standard | 4 hours | 24 business hours | Best effort |

*Note: Because HailBytes runs in your cloud account, overall system availability also depends on your chosen cloud region's SLA (AWS and Azure offer 99.99%+ SLAs for compute and storage services).*

Support channels:
- Enterprise support portal with ticketing
- Dedicated customer success contact for enterprise accounts
- Documentation at [hailbytes.com](https://hailbytes.com)

---

## Marketplace Availability and Procurement Paths

### Option 1: AWS Marketplace

Direct procurement through [AWS Marketplace](https://aws.amazon.com/marketplace/seller-profile?id=company_hailbytes):
- Pay via your existing AWS billing (invoice, credit card, AWS Enterprise Discount Program)
- Eligible for AWS Private Offers (custom pricing, negotiated terms)
- Consolidate vendor spend on AWS bill
- Supports Brazilian, Mexican, and Argentine AWS accounts

### Option 2: Azure Marketplace

Direct procurement through [Azure Marketplace](https://azuremarketplace.microsoft.com/en-us/marketplace/apps?search=hailbytes):
- Pay via your existing Azure subscription
- Supports Azure private offers and EA billing
- Works with Azure Brazil South and Azure Mexico Central regions

### Option 3: Direct / Reseller

Contact HailBytes directly for:
- Enterprise negotiated pricing
- Multi-product bundles (SAT + ASM)
- Local reseller partnerships in Brazil and Mexico
- Purchase order / invoice billing

Contact: [hailbytes.com/contact](https://hailbytes.com/contact)

---

## What to Request for Your RFP

If you are including HailBytes in a formal procurement process, request the following from the HailBytes team:

| Document | Purpose |
|---|---|
| BYOC architecture diagram | Technical review of deployment model |
| Penetration test summary (latest) | Third-party security validation |
| SOC 2 Type II report (if available) | Security controls audit |
| Data Processing Agreement (DPA) | For any HailBytes support access scenarios |
| Software Bill of Materials (SBOM) | Component-level security review |
| Disaster Recovery and BCP documentation | Operational resilience review |
| Reference customers in financial services | Peer validation |

Contact [hailbytes.com/contact](https://hailbytes.com/contact) to initiate the enterprise procurement process.

---

## About HailBytes

HailBytes provides cybersecurity products purpose-built for organizations that need enterprise-grade security capabilities with full control over their data. Our BYOC model was designed specifically for regulated industries — financial services, healthcare, government, and critical infrastructure — where data sovereignty is a compliance requirement, not a preference.

Our products are available on AWS and Azure Marketplace, making procurement straightforward for organizations with existing cloud spend commitments.

**Learn more:** [hailbytes.com](https://hailbytes.com)
**Contact:** [hailbytes.com/contact](https://hailbytes.com/contact)
