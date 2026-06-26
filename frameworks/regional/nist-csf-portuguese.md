# NIST CSF in Portuguese-Speaking Markets

> **Scope:** NIST Cybersecurity Framework (CSF) 2.0 adoption in Brazil and Portuguese-speaking markets, community translation resources, and mapping to LGPD compliance requirements.

---

## Overview

The NIST Cybersecurity Framework (CSF), originally published in 2014 and updated to version 2.0 in February 2024, has become the most widely adopted voluntary cybersecurity framework globally. In Brazil — Latin America's largest economy and the region's leading technology market — the NIST CSF is referenced by enterprise security programs, government digital strategy documents, and increasingly by financial regulators as a complementary control baseline alongside BACEN-specific requirements.

---

## NIST CSF 2.0 — Framework Structure

CSF 2.0 introduces six core Functions (up from five in CSF 1.1, adding **Govern**):

| Function | Abbreviation | Description |
|---|---|---|
| **Govern** | GV | Organizational context, risk management strategy, cybersecurity policy |
| **Identify** | ID | Asset management, risk assessment, improvement |
| **Protect** | PR | Identity management, data security, platform security, resilience |
| **Detect** | DE | Continuous monitoring, adverse event analysis |
| **Respond** | RS | Incident management, analysis, mitigation, reporting |
| **Recover** | RC | Incident recovery, communication |

---

## Brazilian Government References to NIST CSF

### Federal Government Digital Transformation

The Brazilian government's **Estratégia Nacional de Segurança Cibernética (E-Ciber)** — the National Cybersecurity Strategy — and the associated **Decreto No. 10.748/2021** establishing the National Cybersecurity Program (ProgreSS) reference international frameworks including NIST CSF as models for organizational cybersecurity programs.

### ANPD and Security Measures

While ANPD has not formally endorsed a single technical framework, ANPD guidance on security measures (*medidas de segurança*) under LGPD Art. 46 is broadly consistent with NIST CSF Protect function categories. ANPD's 2023 security guidance references risk-based approaches to data protection that align with NIST's identify-protect-detect model.

### Financial Sector

FEBRABAN (Brazilian Federation of Banks) and the BCB have issued guidance that encourages financial institutions to use established frameworks — explicitly mentioning NIST CSF, ISO 27001, and CIS Controls — to structure their cybersecurity programs in compliance with BACEN 4.893.

### Academic and Industry Adoption

Brazilian universities and professional certification bodies (including local ISACA and ISC² chapters) use NIST CSF as a teaching framework. The NIST CSF is increasingly used as a common language for cybersecurity risk communication between Brazilian CISOs and their boards.

---

## Community Portuguese Translation Resources

### Official NIST Resources

NIST publishes CSF 2.0 in English. As of 2024, NIST has announced plans for translated versions of the CSF 2.0 Quick Start Guides:

- **CSF 2.0 Core (English):** [nist.gov/cyberframework](https://www.nist.gov/cyberframework)
- **NIST translation program:** NIST has historically produced or facilitated community translations for CSF 1.1; CSF 2.0 Portuguese translation is in progress via community collaboration

### Community and Industry Translations

| Resource | Description | Source |
|---|---|---|
| NIST CSF 1.1 Portuguese | Community translation of the full CSF 1.1 framework | Available via ISACA Brazil chapter and ANSI |
| ABNT NBR ISO/IEC 27001 | Portuguese-language equivalent via ABNT; covers similar control domains | ABNT (Brazilian standards body) |
| FEBRABAN cybersecurity guides | Portuguese-language practitioner guidance referencing CSF | FEBRABAN.org.br |
| CGI.br security publications | Portuguese-language internet governance and security documents | cgi.br |

> **Note:** For the most current Portuguese translation resources, check NIST's translation portal at [nist.gov/system/files/documents/cyberframework](https://www.nist.gov/cyberframework) and the ISACA Brazil chapter (isaca.org.br).

---

## NIST CSF to LGPD Mapping

The table below maps NIST CSF 2.0 Functions and Categories to the most relevant LGPD articles, supporting organizations that use NIST CSF as their operational framework while meeting LGPD requirements.

| CSF Function | CSF Category | LGPD Article | LGPD Requirement |
|---|---|---|---|
| **Govern** | Organizational Context (GV.OC) | Art. 37, 50 | Records of processing activities; privacy governance program |
| **Govern** | Risk Management Strategy (GV.RM) | Art. 50 §2 | Risk management as component of data protection governance |
| **Govern** | Cybersecurity Policy (GV.PO) | Art. 50 | Privacy and security policies as part of accountability program |
| **Identify** | Asset Management (ID.AM) | Art. 37 | Processing activity records (data inventory) |
| **Identify** | Risk Assessment (ID.RA) | Art. 38, 50 | Privacy Impact Assessment (RIPD); risk-based controls |
| **Protect** | Identity Management & Access Control (PR.AA) | Art. 46 | Technical security measures to protect personal data |
| **Protect** | Data Security (PR.DS) | Art. 46, 47 | Data protection measures; confidentiality obligations for processors |
| **Protect** | Platform Security (PR.PS) | Art. 46 | Administrative and technical controls for processing systems |
| **Protect** | Technology Infrastructure Resilience (PR.IR) | Art. 46 | Business continuity for personal data processing systems |
| **Detect** | Continuous Monitoring (DE.CM) | Art. 46, 48 | Monitoring for unauthorized access; early breach detection |
| **Respond** | Incident Management (RS.MA) | Art. 48 | Incident response for data breaches |
| **Respond** | Incident Analysis (RS.AN) | Art. 48 §1 | Identification of scope and impact of breach |
| **Respond** | Incident Reporting (RS.CO) | Art. 48 | Notification to ANPD and data subjects |
| **Recover** | Incident Recovery Plan (RC.RP) | Art. 46 | Recovery controls as part of security measures |

---

## How HailBytes Products Address Each CSF Function

| CSF Function | HailBytes SAT | HailBytes ASM |
|---|---|---|
| **Govern** | Training policies and program governance documentation | Asset inventory feeds risk governance decisions |
| **Identify** | Phishing simulation identifies employee risk posture | Continuous discovery of internet-facing assets and exposures |
| **Protect** | Security awareness training reduces human vulnerability | Exposure prioritization guides hardening efforts |
| **Detect** | Simulated attack campaigns test detection/response awareness | Real-time monitoring of new assets, open ports, and vulnerabilities |
| **Respond** | Incident response training modules (recognizing and reporting incidents) | Alert workflows for newly discovered critical exposures |
| **Recover** | Incident response training covers employee awareness of recovery procedures; standalone business continuity modules are not part of the current built-in library | Historical attack surface data supports post-incident analysis |

---

## Practical Guidance for Brazilian Enterprises

### Using NIST CSF + LGPD Together

1. **Start with the Govern function** — establish your data protection governance program (LGPD Art. 50) before optimizing individual controls
2. **Use Identify to build your data map** — NIST ID.AM (asset management) is directly equivalent to the processing activity records required by LGPD Art. 37
3. **Map Protect controls to LGPD Art. 46** — any Protect implementation is simultaneously evidence for LGPD security measure compliance
4. **Build Detect + Respond around LGPD Art. 48** — your breach detection and response capabilities must support the ANPD notification timeline (ANPD Res. CD/ANPD No. 15/2024: 3 business days for preliminary notice)
5. **Use the CSF Tier model for risk communication** — CSF Tiers (Partial → Risk Informed → Repeatable → Adaptive) provide a maturity language that boards understand

---

## Key Takeaways for Enterprise Buyers

1. **NIST CSF is the common language** — use it to communicate cybersecurity posture to international stakeholders while complying with Brazilian regulations
2. **CSF 2.0 + LGPD is a strong combination** — the new Govern function directly supports LGPD's accountability principle
3. **Portuguese translations exist** — for Brazilian teams, CSF 1.1 Portuguese translations are available; CSF 2.0 translations are in progress
4. **BACEN and LGPD both align with CSF** — a single CSF-based program can provide evidence for BACEN 4.893 and LGPD simultaneously
5. **HailBytes maps to the full CSF** — SAT addresses the human/people dimensions (Protect, Detect, Respond) while ASM addresses the technical dimensions (Identify, Detect, Respond)
