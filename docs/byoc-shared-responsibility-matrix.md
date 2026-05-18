# BYOC Shared Responsibility Matrix

**Audience:** Procurement, Legal, DPO / Encarregado, CISO, Compliance Officers
**Purpose:** Define exactly which compliance claims are guaranteed by HailBytes-shipped code, which depend on customer BYOC configuration, and which are customer-organizational responsibilities. Buyer-side technical due diligence asks this question; this document is the answer.

---

## How to use this document

For every claim in the LatAm compliance mappings, the responsibility falls into one of three buckets:

- **Bucket A — Shipped by HailBytes.** Property of the binary you launch from Marketplace; true at every tier including the default single-VM image.
- **Bucket B — Customer-Terraform / configuration dependent.** Available via [`hailbytes-terraform-templates`](https://github.com/HailBytes/hailbytes-terraform-templates) Tier 2 (HA) or Tier 3 (ASG/VMSS); requires customer to choose that topology, supply KMS keys, pick a region, etc.
- **Bucket C — Customer-organizational.** Not a HailBytes feature; the customer must perform the activity (appoint a DPO, execute a DPA, file ANPD notifications).

When a buyer asks "is X guaranteed by HailBytes?" the table answers in one of these three ways.

---

## Bucket A — Guaranteed by HailBytes code

Properties of the SAT and ASM binaries; true regardless of which deployment tier the customer picks.

| Claim | Evidence (file path in product repo) |
|---|---|
| AES-256-GCM field encryption | `hailbytes-asm/web/hailbytes_asm/crypto.py`, `hailbytes-sat/crypto/encryption.go` |
| TLS in transit (admin + phish servers) | `hailbytes-sat/acme/`, `hailbytes-sat/customdomain/customdomain.go`, `hailbytes-asm/docker/proxy/` |
| TOTP MFA | `hailbytes-asm/web/hailbytes_asm/settings.py` (`django_otp` + `two_factor`), `hailbytes-sat/mfa/totp.go` |
| OIDC / SAML SSO | `hailbytes-sat/sso/` (OIDC + SAML), ASM via Marketplace settings + LDAP |
| SCIM 2.0 user/group provisioning | `hailbytes-asm/web/api/scim/`, `hailbytes-sat/scim/scim.go` |
| RBAC | `hailbytes-asm/web/hailbytes_asm/roles.py`, `hailbytes-sat/middleware/permissions.go` |
| Audit logging | `hailbytes-asm/web/dashboard/models.py::AuditLog` (21 action types), `hailbytes-sat/audit/audit.go` |
| PII scrubbing of user-reported phish | `hailbytes-sat/piiscrub/piiscrub.go:43-58` |
| Phishing simulation campaigns | `hailbytes-sat/mailer/`, `worker/`, `imap/`, `phish/` |
| Continuous attack surface scanning (30+ tools) | `hailbytes-asm/web/hailbytes_asm/workflows/scan.py` |
| Cloud asset discovery (AWS / Azure / GCP / Cloudflare) | `hailbytes-asm/web/cloudConnectors/` |
| Phishing lookalike detection (`dnstwist`) | `hailbytes-asm/web/brandMonitoring/` |
| SBOM (SPDX + CycloneDX), Cosign keyless signatures, Trivy SARIF | `hailbytes-asm/.github/workflows/build.yml` |
| Webhook signatures (HMAC-SHA256) | `hailbytes-sat/webhook/webhook.go:32-49` |
| 20 training modules (M01–M20) + 19-industry phishing template library | `hailbytes-sat/content/`, `hailbytes-sat/training_templates/` |
| SCORM 1.2 + xAPI completion export | `hailbytes-sat/scorm/` |
| **Per-user, per-module signed PDF completion certificates** | `hailbytes-sat/certs/certificate.go`, `models/training_certificate.go`, `controllers/api/training_certificate.go` |
| Framework-mapped compliance coverage (13 frameworks incl. LGPD, BACEN, LFPDPPP) | `hailbytes-sat/compliance/control-map.json`, `framework-coverage.md` |
| i18n: English, `es-419`, `pt-BR` | `hailbytes-sat/i18n/` |
| Adaptive-training audit hashes (LGPD Art. 20 automated-decision evidence) | `hailbytes-sat/adaptive/adaptive.go:88-90` |
| Envelope-encrypted credential store + KEK rotation | `hailbytes-sat/credstore/envelope.go` |

---

## Bucket B — Depends on customer BYOC configuration

Properties of the **Terraform Tier 2 or Tier 3** deployment via [`hailbytes-terraform-templates`](https://github.com/HailBytes/hailbytes-terraform-templates), or of customer-side cloud-account configuration on a Marketplace VM. **Required customer action is shown.**

| Claim | Tier required | Customer action required |
|---|---|---|
| Customer-managed KMS / Key Vault keys (CMK on RDS, EBS, S3) | Tier 2 or Tier 3 | Choose the Terraform template; provide a KMS key alias; pass it to the module's `kms_key_arn` / `key_vault_secret_uri` variable |
| Cloud-native managed-service architecture (RDS Multi-AZ / Azure Database flexible server, ALB / App Gateway, Front Door / CloudFront, SES / Azure Communication Services) | Tier 2 or Tier 3 | Choose the relevant Terraform topology and apply |
| **Data residency in a specific LatAm region** (e.g. `sa-east-1`, `brazilsouth`, Mexico Central) | Any tier | Set the Terraform `region` variable, or pick the region at Marketplace-launch time. **HailBytes does not pin images to specific LatAm regions.** Verify region quota and SKU availability with your cloud account team. |
| Automatic key rotation | Tier 2 or Tier 3 | Enable AWS KMS automatic rotation flag on the CMK, or Azure Key Vault rotation policy |
| VPC private subnet isolation, NAT Gateway egress, security-group hardening | Tier 2 or Tier 3 | Configure the Terraform network variables |
| HSM-backed key storage | Tier 2 or Tier 3 | Provision CloudHSM / Azure Dedicated HSM separately; configure the KMS key store to use it |
| Auto-scaling with read-replica RDS | Tier 3 | Pick the ASG / VMSS template |

---

## Bucket C — Customer-organizational responsibility

Not a HailBytes feature at all. HailBytes provides templates and tools; the work is the customer's.

| Claim | What HailBytes provides | What customer must do |
|---|---|---|
| DPO / Encarregado appointment (LGPD Art. 41) | Documentation template only | Appoint and publish DPO contact details |
| ARCO requests (LFPDPPP) / Data subject rights (LGPD Art. 17–22) | M17 *GDPR & Data Protection Basics* (trains staff in the concepts); cert revocation flow; planned `purge_training_data` admin command | Build and operate the request-intake workflow; meet the 20-business-day response window |
| ANPD 72-hour / 3-business-day breach notification | M18 training module; audit logs; SIEM dispatch | Operate the SOC; classify incidents per Res. CD/ANPD No. 15/2024; file ANPD notice |
| BCB 72-hour notification (BACEN 4.893 Art. 12–13) | Same | Same, plus file with BCB |
| Data Processing Agreement (DPA) with sub-processors | PT-BR template at `templates/data-processing-agreement-pt-br.md` | Execute DPA with each material vendor |
| BCB audit-rights clause in vendor contracts | Vendor-risk-assessment template; product is BYOC so customer is the data controller | Customer ensures all material vendors accept BCB audit rights |
| Annual BACEN Board Report (Art. 17) | ASM PDF report templates + per-period data | CISO / Board secretariat assembles, signs, and presents |
| Right-to-erasure operationalization | Audit-log records; SCIM soft-deactivate; signed cert revocation; planned hard-delete admin command | Hard-delete user data from primary tables, backups, and any analytic warehouses within the regulatory window |
| Customer ID and identity proofing for ANPD audit response | Audit logs; signed PDF certificates; Evidence Pack ZIP | Customer's compliance team presents the artefacts to ANPD / INAI / AAIP / BCB inspectors |
| Choice of cloud region | Marketplace AMI available globally; Terraform modules accept any region | Customer selects the region at deploy time |

---

## Worked example: "Is HailBytes compliant with LGPD Art. 46?"

LGPD Art. 46 mandates technical and administrative security measures. To answer the buyer's question with precision:

| Sub-claim | Bucket | Status |
|---|---|---|
| Encryption at rest (AES-256-GCM) for training data | **A** | Shipped at every tier |
| Encryption at rest with **customer-managed keys** | **B** | Tier 2 / Tier 3 customer Terraform; customer supplies KMS key |
| TLS in transit (TLS 1.2+ minimum) | **A** | Shipped |
| RBAC and audit logging | **A** | Shipped |
| MFA enforcement | **A** | Shipped (TOTP); customer can additionally enforce SSO MFA via Entra ID / Okta |
| Network isolation (private subnets, no public DB) | **B** | Tier 2 / Tier 3 Terraform |
| Annual review of security measures | **C** | Customer security team |
| Employee training on security obligations | **A** + **C** | 20-module catalog + signed PDF certs are shipped; assigning employees, tracking completion, presenting to ANPD is customer responsibility |

The answer to the buyer is: **"Most of LGPD Art. 46 is in Bucket A. Customer-managed encryption keys and private-subnet network isolation are in Bucket B and ship via `hailbytes-terraform-templates` Tier 2 / Tier 3. Annual review and training-program ownership are in Bucket C."**

This precision is the point of the matrix.
