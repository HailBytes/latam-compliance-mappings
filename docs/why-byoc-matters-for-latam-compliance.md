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

## What BYOC Means

In a BYOC deployment, HailBytes software runs in **your own AWS or Azure account**, in a region you choose. Your data never leaves your environment.

```
Traditional SaaS:
  Your Employees → Vendor's SaaS Platform → Vendor's Data Center (may be outside Brazil/Mexico)

HailBytes BYOC:
  Your Employees → HailBytes in YOUR AWS/Azure account → Your Data, Your Region, Your Control
```

You manage:
- The cloud account (your AWS/Azure subscription)
- Encryption keys
- Network access controls
- Data retention and deletion policies
- Audit log access

HailBytes provides:
- The software, deployed via AWS and Azure Marketplace into your account
- Updates and support
- No access to your data

---

## Data Sovereignty by Regulation

### LGPD (Brazil) — Art. 33: International Data Transfers

LGPD Art. 33 restricts transfers of personal data to countries that do not provide an adequate level of protection equivalent to Brazil's, unless a legal mechanism applies (SCCs, explicit consent, BCRs).

| Deployment Model | Transfer Risk | Mechanism Required |
|---|---|---|
| Shared SaaS (data in US/EU) | **High** — personal data of Brazilian employees processed outside Brazil | SCCs or explicit consent required |
| **BYOC in AWS São Paulo / Azure Brazil South** | **None** — data never leaves Brazil | No transfer mechanism needed |

### BACEN 4.893 (Brazil) — Art. 14: Audit Rights and Cloud Controls

BACEN 4.893 requires that cloud service providers used by financial institutions grant BCB audit rights over data — even data stored abroad. In shared SaaS, satisfying this requires your vendor to contractually accept BCB audit access.

| Deployment Model | Audit Access | BCB Compliance |
|---|---|---|
| Shared SaaS | Requires vendor to accept BCB audit clause in contract | Vendor-dependent; possible resistance |
| **BYOC in customer's AWS/Azure** | BCB audits the customer's own cloud account | **Direct — no vendor dependency** |

### LFPDPPP (Mexico) — Art. 37: International Transfers

LFPDPPP Art. 37 requires that international data transfers provide equivalent data protection. Transfers require consent or a recognized legal mechanism.

| Deployment Model | Transfer Risk | INAI Exposure |
|---|---|---|
| Shared SaaS (data outside Mexico) | **High** — employee data transferred to foreign vendor | Must document transfer mechanism; INAI audit risk |
| **BYOC in AWS Mexico City / Azure Mexico Central** | **None** — data remains in Mexico | No transfer; INAI audit straightforward |

---

## Shared SaaS vs. BYOC: Compliance Comparison

| Dimension | Shared SaaS | HailBytes BYOC |
|---|---|---|
| **Data location** | Vendor-controlled (often US or EU) | Customer's chosen region (BR, MX, etc.) |
| **International transfer (LGPD Art. 33)** | Required — needs legal mechanism | Not applicable — no transfer occurs |
| **BCB audit rights (BACEN 4.893 Art. 14)** | Vendor must contractually accept BCB access | Customer controls their own account |
| **INAI audit evidence (LFPDPPP)** | Depends on vendor cooperation | Customer produces evidence directly |
| **Encryption key control** | Vendor manages keys | Customer manages keys |
| **Access logs** | Vendor provides (may be delayed or limited) | Customer has real-time, direct access |
| **Breach notification timeline** | Depends on vendor detecting and notifying** | Customer has direct monitoring and visibility |
| **Third-party risk assessment** | Customer must assess vendor infrastructure | Customer assesses their own cloud account |
| **Contract exit / data portability** | Vendor must export your data | Your data is already in your account |
| **Concentration risk** | Platform availability depends on vendor uptime | Customer controls availability architecture |

---

## Architecture Overview

HailBytes BYOC deploys via AWS and Azure Marketplace into your cloud account:

```
┌─────────────────────────────────────────────┐
│         Customer AWS / Azure Account         │
│                                              │
│  ┌──────────┐   ┌──────────┐  ┌──────────┐ │
│  │ HailBytes│   │  HailBytes│  │  Logs &  │ │
│  │   SAT    │   │    ASM   │  │  Audit   │ │
│  │(training)│   │(scanning)│  │  Trail   │ │
│  └──────────┘   └──────────┘  └──────────┘ │
│                                              │
│  Encryption: Customer KMS keys               │
│  Network: Customer VPC / private subnets     │
│  Access: Customer IAM policies               │
│  Region: Your choice (São Paulo, Mexico, etc)│
└─────────────────────────────────────────────┘
         ↑ No data exits this boundary ↑
```

HailBytes software is distributed via AWS and Azure Marketplace. You subscribe, deploy into your account, and operate independently.

---

## Cloud Marketplace Links

- **AWS Marketplace:** [HailBytes on AWS Marketplace](https://aws.amazon.com/marketplace/seller-profile?id=company_hailbytes)
- **Azure Marketplace:** [HailBytes on Azure Marketplace](https://azuremarketplace.microsoft.com/en-us/marketplace/apps?search=hailbytes)

Marketplace deployment supports:
- **AWS São Paulo (sa-east-1)** — covers Brazilian data residency requirements
- **AWS Mexico City (mx-central-1)** — covers Mexican data residency
- **Azure Brazil South** — Microsoft's Brazil region
- **Azure Mexico Central** — Microsoft's Mexico region

---

## Summary

BYOC is not just an architecture preference — for organizations subject to LGPD, BACEN 4.893, or LFPDPPP, it is the most direct path to data sovereignty compliance. It eliminates international transfer requirements, gives regulators direct audit access, and removes dependency on vendor cooperation for evidence production.

For LatAm enterprise buyers, BYOC is the answer to the question: *"Where does our data go?"* — with HailBytes, the answer is: *"It stays in your account."*

---

*Questions about BYOC deployment in your compliance program: [hailbytes.com/contact](https://hailbytes.com/contact)*
