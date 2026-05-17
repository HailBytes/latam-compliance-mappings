# ISO 27001:2022 in Latin America — Regional Adoption Notes

> **Scope:** ISO 27001:2022 adoption patterns across Brazil, Mexico, and Argentina, including local certification infrastructure, regulatory cross-references, and common implementation gaps.

---

## Regional Adoption Overview

ISO/IEC 27001 is the dominant information security management system (ISMS) framework across Latin America. The 2022 revision (ISO/IEC 27001:2022) introduced significant changes to Annex A — reducing controls from 114 to 93, restructuring them into four themes (Organizational, People, Physical, Technological) — and organizations across the region are now in transition from the 2013 version.

LatAm adoption is primarily driven by:
- **Regulatory requirements** (BACEN 4893 explicitly references security controls that align with ISO 27001)
- **Enterprise procurement requirements** (large Brazilian and Mexican corporates require ISO 27001 from vendors)
- **Financial services and fintech sector** growth driving compliance investment
- **Government digital transformation programs** requiring baseline security certifications

---

## Local Certification Bodies

ISO 27001 certification requires assessment by an accredited certification body (CB). In LatAm, national accreditation bodies accredit local CBs:

| Country | National Accreditation Body | Acronym | ISO 27001 Certification Notes |
|---|---|---|---|
| **Brazil** | Instituto Nacional de Metrologia, Qualidade e Tecnologia | INMETRO | ABNT NBR ISO/IEC 27001 is the Brazilian localized standard; INMETRO-accredited CBs issue certificates recognized internationally |
| **Mexico** | Entidad Mexicana de Acreditación | EMA | Mexican standard NMX-I-27001-NYCE mirrors ISO 27001; EMA accredits local CBs |
| **Argentina** | Organismo Argentino de Acreditación | OAA | OAA-accredited CBs issue ISO 27001 certificates; IRAM publishes Argentine localization (IRAM-ISO 27001) |

### Major International CBs Active in the Region

Bureau Veritas, BSI Group, SGS, TÜV Rheinland, DNV, and LRQA all operate accredited certification programs in Brazil, Mexico, and Argentina. Most large enterprises in the region pursue certification through these international bodies for global recognition.

---

## Certified Organization Counts

*Approximate figures based on the ISO Survey of Certifications and publicly available data (2022–2023):*

| Country | Approximate ISO 27001 Certificates | Regional Context |
|---|---|---|
| **Brazil** | ~1,500–2,000 | Largest certified population in LatAm; concentrated in financial services, IT, and telecom |
| **Mexico** | ~600–900 | Growing rapidly; fintech sector driving demand |
| **Argentina** | ~200–350 | Smaller base; government and financial services primary adopters |
| **Colombia** | ~150–250 | Emerging; government programs pushing adoption |
| **Chile** | ~100–200 | Financial services and mining sector focused |

> **Note:** These are active certificate estimates. Total organizations that have achieved certification historically is higher. Brazil's financial sector (FEBRABAN members, fintechs under BACEN) is the largest driver of LatAm growth.

---

## How Local Regulators Reference ISO 27001

### Brazil — BACEN Resolution 4.893/2021

BACEN 4.893 does not mandate ISO 27001 certification but extensively references security controls and governance structures that align with it:

- Art. 4 cybersecurity policy requirements map to ISO 27001 Clause 5 (Leadership) and Clause 6 (Planning)
- Vulnerability testing requirements (Art. 6) align with ISO 27001 Annex A 8.8 (management of technical vulnerabilities)
- Third-party risk (Art. 14–17) maps to ISO 27001 Annex A 5.19–5.22 (supplier relationships)
- ISO 27001 certification is routinely accepted by BACEN examiners as evidence of baseline security program maturity

### Mexico — LFPDPPP Regulations (Art. 48)

The LFPDPPP Reglamento (2011) requires *responsables* to implement security measures (*medidas de seguridad*) proportional to the sensitivity of data. INAI guidance cites ISO 27001 and ISO 27002 as recognized frameworks for demonstrating compliance with this requirement.

### Argentina — AAIP Guidance

The AAIP has issued guidance citing ISO 27001 as a benchmark for the security measures required under Law 25.326 Art. 9. While not mandatory, ISO 27001 certification significantly strengthens compliance defensibility.

### Financial Sector Broadly

FELABAN (Latin American Federation of Banks) and regional financial stability bodies reference ISO 27001 in cross-border financial institution guidelines. Many multinational bank procurement teams require ISO 27001 from technology vendors operating in the region.

---

## Common Gap Areas in LatAm Implementations

Based on certification body assessment findings and industry reports:

| Gap Area | Description |
|---|---|
| **Asset inventory completeness** | Shadow IT and cloud sprawl leave asset registers incomplete; critical for Annex A 5.9 |
| **Supplier/third-party risk** | Annex A 5.19–5.22 supplier controls are frequently weak; vendor due diligence processes are often informal |
| **Incident response testing** | Plans exist but tabletop exercises and simulations are rarely conducted; required by Annex A 5.26 |
| **Information security objectives measurement** | Clause 6.2 requires measurable objectives; many organizations define them qualitatively only |
| **Competence and awareness evidence** | Annex A 6.3 training awareness requires documented evidence; often not maintained systematically |
| **Physical security for remote work** | Post-pandemic, home office environments are frequently out of scope for physical controls (Annex A 7) |
| **Cryptography policy** | Annex A 8.24 cryptography policy is often underdocumented; key management procedures frequently missing |
| **Cloud security controls** | Annex A 5.23 (information security for cloud services) is new in 2022 and widely unimplemented |

---

## ISO 27001 and LGPD / LFPDPPP Alignment

Implementing ISO 27001 provides significant foundational coverage for LGPD and LFPDPPP compliance — but is not a complete substitute:

| ISO 27001 Domain | LGPD Coverage | LFPDPPP Coverage |
|---|---|---|
| Information security policy (Clause 5) | LGPD Art. 50 (governance program) | LFPDPPP Reglamento Art. 48 |
| Asset management (A 5.9–5.14) | LGPD Art. 37 (records of processing) | LFPDPPP Art. 19 (security measures) |
| Access control (A 5.15–5.18) | LGPD Art. 46 (security measures) | LFPDPPP Reglamento Art. 57 |
| Supplier relationships (A 5.19–5.22) | LGPD Art. 39 (operator accountability) | LFPDPPP Art. 36 (third-party transfers) |
| Incident management (A 5.24–5.28) | LGPD Art. 48 (breach notification) | LFPDPPP Art. 21 (security incidents) |
| Business continuity (A 5.29–5.30) | LGPD Art. 46 (preventive measures) | LFPDPPP Reglamento Art. 58 |

**What ISO 27001 does NOT cover (requires separate LGPD/LFPDPPP work):**
- Data subject rights management (access, rectification, deletion requests)
- Legal basis documentation for processing
- Privacy notices (*Aviso de Privacidade* / *Aviso de Privacidad*)
- DPO / *Encarregado* appointment
- Records of processing activities (ROPA)
- Cross-border transfer mechanisms

---

## Key Takeaways for Enterprise Buyers

1. **ISO 27001 is the de facto vendor baseline** — if your vendor is not ISO 27001 certified, expect questions in Brazilian and Mexican enterprise procurement
2. **BACEN 4.893 alignment is strong** — ISO 27001's supplier, incident, and vulnerability controls directly address BACEN requirements
3. **Local accreditation matters** — INMETRO/EMA/OAA-accredited certificates carry weight with local regulators; international CBs are widely accepted
4. **2022 transition is ongoing** — ask vendors whether they have transitioned from ISO 27001:2013 to ISO 27001:2022 (deadline was October 2025)
5. **ISO 27001 + data subject rights work = compliance program** — the combination covers the operational and rights-based dimensions of LatAm privacy law
