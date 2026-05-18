# Why BYOC Architecture Matters for LatAm Compliance

**Audience:** CISOs, DPOs, General Counsel, and Compliance Officers evaluating security technology for Brazilian, Mexican, or Argentine operations

---

## The Core Problem: Data Sovereignty in Shared SaaS

Most security software is delivered as multi-tenant SaaS. Your employee training records, phishing simulation results, vulnerability findings, and attack surface data live on a vendor's shared infrastructure — potentially in data centers outside your jurisdiction.

For organizations subject to LGPD, BACEN 4.893, or LFPDPPP, this creates regulatory exposure:

- **International data transfers** require legal mechanisms (adequate country, SCCs, explicit consent)
- **Audit rights** must extend to wherever your data is processed — your vendor's infrastructure
- **Incident notification timelines** assume you know what happened quickly — shared SaaS obscures visibility
- **Third-party risk** regulations require you to assess and control your vendors' security posture

**BYOC (Bring Your Own Cloud) eliminates these problems by design.**

---

## What BYOC Means in HailBytes' Model

In a HailBytes BYOC deployment, software runs in **your own AWS or Azure account**, in a region **you choose at deploy time**. Your data never leaves your environment.

```
Traditional SaaS:
  Your Employees → Vendor's SaaS Platform → Vendor's Data Center (may be outside Brazil/Mexico)

HailBytes BYOC:
  Your Employees → HailBytes in YOUR AWS/Azure account → Your Data, Your Region, Your Control
```

### Deployment tiers — shared-responsibility boundary

HailBytes ships two product tiers, each with a different customer-responsibility profile. **This distinction matters for your compliance program** because not every claim below holds at every tier; the table makes the boundary explicit.

| Tier | What it is | Customer-managed KMS? | Suitable for |
|---|---|---|---|
| **Tier 1: Marketplace VM** (default) | One hardened Ubuntu VM, Docker Compose, local PostgreSQL. Launch from AWS or Azure Marketplace in ~10–15 min. AES-256-GCM field encryption using an env-var key. | Optional via EBS / disk-level KMS at the cloud-account layer; product does not call KMS SDK directly. | Pilots, < 5,000 users / targets, lab and evaluation |
| **Tier 2: Terraform Single / HA** | Same published marketplace AMI in IaC. Single VM or HA pair across availability zones behind an ALB / App Gateway. Managed RDS (PostgreSQL) Multi-AZ. | **Yes** — AWS KMS CMK / Azure Key Vault CMK on RDS, EBS, S3. Wired in [`hailbytes-terraform-templates`](https://github.com/HailBytes/hailbytes-terraform-templates). | Production, 5,000–50,000 users / targets, regulated industries |
| **Tier 3: Terraform Auto-Scaling-Group / VMSS** | Same published marketplace AMI in an Auto Scaling Group / VM Scale Set fronted by an LB. Managed RDS / Azure SQL with read replicas, CloudFront / Front Door, SES / Azure Communication Services. | **Yes** — CMK across the full stack; key rotation enabled at the cloud-account layer. | Enterprise, 50,000+ users / targets, multi-region failover, BACEN-regulated financial institutions |

> **Important:** Tiers 2 and 3 use the **same published Marketplace AMI** as Tier 1; the Terraform modules in `hailbytes-terraform-templates` simply wrap that AMI in additional topology. There is no separate "BYOC build." The previous `byoc-security-architecture-templates` repository (which used cloud-native managed services as standalone container deployments) is **deprecated** in favor of the marketplace-AMI-based templates.

### What you control vs what HailBytes provides

**You manage:**
- The cloud account (your AWS / Azure subscription)
- The deployment **region** (operator choice at Marketplace launch or Terraform `var.region`)
- Encryption keys (Tier 2 / Tier 3 customer-managed CMK; Tier 1 env-var key under EBS encryption controlled by your cloud account)
- Network access controls (security groups, NSGs)
- Data retention and deletion policies
- Audit-log access (`audit_logs` table in your PostgreSQL)
- The choice of in-region deployment (AWS or Azure regions inside Brazil, Mexico, etc.)

**HailBytes provides:**
- The software, distributed via AWS and Azure Marketplace into your account
- Terraform modules wrapping the same AMI in Single / HA / ASG topologies
- Updates and signed-image releases (Sigstore keyless, SBOM SPDX + CycloneDX)
- Support
- No access to your data

For the full A / B / C bucket breakdown of which compliance claims are guaranteed by HailBytes code vs which depend on your Terraform / deployment configuration, see [`docs/byoc-shared-responsibility-matrix.md`](./byoc-shared-responsibility-matrix.md).

---

## Data Sovereignty by Regulation

### LGPD (Brazil) — Art. 33: International Data Transfers

LGPD Art. 33 restricts transfers of personal data to countries that do not provide an adequate level of protection equivalent to Brazil's, unless a legal mechanism applies (SCCs, explicit consent, BCRs).

| Deployment Model | Transfer Risk | Mechanism Required |
|---|---|---|
| Shared SaaS (data in US/EU) | **High** — personal data of Brazilian employees processed outside Brazil | SCCs or explicit consent required |
| **HailBytes BYOC in a Brazilian AWS or Azure region** | **None** — data never leaves Brazil. The customer selects the region at deploy time. | No transfer mechanism needed |

### BACEN 4.893 (Brazil) — Art. 14: Audit Rights and Cloud Controls

BACEN 4.893 requires that cloud service providers used by financial institutions grant BCB audit rights over data — even data stored abroad. In shared SaaS, satisfying this requires your vendor to contractually accept BCB audit access.

| Deployment Model | Audit Access | BCB Compliance |
|---|---|---|
| Shared SaaS | Requires vendor to accept BCB audit clause in contract | Vendor-dependent; possible resistance |
| **HailBytes BYOC** in customer's AWS/Azure | BCB audits the customer's own cloud account | **Direct — no vendor dependency** |

### LFPDPPP (Mexico) — Art. 37: International Transfers

LFPDPPP Art. 37 requires that international data transfers provide equivalent data protection. Transfers require consent or a recognized legal mechanism.

| Deployment Model | Transfer Risk | INAI Exposure |
|---|---|---|
| Shared SaaS (data outside Mexico) | **High** — employee data transferred to foreign vendor | Must document transfer mechanism; INAI audit risk |
| **HailBytes BYOC in a Mexican AWS or Azure region** | **None** — data remains in Mexico (customer-chosen region) | No transfer; INAI audit straightforward |

---

## Shared SaaS vs. BYOC: Compliance Comparison

| Dimension | Shared SaaS | HailBytes BYOC |
|---|---|---|
| **Data location** | Vendor-controlled (often US or EU) | Customer's chosen AWS/Azure region |
| **International transfer (LGPD Art. 33)** | Required — needs legal mechanism | Not applicable when customer chooses in-region deployment |
| **BCB audit rights (BACEN 4.893 Art. 14)** | Vendor must contractually accept BCB access | Customer controls their own account |
| **INAI audit evidence (LFPDPPP)** | Depends on vendor cooperation | Customer produces evidence directly |
| **Encryption key control** | Vendor manages keys | Tier 2 / Tier 3: customer KMS CMK; Tier 1: env-var key with EBS-level encryption controlled by customer cloud account |
| **Access logs** | Vendor provides (may be delayed or limited) | Customer has real-time, direct access |
| **Breach notification timeline** | Depends on vendor detecting and notifying | Customer has direct monitoring and visibility |
| **Third-party risk assessment** | Customer must assess vendor infrastructure | Customer assesses their own cloud account |
| **Contract exit / data portability** | Vendor must export your data | Your data is already in your account |
| **Concentration risk** | Platform availability depends on vendor uptime | Customer controls availability architecture |

---

## Architecture Overview

HailBytes BYOC deploys via AWS and Azure Marketplace into your cloud account, optionally wrapped by the Terraform modules in `hailbytes-terraform-templates`:

```
┌───────────────────────────────────────────
│         Customer AWS / Azure Account         │
│                                              │
│  ┌──────────┐   ┌──────────┐  ┌──────────┐ │
│  │ HailBytes│   │ HailBytes│  │ Postgres │ │
│  │   SAT    │   │    ASM   │  │ +Audit   │ │
│  │  (VM)    │   │  (VM)    │  │  Logs    │ │
│  └──────────┘   └──────────┘  └──────────┘ │
│                                              │
│  Tier 1: local Postgres, env-var key         │
│  Tier 2: RDS Multi-AZ + KMS CMK              │
│  Tier 3: RDS + replicas + CMK + Front Door   │
│                                              │
│  Region: your choice (customer-selected)     │
└─────────────────────────────────────────────┘
         ↑ No data exits this boundary ↑
```

HailBytes software is distributed via AWS and Azure Marketplace. You subscribe, deploy into your account (directly or via the Terraform modules), and operate independently.

---

## Cloud Marketplace Links and Region Selection

- **AWS Marketplace:** [HailBytes on AWS Marketplace](https://aws.amazon.com/marketplace/seller-profile?id=company_hailbytes)
- **Azure Marketplace:** [HailBytes on Azure Marketplace](https://azuremarketplace.microsoft.com/en-us/marketplace/apps?search=hailbytes)
- **Terraform modules:** [`hailbytes-terraform-templates`](https://github.com/HailBytes/hailbytes-terraform-templates) (Single / HA / ASG)

### Region selection is a customer choice

HailBytes does **not** pin its marketplace images to specific Brazilian or Mexican regions. At launch / deploy time you choose the region you want from any region your AWS or Azure account team supports. For LatAm data-sovereignty compliance, common choices include:

| Cloud | Common LatAm region selections |
|---|---|
| **AWS** | `sa-east-1` (São Paulo). AWS Mexico (Central) regions are subject to AWS's own GA timeline — check current availability with your AWS account team. |
| **Azure** | `brazilsouth`, `brazilsoutheast`. Mexico Central is available; confirm SKU availability for the marketplace image with your Microsoft account team. |

If your account team confirms availability and quota in the region you need, the same marketplace AMI / Compute Gallery image deploys there. If you need region availability validation as part of your procurement process, contact [hailbytes.com/contact](https://hailbytes.com/contact).

---

## Summary

BYOC is not just an architecture preference — for organizations subject to LGPD, BACEN 4.893, or LFPDPPP, it is the most direct path to data sovereignty compliance. It eliminates international transfer requirements when the customer selects an in-region deployment, gives regulators direct audit access, and removes dependency on vendor cooperation for evidence production.

For LatAm enterprise buyers, BYOC is the answer to the question: *"Where does our data go?"* — with HailBytes, the answer is: *"It stays in your account, in the region you chose."*

See [`docs/byoc-shared-responsibility-matrix.md`](./byoc-shared-responsibility-matrix.md) for the explicit per-claim shared-responsibility boundary your procurement team will ask for.

---

*Questions about BYOC deployment in your compliance program: [hailbytes.com/contact](https://hailbytes.com/contact)*
