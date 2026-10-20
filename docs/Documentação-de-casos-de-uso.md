# Documento de Casos de Uso — Sistema de Gestão de Academia

Projeto da disciplina **Análise e Projeto de Sistemas** — Semana 1.
Modelo de especificação: *Engenharia de Software Moderna* (nome com verbo no infinitivo, ator principal, fluxo normal e extensões, com pré e pós-condições quando úteis). Casos de uso incluídos aparecem <u>sublinhados</u>.

---

## 1. Visão geral do sistema

O Sistema de Gestão de Academia é uma aplicação web com banco de dados local SQLite que organiza alunos, funcionários, planos, matrículas, pagamentos, treinos e frequência de uma academia. O funcionário cadastra alunos, gerencia o ciclo de vida das matrículas (pendente, ativa, suspensa e encerrada), registra pagamentos do plano mensal (R$ 100, ou R$ 95 para estudantes) e da diária (R$ 35) e registra a presença. O administrador, além de tudo o que o funcionário faz, gerencia funcionários e planos e consulta relatórios gerenciais. O aluno acessa o sistema para consultar seu plano, seus pagamentos e sua frequência. Todo acesso exige autenticação e é limitado ao perfil do usuário.

---

## 2. Atores

| Ator | Descrição |
|---|---|
| **Aluno** | Acessa o próprio perfil para consultar plano, pagamentos e frequência, e pode alterar a própria senha. Seu acesso é restrito exclusivamente às informações e funcionalidades do seu perfil. |
| **Funcionário** | Responsável pela operação da academia. Cadastra, edita e arquiva alunos; cria, ativa, suspende, reativa e encerra matrículas; registra pagamentos e altera vencimentos; registra presença; associa treinos; e consulta o histórico de pagamentos. |
| **Administrador** | Especialização do Funcionário: possui todas as permissões dele e, além delas, gerencia funcionários e perfis, cria planos e visualiza os relatórios gerenciais. |

No diagrama, o Administrador se liga ao Funcionário por generalização. Por isso, os casos de uso do Funcionário não precisam ser ligados também ao Administrador.

---

## 3. Lista de casos de uso

| ID | Caso de uso | Ator principal | Histórias de origem | Issue |
|---|---|---|---|---|
| UC01 | Entrar no sistema | Administrador, Funcionário, Aluno | US01 | #3 |
| UC02 | Trocar a própria senha | Administrador, Funcionário, Aluno | US16 | #18 |
| UC03 | Gerenciar funcionários e perfis | Administrador | US02 | #4 |
| UC04 | Cadastrar e editar aluno | Funcionário | US03 | #5 |
| UC05 | Arquivar aluno | Funcionário | US15 | #17 |
| UC06 | Criar plano | Administrador | US04 | #6 |
| UC07 | Criar matrícula | Funcionário | US05 | #7 |
| UC08 | Ativar matrícula | Funcionário | US06 | #8 |
| UC09 | Suspender e reativar matrícula | Funcionário | US07 | #9 |
| UC10 | Encerrar matrícula | Funcionário | US08 | #10 |
| UC11 | Registrar pagamento | Funcionário | US09 | #11 |
| UC12 | Validar data e vencimento | (incluído por UC11) | US09 | #11 |
| UC13 | Aplicar desconto de estudante | (extensão de UC11) | US09 | #11 |
| UC14 | Alterar data de vencimento | Funcionário | US09 | #11 |
| UC15 | Registrar presença | Funcionário | US10 | #12 |
| UC16 | Associar treino ao aluno | Funcionário | US13 | #15 |
| UC17 | Consultar plano, pagamentos e frequência | Aluno | US11 | #13 |
| UC18 | Consultar histórico de pagamentos de um aluno | Funcionário | US14 | #16 |
| UC19 | Ver relatórios gerenciais | Administrador | US12 | #14 |

A numeração é a mesma do diagrama de casos de uso (`diagramas/casos-de-uso.png`).

### Conferência dos mínimos da disciplina

| Requisito | Mínimo | Situação |
|---|---|---|
| Atores | 3 | 3 (Aluno, Funcionário, Administrador) |
| Casos de uso | 12 (teto sugerido 20) | 19 |
| Casos de uso de CRUD puro | no máximo metade | 5 de 19 (UC03, UC04, UC05, UC06 e UC14), e todos têm regras de validação |
| Entidade com ciclo de vida de 4 estados | 1 | Matrícula: pendente, ativa, suspensa, encerrada (UC07 a UC10) |
| Regras de negócio com cálculo ou validação | 2 | Valor do pagamento e desconto (RN02), vencimento (RN03), presença (RN04), diária (RN05) |
| Autenticação com perfis de acesso | obrigatória | UC01 |

---

## 4. Rastreabilidade: história de usuário → caso de uso

| História | Descrição | Casos de uso |
|---|---|---|
| US01 | Entrar no sistema com perfil | UC01 |
| US02 | Gerenciar funcionários e perfis | UC03 |
| US03 | Cadastrar e editar alunos | UC04 |
| US04 | Criar planos | UC06 |
| US05 | Criar matrícula | UC07 |
| US06 | Ativar matrícula | UC08 |
| US07 | Suspender e reativar matrícula | UC09 |
| US08 | Encerrar matrícula | UC10 |
| US09 | Registrar pagamento com desconto e validação de vencimento | UC11, UC12, UC13, UC14 |
| US10 | Registrar presença | UC15 |
| US11 | Consultar plano, pagamentos e frequência | UC17 |
| US12 | Ver relatórios gerenciais | UC19 |
| US13 | Associar treino ao aluno | UC16 |
| US14 | Consultar histórico de pagamentos de um aluno | UC18 |
| US15 | Arquivar aluno | UC05 |
| US16 | Trocar a própria senha | UC02 |

Todas as 16 histórias originam pelo menos um caso de uso, e todos os 19 casos de uso têm pelo menos uma história de origem.

---

## 5. Relações entre casos de uso

| Relação | Justificativa |
|---|---|
| UC11 `<<include>>` UC12 | Todo registro de pagamento passa pela validação da data informada, e no plano mensal também pela verificação do vencimento. |
| UC13 `<<extend>>` UC11 | O desconto só ocorre em uma condição: aluno marcado como estudante com plano mensal (RN02). Ponto de extensão: cálculo do valor final. |
| Administrador → Funcionário (generalização) | O administrador herda todos os casos de uso do funcionário. |

---

## 6. Regras de negócio

| ID | Regra | Casos de uso |
|---|---|---|
| RN01 | Ciclo de vida da matrícula. Estados: pendente, ativa, suspensa e encerrada. Transições: pendente→ativa, ativa→suspensa, suspensa→ativa, ativa→encerrada, suspensa→encerrada. "Encerrada" é estado final. | UC07, UC08, UC09, UC10 |
| RN02 | Plano mensal: R$ 100 (aluno comum) ou R$ 95 (estudante, desconto fixo de R$ 5). Plano diária: R$ 35 para todos, sem desconto. | UC11, UC13 |
| RN03 | Vencimento do plano mensal atrelado ao dia da matrícula, podendo ser alterado. Todo pagamento é "em dia" (até o vencimento) ou "em atraso" (depois). Data inválida é recusada. Inadimplente é o aluno com matrícula mensal ativa cujo vencimento passou sem pagamento registrado. | UC11, UC12, UC14, UC19 |
| RN04 | A presença só pode ser registrada em matrícula "ativa". Na diária, só no dia pago. | UC15, UC16 |
| RN05 | A matrícula de diária vale apenas para o dia do pagamento e é encerrada automaticamente ao fim desse dia. | UC11, UC10 |

---

## 7. Glossário

| Termo | Significado |
|---|---|
| Usuário | Qualquer pessoa autenticada no sistema: Administrador, Funcionário ou Aluno. |
| Aluno | Pessoa cadastrada na academia que possui ou possuiu matrícula. |
| Estudante | Aluno que comprovou essa condição por matrícula ou carteirinha de instituição de ensino ou do governo. Tem direito ao desconto do plano mensal. |
| Plano | Opção oferecida pela academia, com nome, duração, preço e tipo (mensal ou diária). |
| Matrícula | Vínculo de um aluno com um plano. Passa pelos estados pendente, ativa, suspensa e encerrada. |
| Vencimento | Data limite de pagamento do plano mensal. |
| Em dia / Em atraso | Situação do pagamento: feito até o vencimento ou depois dele. |
| Inadimplente | Aluno com matrícula mensal ativa cujo vencimento passou sem pagamento registrado. |
| Presença | Registro, com data e hora, de que o aluno esteve na academia. |
| Frequência | Conjunto das presenças de um aluno. |
| Treino | Rotina de exercícios associada a um aluno. |

---

## 8. Especificação dos casos de uso

### UC01 — Entrar no sistema

**Ator:** Administrador, Funcionário ou Aluno (Usuário)

**Pré-condição:** o usuário está cadastrado e ativo.

**Fluxo normal:**

1. Usuário informa e-mail e senha
2. Sistema valida as credenciais
3. Sistema identifica o perfil do usuário
4. Sistema apresenta a tela inicial do perfil

**Extensões:**

- **2a** Se as credenciais são inválidas, recusar o acesso sem informar qual dado está errado
- **2b** Se o usuário está desativado, recusar o acesso
- **4a** Se o usuário tenta acessar uma função fora do seu perfil, bloquear o acesso (a verificação vale também no servidor, não só nas telas)
- **\*a** A qualquer momento, usuário encerra a sessão e o sistema a finaliza

**Pós-condição:** sessão iniciada com acesso restrito ao perfil do usuário.

**Observação:** a senha é armazenada de forma protegida (hash).

---

### UC02 — Trocar a própria senha

**Ator:** Administrador, Funcionário ou Aluno

**Pré-condição:** usuário autenticado.

**Fluxo normal:**

1. Usuário informa a senha atual e a nova senha
2. Sistema valida a senha atual
3. Sistema valida a nova senha
4. Sistema atualiza a senha, armazenando-a de forma protegida
5. Sistema informa que a senha foi alterada

**Extensões:**

- **2a** Se a senha atual está errada, recusar a troca
- **3a** Se a nova senha é inválida, solicitar outra senha

---

### UC03 — Gerenciar funcionários e perfis

**Ator:** Administrador

**Propósito:** controlar quem pode acessar o sistema e com qual perfil.

**Fluxo normal:**

1. Administrador informa os dados do novo funcionário e o perfil de acesso
2. Sistema valida os dados
3. Sistema registra o funcionário
4. Sistema informa que o funcionário já pode entrar com o perfil definido

**Extensões:**

- **2a** Se o e-mail já existe, recusar o cadastro
- **\*a** Administrador edita os dados ou o perfil de um funcionário existente, e o sistema atualiza o cadastro
- **\*b** Administrador desativa um funcionário, e o sistema impede que ele entre no sistema

---

### UC04 — Cadastrar e editar aluno

**Ator:** Funcionário

**Fluxo normal:**

1. Funcionário informa os dados do aluno, incluindo o CPF
2. Sistema valida os dados
3. Sistema registra o aluno
4. Sistema informa que o aluno foi cadastrado e passa a exibi-lo nas consultas

**Extensões:**

- **2a** Se o CPF já está cadastrado, recusar o cadastro
- **\*a** Funcionário consulta e edita os dados de um aluno existente, e o sistema atualiza o cadastro
- **\*b** Funcionário marca o aluno como estudante mediante comprovação por matrícula ou carteirinha da instituição de ensino ou do governo, e o sistema registra essa condição

**Observação:** a condição de estudante é necessária para o desconto do UC13.

---

### UC05 — Arquivar aluno

**Ator:** Funcionário

**Pré-condição:** aluno cadastrado.

**Fluxo normal:**

1. Funcionário seleciona o aluno
2. Sistema verifica que o aluno não tem matrícula ativa
3. Sistema arquiva o aluno
4. Sistema retira o aluno das listas comuns, preservando o histórico

**Extensões:**

- **2a** Se o aluno tem matrícula ativa, recusar o arquivamento e informar o motivo

---

### UC06 — Criar plano

**Ator:** Administrador

**Fluxo normal:**

1. Administrador informa nome, duração, preço e tipo do plano (mensal ou diária)
2. Sistema valida os dados
3. Sistema registra o plano
4. Sistema disponibiliza o plano para matrículas

**Extensões:**

- **2a** Se o preço é zero ou negativo, recusar o plano
- **\*a** Administrador consulta os planos existentes, e o sistema os apresenta

---

### UC07 — Criar matrícula

**Ator:** Funcionário

**Pré-condição:** aluno cadastrado e plano disponível.

**Fluxo normal:**

1. Funcionário seleciona o aluno
2. Funcionário seleciona o plano
3. Sistema verifica que o aluno não possui matrícula ativa nem pendente
4. Sistema cria a matrícula no estado "pendente"
5. Sistema informa que a matrícula foi criada

**Extensões:**

- **3a** Se o aluno já tem matrícula ativa ou pendente, recusar a criação e informar o motivo

**Pós-condição:** matrícula no estado "pendente".

**Regras:** RN01.

---

### UC08 — Ativar matrícula

**Ator:** Funcionário

**Pré-condição:** matrícula existente.

**Fluxo normal:**

1. Funcionário seleciona a matrícula
2. Sistema verifica que a matrícula está "pendente"
3. Sistema verifica que há pagamento registrado
4. Sistema altera a matrícula para "ativa"
5. Sistema informa que o acesso do aluno está liberado

**Extensões:**

- **2a** Se a matrícula está em outro estado, recusar a ativação e informar o motivo
- **3a** Se não há pagamento registrado, recusar a ativação

**Pós-condição:** matrícula no estado "ativa".

**Regras:** RN01.

---

### UC09 — Suspender e reativar matrícula

**Ator:** Funcionário

**Propósito:** tratar trancamentos e inadimplência sem perder o histórico do aluno.

**Fluxo normal (suspender):**

1. Funcionário seleciona a matrícula
2. Sistema verifica que a matrícula está "ativa"
3. Sistema altera a matrícula para "suspensa"
4. Sistema informa que a matrícula foi suspensa

**Extensões:**

- **2a** Se a matrícula está "pendente" ou "encerrada", recusar a suspensão e informar o motivo
- **\*a** Funcionário reativa uma matrícula "suspensa", e o sistema a altera para "ativa"
- **\*b** Se a matrícula a reativar não está "suspensa", recusar a reativação e informar o motivo

**Observação:** enquanto a matrícula estiver "suspensa", o aluno não pode ter presença registrada (UC15).

**Regras:** RN01, RN04.

---

### UC10 — Encerrar matrícula

**Ator:** Funcionário

**Propósito:** registrar o cancelamento do aluno.

**Fluxo normal:**

1. Funcionário seleciona a matrícula
2. Sistema verifica que a matrícula está "ativa" ou "suspensa"
3. Sistema altera a matrícula para "encerrada"
4. Sistema preserva o histórico de pagamentos e de frequência
5. Sistema informa que a matrícula foi encerrada

**Extensões:**

- **2a** Se a matrícula está "pendente" ou já "encerrada", recusar o encerramento e informar o motivo (encerrada é estado final)

**Observação:** a matrícula de diária é encerrada automaticamente pelo sistema ao fim do dia do pagamento (RN05, ver UC11).

**Regras:** RN01, RN05.

---

### UC11 — Registrar pagamento

**Ator:** Funcionário

**Pré-condição:** matrícula existente.

**Fluxo normal** (plano mensal, aluno comum):

1. Funcionário seleciona a matrícula do aluno
2. Funcionário informa a data do pagamento
3. Sistema executa <u>Validar data e vencimento</u> (UC12)
4. Sistema determina o valor do plano mensal (R$ 100)
5. Sistema registra o pagamento, com valor final e situação "em dia"
6. Sistema informa o valor e a situação do pagamento

**Extensões:**

- **1a** Se a matrícula está "encerrada", recusar o registro
- **3a** Se a data é inválida, recusar o registro (ver UC12)
- **4a** Se o aluno é estudante e o plano é mensal, executar <u>Aplicar desconto de estudante</u> (UC13), e o valor final é R$ 95
- **4b** Se o plano é diária, o valor é R$ 35 para qualquer aluno, sem desconto
- **5a** Se o plano é mensal e o pagamento ocorre após o vencimento, registrar a situação "em atraso", sem alterar o valor
- **5b** Se o plano é diária, registrar o pagamento sem situação de vencimento, e o sistema encerra a matrícula automaticamente ao fim desse dia

**Pós-condição:** pagamento registrado. A matrícula de diária vale apenas para o dia pago.

**Regras:** RN02, RN03, RN05.

---

### UC12 — Validar data e vencimento

**Ator:** nenhum (caso de uso incluído por UC11)

**Fluxo normal:**

1. Sistema verifica que a data informada é válida e está dentro do período de referência
2. Sistema identifica o vencimento da matrícula mensal
3. Sistema classifica o pagamento como "em dia" (até o vencimento) ou "em atraso" (depois)

**Extensões:**

- **1a** Se a data é vazia ou fora do período de referência, recusar a data e interromper o registro do pagamento
- **2a** Se o plano é diária, não existe vencimento, e o sistema valida apenas a data do pagamento

**Regras:** RN03.

---

### UC13 — Aplicar desconto de estudante

**Ator:** nenhum (extensão de UC11)

**Condição de extensão:** aluno marcado como estudante com plano mensal.

**Fluxo normal:**

1. Sistema verifica a condição de estudante do aluno
2. Sistema aplica o desconto fixo de R$ 5 sobre o valor de R$ 100
3. Sistema devolve ao UC11 o valor final de R$ 95

**Extensões:**

- **1a** Se o aluno não é estudante ou o plano é diária, o desconto não é aplicado

**Regras:** RN02.

---

### UC14 — Alterar data de vencimento

**Ator:** Funcionário

**Pré-condição:** aluno com matrícula de plano mensal.

**Fluxo normal:**

1. Funcionário seleciona a matrícula do aluno
2. Funcionário informa a nova data de vencimento
3. Sistema valida a data
4. Sistema atualiza o vencimento
5. Sistema informa que o vencimento foi alterado

**Extensões:**

- **1a** Se o plano é diária, recusar a alteração, pois não há vencimento
- **3a** Se a data é inválida, recusar a alteração

**Regras:** RN03.

---

### UC15 — Registrar presença

**Ator:** Funcionário

**Pré-condição:** aluno com matrícula cadastrada.

**Fluxo normal:**

1. Funcionário seleciona o aluno
2. Sistema verifica que a matrícula está "ativa"
3. Sistema grava a presença com data e hora
4. Sistema informa que a presença foi registrada

**Extensões:**

- **2a** Se a matrícula não está "ativa" (pendente, suspensa ou encerrada), bloquear o registro e informar o motivo
- **2b** Se a matrícula é de diária e a data não é o dia do pagamento, recusar o registro

**Pós-condição:** presença gravada.

**Regras:** RN04.

---

### UC16 — Associar treino ao aluno

**Ator:** Funcionário

**Pré-condição:** aluno cadastrado.

**Fluxo normal:**

1. Funcionário seleciona o aluno
2. Funcionário informa o treino
3. Sistema verifica que o aluno tem matrícula ativa
4. Sistema associa o treino ao aluno
5. Sistema apresenta o treino na consulta do aluno

**Extensões:**

- **3a** Se o aluno não tem matrícula ativa, recusar a associação e informar o motivo

---

### UC17 — Consultar plano, pagamentos e frequência

**Ator:** Aluno

**Pré-condição:** aluno autenticado.

**Fluxo normal:**

1. Aluno solicita a consulta
2. Sistema identifica o aluno autenticado
3. Sistema apresenta o plano, os pagamentos e a frequência do aluno

**Extensões:**

- **\*a** Se o aluno tenta ver dados de outro aluno, bloquear o acesso

---

### UC18 — Consultar histórico de pagamentos de um aluno

**Ator:** Funcionário

**Propósito:** resolver dúvidas de cobrança.

**Fluxo normal:**

1. Funcionário seleciona o aluno
2. Sistema apresenta os pagamentos em ordem de data, com valor, desconto e situação (em dia ou em atraso)

**Extensões:**

- **2a** Se o aluno não possui pagamentos, informar que não há registros

---

### UC19 — Ver relatórios gerenciais

**Ator:** Administrador

**Propósito:** apoiar decisões da gestão.

**Fluxo normal:**

1. Administrador solicita o relatório
2. Sistema apresenta a quantidade e a lista de alunos ativos, de matrículas pendentes e de inadimplentes

**Extensões:**

- **2a** Se uma matrícula mensal ativa tem vencimento vencido sem pagamento registrado, listar o aluno como inadimplente
- **\*a** Se um funcionário ou aluno tenta acessar os relatórios, bloquear o acesso

**Regras:** RN03.

---


