# BACEN Resolution 4.893/2021 — Cybersecurity for Financial Institutions

## Metadata

| Field | Detail |
|---|---|
| **Jurisdiction** | Federative Republic of Brazil |
| **Regulation** | Resolução BCB No. 4.893 (February 26, 2021) |
| **Enacted** | February 26, 2021 |
| **Effective** | July 1, 2021 |
| **Regulator** | Banco Central do Brasil (BCB / BACEN) |
| **Supersedes** | Resolução No. 4.658/2018 |
| **Official Text** | [bcb.gov.br](https://www.bcb.gov.br/estabilidadefinanceira/resolucao4893) |

---

## Overview

Resolution 4.893/2021 (*Resolução BCB No. 4.893*) is the primary cybersecurity regulation issued by the Banco Central do Brasil (BCB) for financial institutions under its supervision. It superseded Resolution 4.658/2018, strengthening requirements around cybersecurity policy, incident notification, cloud computing governance, and third-party risk management.

The resolution applies to all entities authorized to operate by BCB, including:

- Commercial banks (*bancos comerciais*)
- Multiple service banks (*bancos múltiplos*)
- Payment institutions (*instituições de pagamento*)
- Fintechs and digital lenders (*fintechs de crédito*)
- Credit unions (*cooperativas de crédito*)
- Mortgage companies, leasing companies, and other BCB-licensed entities

---

## Cybersecurity Policy Requirements (Art. 4–5)

Each institution must adopt, implement, and maintain a formal **Cybersecurity Policy** (*Política de Segurança Cibernética*) approved by the Board of Directors (*conselho de administração*) or equivalent governance body.

The policy must address:

| Requirement | Detail |
|---|---|
| **Risk appetite** | Define acceptable levels of cyber risk aligned with business strategy |
| **Roles and responsibilities** | Clear ownership for cybersecurity functions |
| **Asset classification** | Identify and classify information assets by criticality and sensitivity |
| **Preventive controls** | Authentication, access control, encryption, network segmentation |
| **Detection and monitoring** | SIEM, anomaly detection, log retention |
| **Response and recovery** | Incident response plan, business continuity, disaster recovery |
| **Testing schedule** | Mandatory penetration tests and vulnerability assessments at defined intervals |
| **Employee awareness** | Training and communication programs for all staff handling sensitive data |
| **Continuous improvement** | Regular review cycle; at minimum annual review |

Annual reporting to the Board is required. The policy and action plans must be registered with the BCB and made available on request.

---

## Incident Response and Notification (Art. 12–13)

### Incident Classification

Institutions must maintain a formal incident classification scheme (*classificação de incidentes relevantes*). A "relevant incident" (*incidente relevante*) is one that:
- Affects critical systems or sensitive customer data at scale
- Causes or threatens significant financial or reputational harm
- Involves confirmed breach of security controls
- Triggers regulatory notification obligations

### Notification to BCB

| Trigger | Timeline |
|---|---|
| Knowledge of a relevant cybersecurity incident | Report to BCB within **72 hours** |
| Incident affecting payment infrastructure | Immediate notification (same business day) |
| Final post-incident report | Within 30 days of resolution |

Notification must include: nature of incident, systems/data affected, initial containment measures, estimated impact, and corrective action plan.

---

## Cloud Computing Rules (Art. 14–17)

Resolution 4.893 explicitly permits financial institutions to use cloud services (*computação em nuvem*), subject to the following conditions:

### Permissible Use

- Public, private, hybrid, and community cloud models are permitted
- Data may be stored or processed outside Brazil **provided** BCB retains unimpeded audit access rights
- Institutions must assess risk equivalence of cloud controls versus on-premises

### Required Controls for Cloud Adoption

| Control Area | Requirement |
|---|---|
| **Due diligence** | Formal risk assessment of CSP before contract signing |
| **Contractual protections** | CSP must agree to BCB audit rights, breach notification, data deletion on exit |
| **Data classification** | Define which data categories may be processed in cloud vs. kept on-premises |
| **Exit strategy** | Data portability and transition plan documented before go-live |
| **Concentration risk** | Assess dependency on single CSP; maintain contingency |
| **Segregation** | Customer data must be logically segregated from other CSP customers |

### BCB Audit Rights Clause (Required)

Contracts with cloud service providers must include a clause granting the BCB the right to inspect premises, systems, and records related to the institution's data — even if data is stored outside Brazil.

---

## Third-Party and Outsourcing Controls (Art. 14–17)

### Scope

All material outsourcing (*prestação de serviços relevantes de processamento e armazenamento de dados*) is in scope, including:

- Core banking system providers
- Payment processors
- Cloud infrastructure providers
- Security operations and monitoring services
- IT support with access to production systems

### Required Controls

| Requirement | Detail |
|---|---|
| **Pre-contract due diligence** | Security assessment before engagement; review of CSP/provider's own certifications (ISO 27001, SOC 2) |
| **Contractual clauses** | Incident notification obligations on the provider; data handling standards; audit rights |
| **Ongoing monitoring** | Annual re-assessment of critical providers; continuous monitoring for systemic risk |
| **Concentration risk management** | Maximum tolerable dependency on any single provider must be defined |
| **Exit / substitution plan** | Must be tested or at least documented for all critical providers |
| **Subcontractor visibility** | Institution must know the subcontractor chain of critical service providers |

---

## Annual Report to the Board

Each institution must prepare and present an **Annual Cybersecurity Report** (*Relatório Anual de Segurança Cibernética*) to its Board of Directors covering:

- Incidents and near-misses during the year
- Results of penetration tests and vulnerability assessments
- Status of the cybersecurity action plan (*plano de ação*)
- Third-party risk review outcomes
- Training and awareness metrics
- Planned improvements for the next cycle

This report must be retained and provided to BCB on demand.

---

## Key Differences from Resolution 4.658/2018

| Area | 4.658/2018 | 4.893/2021 |
|---|---|---|
| Incident notification | Vague timeline | 72-hour hard deadline |
| Cloud rules | Basic principles | Detailed controls and audit rights |
| Third-party risk | High-level requirements | Specific due diligence and contract requirements |
| Board reporting | Annual report required | More structured content requirements |
| Concentration risk | Not explicitly addressed | Explicit assessment requirement |

---

## Key Takeaways for Enterprise Buyers

1. **72-hour notification is non-negotiable** — your incident detection and escalation chain must be designed to hit this deadline
2. **Cloud is permitted but conditional** — BCB must be able to audit your cloud data; ensure your CSP contract includes this clause
3. **Attack surface management is a regulatory expectation** — Art. 6 vulnerability testing requirement maps directly to continuous ASM capabilities
4. **Third-party risk requires contractual teeth** — your vendor (including HailBytes) must accept audit rights and breach notification obligations
5. **BYOC eliminates CSP substitution risk** — when data lives in your own AWS/Azure account, you control the audit trail without depending on a vendor's cooperation
6. **Board-level accountability** — the annual report requirement means cybersecurity is a governance matter, not just an IT concern
