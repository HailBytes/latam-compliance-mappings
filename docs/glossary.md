# Canonical Glossary

Resolves terminology drift across `latam-compliance-mappings`,
`security-policy-templates`, `hailbytes-asm`, and `hailbytes-sat`. Buyer-side
teams (especially in Brazil, Mexico, and Argentina) ask about the same
concepts under different names; this document picks the canonical English
term and provides Portuguese and Spanish equivalents.

## Concepts

| Canonical (English) | Portuguese (PT-BR) | Spanish (Latin America) | Notes |
|---|---|---|---|
| **RBAC** — Role-Based Access Control | Controle de acesso baseado em funções (RBAC) | Control de acceso basado en roles (RBAC) | The implementation in ASM is `django-rolepermissions` (`web/hailbytes_asm/roles.py`); in SAT it's `middleware/permissions.go`. "Access control" and "authorization policy" are synonyms; prefer **RBAC**. |
| **MFA** — Multi-Factor Authentication | Autenticação multifator (MFA) | Autenticación multifactor (MFA) | The implementation is TOTP (RFC 6238). "2FA" is colloquially equivalent but technically a subset; prefer **MFA**. |
| **TOTP** — Time-based One-Time Password (RFC 6238) | TOTP | TOTP | The HailBytes MFA implementation. Used as the second factor; backup codes available. |
| **BYOC** — Bring Your Own Cloud | BYOC (Implantação na sua própria nuvem) | BYOC (Implementación en tu propia nube) | Deployment model. **Tier 1 = Marketplace VM** (default; Docker Compose on customer VM). **Tier 2 / Tier 3 = Terraform** from `hailbytes-terraform-templates` (HA / Auto-Scaling-Group with managed RDS and CMK encryption). |
| **CMK** — Customer-Managed Key | Chave gerenciada pelo cliente (CMK) | Clave administrada por el cliente (CMK) | Available in BYOC Tier 2 / Tier 3 only. AWS KMS CMK or Azure Key Vault key. |
| **SBOM** — Software Bill of Materials | SBOM (Lista de materiais de software) | SBOM (Lista de materiales de software) | SAT and ASM publish SPDX 2.3 and CycloneDX 1.5 SBOMs with each release; Cosign-attested. |
| **Completion Certificate** | Certificado de conclusão de treinamento (PDF assinado) | Certificado de finalización de capacitación (PDF firmado) | The canonical evidence artefact for SAT. Per-user, per-module, HMAC-SHA256 signed; verifiable at `/api/training/certificates/{id}/verify`. |
| **Evidence Pack** | Pacote de evidências | Paquete de evidencia | ZIP archive produced by `GET /api/compliance/evidence`; contains training-completions CSV, signed certificates, audit log, campaign data, xAPI statements. |
| **ANPD** — Autoridade Nacional de Proteção de Dados | ANPD | ANPD | Brazil's data-protection regulator. Always expand on first use. |
| **BCB / BACEN** — Banco Central do Brasil | BCB (informalmente BACEN) | BCB (informalmente BACEN) | Brazil's central bank, financial-cybersecurity regulator for Resolução 4.893/2021. Use **BCB** in formal docs, **BACEN** is accepted informally. |
| **INAI** — Instituto Nacional de Transparencia, Acceso a la Información y Protección de Datos Personales | INAI | INAI | Mexico's data-protection regulator. |
| **AAIP** — Agencia de Acceso a la Información Pública | AAIP | AAIP | Argentina's data-protection regulator. |
| **LGPD** — Lei Geral de Proteção de Dados (Brazil, Law 13.709/2018) | LGPD | LGPD | Brazil's general data protection law, modeled on the GDPR. |
| **LFPDPPP** — Ley Federal de Protección de Datos Personales en Posesión de los Particulares (Mexico) | LFPDPPP | LFPDPPP | Mexico's private-sector data protection law. |
| **Ley 25.326** — Personal Data Protection Law (Argentina) | Lei 25.326 | Ley 25.326 | Argentina's national data protection law; AAIP guidance cites ISO 27001 A.6.3 as a benchmark. |
| **Encarregado / DPO** — Data Protection Officer | Encarregado de Proteção de Dados | Oficial de Protección de Datos (DPO) | LGPD Art. 41. Required for controllers; identity must be publicly available. |
| **Responsable** — Data controller (Mexico) | Controlador (equivalente em LGPD) | Responsable | LFPDPPP term. "Controller" / "controlador" are equivalent in EU/Brazilian usage. |
| **Encargado** — Data processor (Mexico) | Operador (equivalente em LGPD) | Encargado | LFPDPPP term. |
| **ARCO Rights** | Direitos ARCO (Acesso, Retificação, Cancelamento, Oposição) | Derechos ARCO (Acceso, Rectificación, Cancelación, Oposición) | Mexican data-subject rights under LFPDPPP. Roughly equivalent to LGPD Art. 18 rights. |
| **Aviso de Privacidad / Aviso de Privacidade** | Aviso de Privacidade | Aviso de Privacidad | Privacy notice. Required under LFPDPPP Art. 15–17. |
| **Sensitive personal data** | Dados pessoais sensíveis (LGPD Art. 11) | Datos personales sensibles (LFPDPPP Art. 9) | Includes health, biometric, religious, political, sexual-preference categories. **Not** equivalent to ISO/NIST data-classification levels like "Confidential" or "Restricted" — those are organisational classifications; sensitive personal data is a regulatory category. |
| **BCB Audit Rights** | Direitos de auditoria do BCB | Derechos de auditoría del BCB | BACEN 4.893 Art. 14 requirement that the BCB has unimpeded audit access to financial-institution data even if stored abroad. |
| **Incident notification window (Brazil, LGPD)** | Prazo de notificação de incidente | Plazo de notificación de incidente | **3 business days** (*3 dias úteis*) for the preliminary communication to ANPD per Res. CD/ANPD No. 15/2024. |
| **Incident notification window (Brazil, BACEN)** | Prazo de notificação ao BCB | Plazo de notificación al BCB | **72 hours** for relevant cybersecurity incidents per BACEN 4.893 Art. 12–13. |
| **HailBytes Terraform Templates** | Modelos Terraform da HailBytes | Plantillas Terraform de HailBytes | `hailbytes-terraform-templates` — the canonical home for Single / HA / ASG deployments wrapping the marketplace AMIs. The deprecated `byoc-security-architecture-templates` repo is being retired. |
| **Marketplace VM** | Máquina virtual do Marketplace | Máquina virtual de Marketplace | The hardened Ubuntu AMI / Compute Gallery image published on AWS and Azure Marketplace. The default deployment unit; all higher tiers wrap it. |

## Cross-repo synonyms to deprecate

The following older terms appear in product docs and should be migrated to the canonical entries above:

| Old term | Canonical replacement |
|---|---|
| "access control policy" | "RBAC" |
| "authorization policy" | "RBAC" |
| "2FA" (in marketing-facing copy; OK in code/internal docs) | "MFA" |
| "BYOC architecture" (without tier qualifier) | "BYOC — Tier 1 Marketplace VM" or "BYOC — Tier 2/3 Terraform" |
| `byoc-security-architecture-templates` (the repo) | `hailbytes-terraform-templates` |
| "BACEN Art. 11 — Incident Reporting" | "BACEN Art. 12–13 — Incident Classification & Notification" |
| "ANPD Res. 15/2023" | "ANPD Res. CD/ANPD No. 15/2024" (re-issue; supersedes 15/2023) |
| "training records" (when implying a separate table) | "training-completion records (signed PDF certificates + audit-log events)" |
