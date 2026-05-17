# Runbook de Resposta a Incidentes de Segurança

**Versão:** 1.0
**Jurisdição:** Brasil — LGPD (Lei 13.709/2018) + BACEN Resolução 4.893/2021
**Idioma:** Português (Brasil)
**Revisão:** [DATA DA ÚLTIMA REVISÃO]
**Responsável:** [CARGO DO RESPONSÁVEL — ex.: CISO / Encarregado de Dados]

---

## 1. Objetivo e Escopo

Este runbook define os procedimentos operacionais para detecção, contenção, erradicação, recuperação e comunicação de incidentes de segurança cibernética que possam envolver dados pessoais (*violação de dados pessoais*) ou sistemas críticos da organização.

**Obrigações legais cobertas:**
- **LGPD Art. 48:** Notificação à ANPD e aos Titulares em caso de incidente de segurança relevante
- **BACEN 4.893 Art. 12–13:** Notificação ao Banco Central do Brasil para incidentes relevantes em instituições financeiras (prazo: 72 horas)
- **LGPD Resolução CD/ANPD No. 15/2023:** Regulamenta prazos e conteúdo da notificação à ANPD

---

## 2. Classificação de Incidentes

### Critérios de Classificação

| Prioridade | Critérios | Exemplos |
|---|---|---|
| **P1 — Crítico** | Violação de dados pessoais sensíveis em larga escala; comprometimento de sistemas críticos; ransomware em produção; risco imediato de dano irreparável | Vazamento de dados de saúde ou financeiros de milhares de titulares; ransomware em core banking; credenciais de administrador comprometidas |
| **P2 — Alto** | Violação de dados pessoais não sensíveis; acesso não autorizado confirmado; incidente com potencial de escalonamento | Vazamento de nomes e e-mails corporativos; acesso indevido por ex-funcionário; servidor comprometido sem dados confirmados exfiltrados |
| **P3 — Médio/Baixo** | Suspeita de incidente sem confirmação; violações de política sem impacto externo; tentativas bloqueadas | Phishing bloqueado pelo gateway; tentativa de acesso negada; uso indevido de credenciais internas sem exfiltração |

---

## 3. Papéis e Responsabilidades

| Papel | Responsabilidades | Contato |
|---|---|---|
| **Encarregado de Dados (DPO)** | Coordenar notificações à ANPD; orientar decisões legais; comunicar-se com titulares | [E-MAIL] / [TELEFONE] |
| **CISO / Segurança da Informação** | Liderar resposta técnica; coordenar contenção e erradicação; declarar P1/P2 | [E-MAIL] / [TELEFONE] |
| **Jurídico** | Avaliar obrigações de notificação; analisar cláusulas contratuais; comunicação com reguladores | [E-MAIL] / [TELEFONE] |
| **Comunicação / Relações Públicas** | Comunicados externos, se aplicável; mensagens a clientes e imprensa | [E-MAIL] / [TELEFONE] |
| **TI / Infraestrutura** | Suporte técnico à contenção e recuperação; análise forense | [E-MAIL] / [TELEFONE] |
| **Alta Direção / Board** | Decidir ações de alto impacto; aprovação de comunicados públicos | [E-MAIL] / [TELEFONE] |

**Comandante do Incidente (Incident Commander):** [CARGO] — responsável pela coordenação geral durante P1/P2.

---

## 4. Prazos de Notificação — Resumo

| Destinatário | Prazo | Base Legal | Conteúdo Mínimo |
|---|---|---|---|
| **Equipe interna / CISO** | Imediato (dentro de 1h do conhecimento) | Política interna | Natureza do incidente, sistemas afetados, ações iniciais |
| **Encarregado (DPO)** | Dentro de 4h | Política interna | Briefing completo para avaliar obrigação de notificação externa |
| **ANPD — Comunicação Inicial** | **Até 3 dias úteis** do conhecimento do incidente (Res. CD/ANPD 15/2023) | LGPD Art. 48 + Res. ANPD 15/2023 | Dados iniciais: natureza, categorias de dados, medidas de contenção |
| **ANPD — Comunicação Complementar** | Prazo estabelecido pela ANPD na resposta inicial | Res. ANPD 15/2023 | Relatório completo com análise de causa raiz |
| **Banco Central (BACEN)** | **Até 72 horas** do conhecimento (incidentes relevantes) | BACEN 4.893 Art. 12 | Natureza, sistemas afetados, impacto estimado, medidas tomadas |
| **Titulares afetados** | Prazo razoável / conforme orientação ANPD | LGPD Art. 48 §1 | Natureza do incidente, dados envolvidos, medidas recomendadas |

> **Atenção:** O prazo começa a contar a partir do momento em que a organização *tomou conhecimento* do incidente — não da data em que ele ocorreu.

---

## 5. Fases do Processo de Resposta

### Fase 1 — Detecção e Triagem

**Objetivo:** Identificar e confirmar a ocorrência do incidente o mais rápido possível.

**Checklist:**
- [ ] Alerta ou reporte recebido por: [canal — ex.: SIEM, e-mail, helpdesk, terceiro]
- [ ] Registrar data e hora do conhecimento inicial: ___________
- [ ] Atribuir analista de plantão responsável pela triagem
- [ ] Coletar evidências iniciais sem alterar o estado dos sistemas
- [ ] Classificar o incidente (P1 / P2 / P3) com base nos critérios da Seção 2
- [ ] Notificar o Incident Commander (se P1 ou P2)
- [ ] Abrir registro formal no sistema de tickets: [SISTEMA] Ticket nº: ___________

---

### Fase 2 — Contenção

**Objetivo:** Impedir que o incidente se propague ou cause danos adicionais.

**Contenção Imediata (curto prazo):**
- [ ] Isolar sistemas comprometidos da rede (se aplicável sem interromper serviços críticos)
- [ ] Revogar credenciais comprometidas ou suspeitas
- [ ] Bloquear IPs / endereços suspeitos no firewall / WAF
- [ ] Preservar logs e evidências (captura de imagem forense se P1)
- [ ] Notificar DPO e Jurídico
- [ ] Iniciar timeline documentada do incidente

**Contenção de Longo Prazo:**
- [ ] Implementar controles temporários para manter operação segura
- [ ] Definir plano de contenção com prazo de resolução estimado
- [ ] Comunicar stakeholders internos conforme cadeia de escalamento

---

### Fase 3 — Erradicação

**Objetivo:** Eliminar a causa raiz do incidente.

- [ ] Identificar vetor de ataque e causa raiz
- [ ] Remover malware, backdoors ou acessos não autorizados
- [ ] Aplicar patches e correções de segurança
- [ ] Reforçar controles que falharam
- [ ] Validar erradicação com teste / varredura
- [ ] Documentar ações realizadas com timestamps

---

### Fase 4 — Recuperação

**Objetivo:** Restaurar operação normal de forma segura e monitorada.

- [ ] Restaurar sistemas a partir de backup limpo (se necessário)
- [ ] Validar integridade dos dados restaurados
- [ ] Reativar sistemas isolados de forma gradual e monitorada
- [ ] Monitorar sistemas restaurados por no mínimo [PRAZO — ex.: 72h] após reativação
- [ ] Confirmar ausência de atividade suspeita remanescente
- [ ] Declarar fim da fase de recuperação e comunicar stakeholders

---

### Fase 5 — Notificações Regulatórias

#### 5.1. Notificação à ANPD

Utilizar o formulário oficial disponível em: [gov.br/anpd](https://www.gov.br/anpd/)

**Conteúdo obrigatório (Res. CD/ANPD 15/2023):**
- [ ] Data e hora do conhecimento do incidente
- [ ] Natureza dos dados pessoais afetados
- [ ] Categorias e quantidade estimada de titulares afetados
- [ ] Informações de contato do Encarregado (DPO)
- [ ] Medidas técnicas e administrativas adotadas para contenção
- [ ] Riscos relacionados ao incidente
- [ ] Medidas de mitigação implementadas ou em andamento

#### 5.2. Notificação ao BACEN (instituições financeiras — BACEN 4.893)

- [ ] Preencher formulário BACEN / usar canal oficial [inserir link/canal BACEN]
- Conteúdo: natureza do incidente, data de ocorrência, sistemas afetados, estimativa de impacto, medidas de resposta, ponto de contato

#### 5.3. Comunicação aos Titulares

- [ ] Identificar titulares afetados
- [ ] Redigir comunicado claro e acessível (sem jargão técnico excessivo)
- [ ] Comunicado deve incluir: o que aconteceu, quais dados foram afetados, riscos potenciais, medidas tomadas pela organização, medidas recomendadas ao titular, canal de contato para dúvidas
- [ ] Aprovar comunicado com Jurídico e DPO
- [ ] Enviar por canal adequado: e-mail, portal, carta, conforme tipo de relacionamento

---

### Fase 6 — Lições Aprendidas (*Post-Mortem*)

**Prazo:** Reunião de post-mortem em até **[PRAZO — ex.: 15 dias úteis]** após o encerramento do incidente.

**Agenda padrão:**
1. Linha do tempo do incidente (timeline completa)
2. Causa raiz identificada
3. O que funcionou bem na resposta
4. O que falhou ou poderia ter sido mais rápido
5. Ações corretivas e preventivas com responsável e prazo
6. Atualização da documentação de segurança
7. Atualização deste Runbook, se necessário

**Saída obrigatória:** Relatório de Post-Mortem registrado em [SISTEMA / REPOSITÓRIO]. Copiar DPO, CISO e Jurídico.

---

## 6. Formulários e Checklists

### Registro Inicial do Incidente

| Campo | Informação |
|---|---|
| **Data/hora do conhecimento** | |
| **Reportado por** | |
| **Sistemas / dados afetados** | |
| **Classificação inicial** | P1 / P2 / P3 |
| **Incident Commander** | |
| **Ticket nº** | |
| **Notificações internas realizadas** | DPO: ☐ CISO: ☐ Jurídico: ☐ Direção: ☐ |

### Checklist de Notificação Regulatória

| Obrigação | Prazo | Realizado | Data/Hora | Responsável |
|---|---|---|---|---|
| Notificação ANPD (preliminar) | 3 dias úteis | ☐ | | |
| Notificação ANPD (complementar) | Conforme ANPD | ☐ | | |
| Notificação BACEN (se aplicável) | 72 horas | ☐ | | |
| Comunicação aos titulares | Conforme ANPD | ☐ | | |
| Comunicação a parceiros/fornecedores | Conforme contratos | ☐ | | |

---

> *Este modelo é fornecido para fins informativos. Consulte um advogado e adapte às políticas internas da sua organização.*
