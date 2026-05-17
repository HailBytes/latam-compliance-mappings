<div align="center">
  <img src="https://hailbytes.com/images/icons/hb_hb_white_horizontal.png" alt="HailBytes" width="300"/>
</div>

<br/>

<div align="center">

# HailBytes LatAm Compliance Mappings

**How HailBytes SAT and ASM map to LatAm compliance frameworks: LGPD, BACEN 4893, LFPDPPP, and more.**

[![License: MPL 2.0](https://img.shields.io/badge/License-MPL_2.0-brightgreen.svg)](https://opensource.org/licenses/MPL-2.0)
[![AWS Marketplace](https://img.shields.io/badge/AWS-Marketplace-orange)](https://aws.amazon.com/marketplace/seller-profile?id=company_hailbytes)
[![Azure Marketplace](https://img.shields.io/badge/Azure-Marketplace-blue)](https://azuremarketplace.microsoft.com/en-us/marketplace/apps?search=hailbytes)

</div>

---

## About This Repository

This repository is HailBytes' public reference for how our **Security Awareness Training (SAT)** and **Attack Surface Management (ASM)** products support compliance with Latin American data protection and cybersecurity regulations.

It is designed for:
- **CISOs and DPOs** building compliance programs in Brazil, Mexico, and Argentina
- **Procurement and legal teams** evaluating HailBytes for enterprise deployment
- **Security professionals** mapping controls to LatAm regulatory frameworks

All content reflects public law text and official regulatory guidance. No customer-specific or proprietary information is included.

---

## Resumo em Português

Este repositório contém mapeamentos de controles dos produtos HailBytes (SAT e ASM) para os principais marcos regulatórios de proteção de dados e cibersegurança da América Latina: LGPD, Resoluções BACEN 4.893 e 4.658, Marco Civil da Internet, e outros. Inclui ainda modelos de documentos em português (Acordo de Processamento de Dados, Runbook de Resposta a Incidentes, Questionário de Risco de Fornecedores) e notas sobre a arquitetura BYOC que mantém os dados dentro do ambiente do cliente.

## Resumen en Español

Este repositorio contiene mapeos de los controles de los productos HailBytes (SAT y ASM) con los principales marcos regulatorios de protección de datos y ciberseguridad en América Latina: LGPD (Brasil), BACEN 4893, LFPDPPP (México), Ley 25.326 (Argentina) y otros. Incluye también una guía sobre la arquitectura BYOC (Bring Your Own Cloud), que garantiza que los datos permanecen en el entorno del cliente, facilitando el cumplimiento de las obligaciones de soberanía de datos en la región.

---

## Quick Links

| Region | Frameworks |
|---|---|
| 🇧🇷 [Brazil](./frameworks/brazil/) | [LGPD](./frameworks/brazil/lgpd.md) · [BACEN 4893](./frameworks/brazil/bacen-4893.md) · [BACEN 4658](./frameworks/brazil/bacen-4658.md) · [Marco Civil](./frameworks/brazil/marco-civil.md) |
| 🇲🇽 [Mexico](./frameworks/mexico/) | [LFPDPPP](./frameworks/mexico/lfpdppp.md) |
| 🇦🇷 [Argentina](./frameworks/argentina/) | [Ley 25.326](./frameworks/argentina/ley-25326.md) |
| 🌎 [Regional](./frameworks/regional/) | [ISO 27001 LatAm](./frameworks/regional/iso-27001-latam-notes.md) · [NIST CSF (Portuguese)](./frameworks/regional/nist-csf-portuguese.md) |
| 🗺️ [Mappings](./mappings/) | [SAT → LGPD](./mappings/hailbytes-sat-to-lgpd.md) · [ASM → BACEN 4893](./mappings/hailbytes-asm-to-bacen-4893.md) · [SAT → LFPDPPP](./mappings/hailbytes-sat-to-lfpdppp.md) |
| 📄 [Templates](./templates/) | [DPA PT-BR](./templates/data-processing-agreement-pt-br.md) · [IR Runbook PT-BR](./templates/incident-response-runbook-pt-br.md) · [Vendor Risk PT-BR](./templates/vendor-risk-assessment-pt-br.md) |
| 📚 [Docs](./docs/) | [Why BYOC Matters](./docs/why-byoc-matters-for-latam-compliance.md) · [Enterprise Trust Package](./docs/enterprise-trust-package.md) |

---

## Frameworks Coverage

| Framework | Country | Regulator | Year | File |
|---|---|---|---|---|
| LGPD — Lei Geral de Proteção de Dados | 🇧🇷 Brazil | ANPD | 2018 | [lgpd.md](./frameworks/brazil/lgpd.md) |
| BACEN Resolution 4.893 | 🇧🇷 Brazil (Financial) | BCB | 2021 | [bacen-4893.md](./frameworks/brazil/bacen-4893.md) |
| BACEN Resolution 4.658 | 🇧🇷 Brazil (Financial) | BCB | 2018 | [bacen-4658.md](./frameworks/brazil/bacen-4658.md) |
| Marco Civil da Internet | 🇧🇷 Brazil | CGI.br / Courts | 2014 | [marco-civil.md](./frameworks/brazil/marco-civil.md) |
| LFPDPPP | 🇲🇽 Mexico | INAI | 2010 | [lfpdppp.md](./frameworks/mexico/lfpdppp.md) |
| Ley 25.326 | 🇦🇷 Argentina | AAIP | 2000 | [ley-25326.md](./frameworks/argentina/ley-25326.md) |
| ISO 27001:2022 LatAm Notes | 🌎 Regional | INMETRO / EMA / OAA | 2022 | [iso-27001-latam-notes.md](./frameworks/regional/iso-27001-latam-notes.md) |
| NIST CSF 2.0 (Portuguese Markets) | 🌎 Regional | NIST | 2024 | [nist-csf-portuguese.md](./frameworks/regional/nist-csf-portuguese.md) |

---

## Product → Framework Mappings

| Product | Framework | Country | File |
|---|---|---|---|
| HailBytes SAT | LGPD | 🇧🇷 Brazil | [hailbytes-sat-to-lgpd.md](./mappings/hailbytes-sat-to-lgpd.md) |
| HailBytes ASM | BACEN 4.893 | 🇧🇷 Brazil (Financial) | [hailbytes-asm-to-bacen-4893.md](./mappings/hailbytes-asm-to-bacen-4893.md) |
| HailBytes SAT | LFPDPPP | 🇲🇽 Mexico | [hailbytes-sat-to-lfpdppp.md](./mappings/hailbytes-sat-to-lfpdppp.md) |

---

## Templates

Ready-to-use document templates in Brazilian Portuguese (PT-BR), aligned with LGPD and BACEN 4.893:

| Template | Description | File |
|---|---|---|
| **Data Processing Agreement** (Acordo de Processamento de Dados) | LGPD-compliant DPA for controller–processor relationships. Includes ANPD notification obligations, data subject rights provisions, and standard clauses. | [data-processing-agreement-pt-br.md](./templates/data-processing-agreement-pt-br.md) |
| **Incident Response Runbook** (Runbook de Resposta a Incidentes) | Operational IR runbook aligned with LGPD Art. 48 and BACEN 4.893 Art. 12–13. Includes P1/P2/P3 classification, 72h notification checklists, and post-mortem template. | [incident-response-runbook-pt-br.md](./templates/incident-response-runbook-pt-br.md) |
| **Vendor Risk Assessment** (Questionário de Avaliação de Risco de Fornecedores) | Vendor due diligence questionnaire aligned with LGPD Art. 37–39 (operator chain) and BACEN 4.893 Art. 14–17 (third-party risk). Includes scoring rubric. | [vendor-risk-assessment-pt-br.md](./templates/vendor-risk-assessment-pt-br.md) |

> All templates are provided for informational purposes. Consult qualified legal counsel before use in your organization.

---

## Why BYOC Matters for LatAm Compliance

HailBytes products are deployed in your own AWS or Azure account — your data never leaves your environment.

For organizations subject to LGPD Art. 33 (international transfer restrictions), BACEN 4.893 Art. 14 (BCB audit rights), or LFPDPPP Art. 37 (cross-border transfer rules), BYOC eliminates the primary data sovereignty risk of traditional SaaS:

→ [Read the full BYOC compliance analysis](./docs/why-byoc-matters-for-latam-compliance.md)

---

## About HailBytes

HailBytes provides BYOC (Bring Your Own Cloud) security awareness training and attack surface management. Deploy in your own AWS or Azure account — your data never leaves your environment.

- **HailBytes SAT:** Phishing simulation and security awareness training
- **HailBytes ASM:** Continuous external attack surface monitoring and vulnerability discovery

**Available on:**
- [AWS Marketplace](https://aws.amazon.com/marketplace/seller-profile?id=company_hailbytes)
- [Azure Marketplace](https://azuremarketplace.microsoft.com/en-us/marketplace/apps?search=hailbytes)

**Enterprise inquiries:** [hailbytes.com/contact](https://hailbytes.com/contact)

---

## License

This documentation is licensed under the [Mozilla Public License 2.0](./LICENSE).

You are free to use, adapt, and share this content with attribution. Modifications must be released under the same license.

---

<div align="center">
  <sub>Maintained by <a href="https://hailbytes.com">HailBytes</a> · <a href="https://hailbytes.com/contact">Contact</a></sub>
</div>
