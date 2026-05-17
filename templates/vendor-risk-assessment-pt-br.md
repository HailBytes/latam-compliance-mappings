# Questionário de Avaliação de Risco de Fornecedores

**Versão:** 1.0
**Jurisdição:** Brasil — LGPD (Lei 13.709/2018) + BACEN Resolução 4.893/2021
**Idioma:** Português (Brasil)
**Instrução:** Este questionário deve ser respondido pelo fornecedor e revisado pelo responsável pela gestão de fornecedores e pelo Encarregado de Dados (DPO) antes da contratação.

> *Este modelo é fornecido para fins informativos. Adapte-o às políticas internas da sua organização.*

---

## SEÇÃO 1 — IDENTIFICAÇÃO DO FORNECEDOR

| Campo | Resposta |
|---|---|
| **Razão Social** | |
| **CNPJ / Identificação Fiscal** | |
| **Endereço Sede** | |
| **País de Sede** | |
| **Website** | |
| **Representante Legal** | |
| **Contato de Segurança / DPO** | Nome: E-mail: Telefone: |
| **Serviço / Produto Contratado** | |
| **Data do Questionário** | |
| **Revisado por (cliente)** | |

---

## SEÇÃO 2 — CLASSIFICAÇÃO DE RISCO

Marque todas as categorias aplicáveis ao serviço prestado pelo fornecedor:

### 2.1. Tipo de Dados Envolvidos

| Categoria | Aplicável? | Estimativa de Volume |
|---|---|---|
| ☐ Dados pessoais comuns (nome, e-mail, telefone) | | |
| ☐ Dados pessoais sensíveis (saúde, biometria, origem étnica, religião, orientação sexual) | | |
| ☐ Dados financeiros / bancários | | |
| ☐ Credenciais de acesso / senhas | | |
| ☐ Dados de menores de idade | | |
| ☐ Dados de funcionários | | |
| ☐ Nenhum dado pessoal — apenas dados corporativos / técnicos | | |

### 2.2. Nível de Acesso do Fornecedor

| Tipo de Acesso | Aplicável? |
|---|---|
| ☐ Acesso direto a sistemas de produção | |
| ☐ Acesso a banco de dados com dados pessoais | |
| ☐ Acesso remoto à rede corporativa | |
| ☐ Acesso físico a instalações da empresa | |
| ☐ Processamento de dados em ambiente próprio do fornecedor | |
| ☐ Processamento em ambiente do cliente (on-premises ou BYOC) | |

### 2.3. Criticidade do Serviço

| Criticidade | Descrição | Aplicável? |
|---|---|---|
| **Alta** | Serviço essencial para operação; indisponibilidade causa impacto direto ao negócio | ☐ |
| **Média** | Serviço importante mas com alternativas ou tolerância a indisponibilidade de curto prazo | ☐ |
| **Baixa** | Serviço auxiliar sem acesso a dados sensíveis e com baixo impacto operacional | ☐ |

**Classificação de Risco Consolidada:** ☐ Alto ☐ Médio ☐ Baixo *(definida pelo avaliador)*

---

## SEÇÃO 3 — CERTIFICAÇÕES DE SEGURANÇA

| Certificação | Possui? | Versão / Escopo | Validade | Documento Disponível? |
|---|---|---|---|---|
| **ISO 27001** | ☐ Sim ☐ Não | | | ☐ Sim ☐ Não |
| **SOC 2 Type II** | ☐ Sim ☐ Não | | | ☐ Sim ☐ Não |
| **PCI DSS** | ☐ Sim ☐ Não | | | ☐ Sim ☐ Não |
| **ISO 27701** (Privacidade) | ☐ Sim ☐ Não | | | ☐ Sim ☐ Não |
| **Outra:** __________ | ☐ Sim ☐ Não | | | ☐ Sim ☐ Não |

---

## SEÇÃO 4 — CONTROLES DE ACESSO E AUTENTICAÇÃO

| Pergunta | Resposta |
|---|---|
| 4.1. A autenticação multifator (MFA) é obrigatória para acesso a sistemas que processam dados pessoais? | ☐ Sim ☐ Não ☐ Parcialmente — Detalhar: |
| 4.2. Existe política de controle de acesso baseada no princípio do menor privilégio? | ☐ Sim ☐ Não |
| 4.3. As contas de acesso são individuais e nominais (sem contas compartilhadas)? | ☐ Sim ☐ Não ☐ Exceções — Detalhar: |
| 4.4. Existe processo de revisão periódica de acessos? Qual a frequência? | ☐ Sim — Frequência: _______ ☐ Não |
| 4.5. O acesso de ex-funcionários é revogado imediatamente após o desligamento? | ☐ Sim ☐ Não ☐ Prazo máximo: _______ |
| 4.6. Todos os acessos a dados pessoais são registrados em logs de auditoria? | ☐ Sim ☐ Não |
| 4.7. Por quanto tempo os logs de acesso são retidos? | _______ meses/anos |

---

## SEÇÃO 5 — PROTEÇÃO DE DADOS E CRIPTOGRAFIA

| Pergunta | Resposta |
|---|---|
| 5.1. Os dados em repouso (*data at rest*) são criptografados? | ☐ Sim ☐ Não — Algoritmo: |
| 5.2. Os dados em trânsito (*data in transit*) são protegidos com TLS 1.2 ou superior? | ☐ Sim ☐ Não |
| 5.3. As chaves criptográficas são gerenciadas pelo fornecedor ou pelo cliente? | ☐ Fornecedor ☐ Cliente ☐ Compartilhado |
| 5.4. Existe política formal de gestão de chaves criptográficas? | ☐ Sim ☐ Não |
| 5.5. Os dados pessoais são anonimizados ou pseudonimizados quando possível? | ☐ Sim ☐ Não ☐ Parcialmente |
| 5.6. Em quais regiões/países os dados são armazenados e processados? | |
| 5.7. Os dados são armazenados no Brasil ou fora do Brasil? | ☐ Somente Brasil ☐ Fora do Brasil — Países: |

---

## SEÇÃO 6 — GESTÃO DE VULNERABILIDADES E TESTES DE SEGURANÇA

| Pergunta | Resposta |
|---|---|
| 6.1. O fornecedor realiza testes de penetração (*pentest*) periódicos? Frequência? | ☐ Sim — Frequência: _______ ☐ Não |
| 6.2. O fornecedor realiza varreduras de vulnerabilidades nos sistemas? Frequência? | ☐ Sim — Frequência: _______ ☐ Não |
| 6.3. O cliente pode solicitar o resultado dos testes de segurança? | ☐ Sim ☐ Não ☐ Sob NDA |
| 6.4. Existe processo documentado de gestão e priorização de vulnerabilidades? | ☐ Sim ☐ Não |
| 6.5. Qual o prazo médio de correção de vulnerabilidades críticas (*CVSS ≥ 9.0*)? | _______ dias |
| 6.6. O fornecedor possui programa de divulgação responsável (*bug bounty* ou VDP)? | ☐ Sim ☐ Não |

---

## SEÇÃO 7 — GESTÃO DE INCIDENTES

| Pergunta | Resposta |
|---|---|
| 7.1. O fornecedor possui Política de Resposta a Incidentes documentada? | ☐ Sim ☐ Não |
| 7.2. Em quanto tempo o fornecedor notificará o cliente em caso de incidente de segurança envolvendo dados pessoais? | _______ horas |
| 7.3. A notificação inclui: natureza do incidente, dados afetados e medidas de contenção? | ☐ Sim ☐ Não ☐ Parcialmente |
| 7.4. O fornecedor realizou simulações de resposta a incidentes nos últimos 12 meses? | ☐ Sim ☐ Não |
| 7.5. Houve incidentes de segurança envolvendo dados de clientes nos últimos 2 anos? | ☐ Sim — Detalhar: ☐ Não |
| 7.6. O fornecedor dispõe de seguro de responsabilidade cibernética (*cyber insurance*)? | ☐ Sim — Cobertura: _______ ☐ Não |

---

## SEÇÃO 8 — SUBCONTRATADOS E CADEIA DE FORNECIMENTO

| Pergunta | Resposta |
|---|---|
| 8.1. O fornecedor utiliza subcontratados para processar dados pessoais do cliente? | ☐ Sim ☐ Não |
| 8.2. Liste os principais subcontratados que terão acesso a dados pessoais: | |
| 8.3. Os subcontratados estão sujeitos às mesmas obrigações de segurança e privacidade? | ☐ Sim ☐ Não |
| 8.4. O cliente será notificado antes de qualquer alteração na cadeia de subcontratados? | ☐ Sim ☐ Não |
| 8.5. O fornecedor realiza due diligence de segurança em seus próprios subcontratados? | ☐ Sim ☐ Não |

---

## SEÇÃO 9 — TRANSFERÊNCIA INTERNACIONAL DE DADOS

| Pergunta | Resposta |
|---|---|
| 9.1. Dados pessoais serão transferidos para fora do Brasil? | ☐ Sim ☐ Não |
| 9.2. Se sim, para quais países? | |
| 9.3. Qual mecanismo legal é utilizado para a transferência? | ☐ País com nível adequado (ANPD) ☐ Cláusulas Contratuais Padrão (ANPD) ☐ Regras Corporativas Globais ☐ Consentimento do titular ☐ Outro: |
| 9.4. O fornecedor pode garantir que os dados não serão acessados em jurisdições sem adequação? | ☐ Sim ☐ Não ☐ Não aplicável |

---

## SEÇÃO 10 — CLÁUSULAS CONTRATUAIS MÍNIMAS EXIGIDAS

Para fornecedores com acesso a dados pessoais, as seguintes cláusulas contratuais são **obrigatórias** (conforme LGPD Art. 37–39 e BACEN 4.893 Art. 14–17):

| Cláusula | Status |
|---|---|
| Definição de papéis (controlador/operador) | ☐ Incluída ☐ Pendente |
| Finalidade e limitação de uso dos dados | ☐ Incluída ☐ Pendente |
| Obrigação de notificação de incidentes em até [PRAZO] horas | ☐ Incluída ☐ Pendente |
| Direito de auditoria do cliente sobre o fornecedor | ☐ Incluída ☐ Pendente |
| Proibição de uso dos dados para fins próprios do fornecedor | ☐ Incluída ☐ Pendente |
| Obrigação de eliminação / devolução de dados ao término | ☐ Incluída ☐ Pendente |
| Restrição a subcontratados e obrigação de notificação | ☐ Incluída ☐ Pendente |
| Cumprimento da LGPD e legislação aplicável | ☐ Incluída ☐ Pendente |
| Direitos de autoridade regulatória (BCB, ANPD) sobre o fornecedor | ☐ Incluída ☐ Pendente |

---

## RUBRICA DE PONTUAÇÃO DE RISCO

Utilize esta rubrica para consolidar o resultado da avaliação:

| Área | Pontuação Máxima | Pontuação Obtida | Critério |
|---|---|---|---|
| Certificações de segurança | 20 | | ISO 27001 = 10pts; SOC 2 = 5pts; ISO 27701 = 5pts |
| Controles de acesso | 20 | | MFA = 5; menor privilégio = 5; logs = 5; revisão periódica = 5 |
| Criptografia e dados | 15 | | Criptografia em repouso e trânsito = 10; localização Brasil = 5 |
| Vulnerabilidades e testes | 15 | | Pentest anual = 10; prazo correção crítica ≤7d = 5 |
| Gestão de incidentes | 15 | | Política documentada = 5; notificação ≤72h = 5; simulações = 5 |
| Cadeia de fornecimento | 10 | | Due diligence subcontratados = 5; notificação mudanças = 5 |
| Cláusulas contratuais | 5 | | Todas presentes = 5 |
| **TOTAL** | **100** | | |

**Resultado:**
- **80–100:** Baixo risco — aprovado para contratação
- **60–79:** Risco médio — aprovado com plano de ação e revisão em 6 meses
- **40–59:** Alto risco — aprovado condicionado a remediações antes da contratação
- **< 40:** Risco crítico — não recomendado para contratação sem remediações substanciais

**Decisão:** ☐ Aprovado ☐ Aprovado com condições ☐ Reprovado
**Justificativa:** _______________________________________________
**Aprovado por:** _______________________________________________ Data: ___________

---

> *Este modelo é fornecido para fins informativos. Adapte-o às políticas internas da sua organização e consulte um advogado.*
