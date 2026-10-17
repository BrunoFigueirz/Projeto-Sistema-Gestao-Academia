# Documento de Casos de Uso — Sistema de Gestão de Academia

> **Status:** rascunho. A lista de casos de uso deve ser conferida contra o diagrama em `docs/diagramas/casos-de-uso.puml`. Se houver diferença, o diagrama e este documento precisam ser ajustados juntos.

## 1. Visão geral do sistema

O Sistema de Gestão de Academia é uma aplicação web com banco de dados local SQLite que organiza alunos, funcionários, planos, matrículas, pagamentos, treinos e frequência de uma academia. O funcionário cadastra alunos, gerencia o ciclo de vida das matrículas (pendente, ativa, suspensa e encerrada), registra pagamentos do plano mensal (R$ 100, ou R$ 95 para estudantes) e da diária (R$ 35) e registra a presença. O administrador, além de tudo o que o funcionário faz, gerencia funcionários e planos e consulta relatórios gerenciais. O aluno acessa o sistema para consultar seu plano, seus pagamentos e sua frequência. Todo acesso exige autenticação e é limitado ao perfil do usuário.

## 2. Atores

| Ator | Descrição |
|---|---|
| **Aluno** | Acessa o próprio perfil para consultar plano, pagamentos e frequência, e pode alterar a própria senha. Seu acesso é restrito exclusivamente às informações e funcionalidades do seu perfil. |
| **Funcionário** | Responsável pela operação da academia. Cadastra, edita e arquiva alunos; cria, ativa, suspende, reativa e encerra matrículas; registra pagamentos e altera vencimentos; registra presença; associa treinos; e consulta o histórico de pagamentos. |
| **Administrador** | Especialização do Funcionário: possui todas as permissões dele e, além delas, gerencia funcionários e perfis, cria planos e visualiza e emite os relatórios gerenciais. |

No diagrama, o Administrador se liga ao Funcionário por **generalização**. Por isso, os casos de uso do Funcionário não precisam ser ligados também ao Administrador.

## 3. Lista de casos de uso

| ID | Caso de uso | Ator principal | Histórias de origem | Issues |
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
| UC12 | Alterar data de vencimento | Funcionário | US09 | #11 |
| UC13 | Registrar presença | Funcionário | US10 | #12 |
| UC14 | Consultar plano, pagamentos e frequência | Aluno | US11 | #13 |
| UC15 | Consultar histórico de pagamentos de um aluno | Funcionário | US14 | #16 |
| UC16 | Associar treino ao aluno | Funcionário | US13 | #15 |
| UC17 | Gerar relatórios gerenciais | Administrador | US12 | #14 |
| UC18 | Validar vencimento | (incluído por UC11) | US09 | #11 |

**Conferência dos mínimos da disciplina**

- Atores: 3 (mínimo 3)
- Casos de uso: 18 (mínimo 12, teto sugerido 20)
- Casos de uso de CRUD puro: 5 a 6 (UC03, UC04, UC05, UC06 e talvez UC12), no máximo metade
- Entidade com ciclo de vida de 4 estados: Matrícula (UC07 a UC10)
- Regras de negócio com cálculo ou validação: desconto e valor da diária (RN02), vencimento (RN03), presença só em matrícula ativa (RN04), diária (RN05)
- Autenticação com perfis: UC01

## 4. Relações entre casos de uso

Sugestões para conferir no diagrama. Use `<<include>>` e `<<extend>>` somente onde a relação existe de fato.

| Relação | Justificativa |
|---|---|
| UC11 `<<include>>` UC18 | Todo pagamento de plano mensal passa pela validação de vencimento |
| Administrador → Funcionário (generalização) | O administrador herda todos os casos de uso do funcionário |

## 5. Regras de negócio relacionadas

| ID | Regra | Casos de uso |
|---|---|---|
| RN01 | Ciclo de vida da matrícula: pendente → ativa ⇄ suspensa → encerrada | UC07, UC08, UC09, UC10 |
| RN02 | Plano mensal: R$ 100 (aluno comum) ou R$ 95 (estudante). Diária: R$ 35, sem desconto | UC11 |
| RN03 | Vencimento atrelado ao dia da matrícula; pagamento "em dia" ou "em atraso"; inadimplente é a matrícula mensal ativa com vencimento vencido e sem pagamento | UC11, UC12, UC18, UC17 |
| RN04 | Presença só em matrícula "ativa" (na diária, só no dia pago) | UC13 |
| RN05 | Matrícula de diária vale só no dia do pagamento e é encerrada ao fim dele | UC11, UC10 |

## 6. Especificação dos casos de uso

Cada caso de uso será detalhado no **modelo de especificação do livro didático** apresentado em sala. Pendências:

| ID | Caso de uso | Responsável | Status |
|---|---|---|---|
| UC11 | Registrar pagamento | P4 | A fazer |
| UC08 | Ativar matrícula | P4 | A fazer |
| UC13 | Registrar presença | P4 | A fazer |
| Demais | | P4 | A fazer |
