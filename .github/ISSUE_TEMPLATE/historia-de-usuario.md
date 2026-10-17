# Histórias de Usuário

## 1. Backlog

Ordenado por prioridade (MoSCoW). A coluna UC é preenchida quando a lista de casos de uso estiver pronta.

| ID | História | Ator | Origem | Prioridade | UC |
|---|---|---|---|---|---|
| US01 | Entrar no sistema com perfil | Administrador, Funcionário, Aluno | RF01 | Must | |
| US02 | Gerenciar funcionários e perfis | Administrador | RF08 | Must | |
| US03 | Cadastrar e editar alunos | Funcionário | RF02 | Must | |
| US04 | Criar planos | Administrador | RF03 | Must | |
| US05 | Criar matrícula | Funcionário | RF04, RN01 | Must | |
| US06 | Ativar matrícula | Funcionário | RF04, RN01 | Must | |
| US07 | Suspender e reativar matrícula | Funcionário | RF04, RN01 | Must | |
| US08 | Encerrar matrícula | Funcionário | RF04, RN01 | Must | |
| US09 | Registrar pagamento com desconto e validação de vencimento | Funcionário | RF05, RN02, RN03 | Must | |
| US10 | Registrar presença | Funcionário | RF06 | Must | |
| US11 | Consultar plano, pagamentos e frequência | Aluno | RF01, RF05, RF06 | Must | |
| US12 | Ver relatórios gerenciais | Administrador | RF07 | Must | |
| US13 | Associar treino ao aluno | Funcionário | RF06 | Should | |
| US14 | Consultar histórico de pagamentos de um aluno | Funcionário | RF05 | Should | |
| US15 | Arquivar aluno | Funcionário | RF02 | Should | |
| US16 | Trocar a própria senha | Todos os perfis | RF01 | Could | |

## 2. Atores

**Aluno:** acessa o próprio perfil para consultar plano, pagamentos e frequência, e pode alterar a própria senha. Seu acesso é restrito exclusivamente às informações e funcionalidades do seu perfil.

**Funcionário:** acessa o próprio perfil e é responsável pela operação da academia. Cadastra, edita e arquiva alunos; cria, ativa, suspende, reativa e encerra matrículas; registra pagamentos (planos mensal e diária, com desconto de estudante e validação de vencimento) e altera datas de vencimento; registra a presença e acompanha a frequência dos alunos; associa treinos aos alunos; e consulta o histórico de pagamentos deles.

**Administrador:** possui todas as permissões do funcionário e, além delas, tem acesso exclusivo para gerenciar funcionários e perfis, criar planos, e visualizar e emitir os relatórios gerenciais da academia. No diagrama de casos de uso, o Administrador é uma especialização do Funcionário.

## 3. Regras de negócio

| ID | Regra | Descrição |
|---|---|---|
| RN01 | Ciclo de vida da matrícula | Estados: pendente, ativa, suspensa e encerrada. Transições permitidas: pendente→ativa, ativa→suspensa, suspensa→ativa, ativa→encerrada e suspensa→encerrada. "Encerrada" é estado final. |
| RN02 | Valor do pagamento | Plano mensal: aluno comum paga R$ 100 e aluno estudante paga R$ 95 (desconto fixo de R$ 5). Plano diária: R$ 35 para todos, sem desconto. |
| RN03 | Vencimento | Vale para o plano mensal. O vencimento é atrelado ao dia da matrícula e pode ser alterado. Todo pagamento é "em dia" (até o vencimento) ou "em atraso" (depois). Data inválida é recusada. Inadimplente é o aluno com matrícula mensal ativa cujo vencimento passou sem pagamento registrado. |
| RN04 | Presença | A presença só pode ser registrada em matrícula "ativa". Na diária, só no dia pago. |
| RN05 | Diária | A matrícula de diária vale apenas para o dia do pagamento e é encerrada automaticamente ao fim desse dia. |

## 4. Histórias de usuário

### US01 — Entrar no sistema com perfil

Como **administrador, funcionário ou aluno**, quero entrar no sistema com e-mail e senha, para acessar apenas as funções do meu perfil.

- [ ] Dado e-mail e senha válidos, quando eu entro, então vejo a tela inicial do meu perfil.
- [ ] Dado credenciais inválidas, quando eu tento entrar, então o sistema recusa sem dizer qual campo errou.
- [ ] Dado um perfil sem permissão, quando eu tento acessar uma tela restrita, então o sistema bloqueia no backend, não só na tela.
- [ ] A senha é armazenada com hash.
- [ ] Posso encerrar a sessão.

**Origem:** RF01 · **Prioridade:** Must

### US02 — Gerenciar funcionários e perfis

Como **administrador**, quero cadastrar funcionários e definir o perfil de cada um, para controlar quem pode fazer o quê.

- [ ] Dados válidos, quando eu cadastro um funcionário, então ele consegue entrar com o perfil definido.
- [ ] Dado um e-mail já existente, quando eu tento cadastrar, então o sistema recusa.
- [ ] Posso editar e desativar um funcionário.

**Origem:** RF08 · **Prioridade:** Must

### US03 — Cadastrar e editar alunos

Como **funcionário**, quero cadastrar e editar alunos, para manter a base atualizada.

- [ ] Dados válidos, quando eu cadastro, então o aluno aparece na consulta.
- [ ] Dado um documento (CPF) já cadastrado, quando eu tento cadastrar, então o sistema recusa.
- [ ] Posso consultar e editar os dados de um aluno.
- [ ] Posso marcar o aluno como estudante mediante comprovação por matrícula ou carteirinha da instituição de ensino ou do governo.
- [ ] A condição de estudante é necessária para o desconto da US09.

**Origem:** RF02 · **Prioridade:** Must

### US04 — Criar planos

Como **administrador**, quero criar planos com duração e preço, para oferecer opções de matrícula.

- [ ] Dados nome, duração, preço e tipo (mensal ou diária) válidos, quando eu salvo, então o plano fica disponível para matrículas.
- [ ] Preço zero ou negativo é recusado.
- [ ] Posso consultar os planos existentes.

**Origem:** RF03 · **Prioridade:** Must

### US05 — Criar matrícula

Como **funcionário**, quero criar uma matrícula para um aluno em um plano, para formalizar a entrada dele.

- [ ] Dado um aluno e um plano, quando eu crio a matrícula, então ela nasce como "pendente".
- [ ] Dado um aluno que já tem matrícula ativa ou pendente, quando eu tento criar outra, então o sistema recusa.

**Origem:** RF04, RN01 · **Prioridade:** Must

### US06 — Ativar matrícula

Como **funcionário**, quero ativar a matrícula após o primeiro pagamento, para liberar o acesso do aluno.

- [ ] Dada uma matrícula "pendente" com pagamento registrado, quando eu ativo, então ela passa para "ativa".
- [ ] Dada uma matrícula em outro estado, quando eu tento ativar, então o sistema recusa e informa o motivo.
- [ ] Dada uma matrícula sem pagamento, quando eu tento ativar, então o sistema recusa.

**Origem:** RF04, RN01 · **Prioridade:** Must

### US07 — Suspender e reativar matrícula

Como **funcionário**, quero suspender e reativar a matrícula de um aluno, para tratar trancamentos e inadimplência sem perder o histórico dele.

- [ ] Dada uma matrícula "ativa", quando eu suspendo, então ela passa para "suspensa".
- [ ] Dada uma matrícula "suspensa", quando eu reativo, então ela volta para "ativa".
- [ ] Dada uma matrícula "pendente" ou "encerrada", quando eu tento suspender, então o sistema recusa e informa o motivo.
- [ ] Enquanto estiver "suspensa", o aluno não consegue ter presença registrada.

**Origem:** RF04, RN01 · **Prioridade:** Must

### US08 — Encerrar matrícula

Como **funcionário**, quero encerrar uma matrícula, para registrar o cancelamento do aluno.

- [ ] Dada uma matrícula "ativa" ou "suspensa", quando eu encerro, então ela passa para "encerrada".
- [ ] Dada uma matrícula "encerrada", quando eu tento qualquer transição, então o sistema recusa (estado final).
- [ ] O histórico de pagamentos e frequência é preservado.

**Origem:** RF04, RN01 · **Prioridade:** Must

### US09 — Registrar pagamento com desconto e validação de vencimento

Como **funcionário**, quero registrar um pagamento aplicando o desconto de estudante quando houver direito e validando o vencimento, para cobrar o valor correto de cada plano e saber quem está em atraso.

- [ ] Dado um aluno comum com plano mensal, quando eu registro o pagamento, então o valor final é R$ 100 e nenhum desconto é aplicado.
- [ ] Dado um aluno marcado como estudante com plano mensal, quando eu registro o pagamento, então o valor final é R$ 95 (desconto fixo de R$ 5 sobre os R$ 100).
- [ ] Dado um pagamento de plano diária, quando eu registro, então o valor final é R$ 35 para qualquer aluno, sem desconto de estudante.
- [ ] Dada uma matrícula de diária com pagamento registrado, então ela vale apenas para o dia pago e passa para "encerrada" automaticamente ao fim desse dia.
- [ ] A data de vencimento do plano mensal é atrelada ao dia da matrícula do aluno.
- [ ] Posso alterar a data de vencimento de um aluno quando necessário.
- [ ] Dado um pagamento de plano mensal registrado até a data de vencimento, quando eu registro, então ele fica como "em dia".
- [ ] Dado um pagamento de plano mensal registrado após o vencimento, quando eu registro, então ele fica como "em atraso", sem alterar o valor.
- [ ] Dada uma data inválida (vazia ou fora do período de referência), quando eu tento registrar, então o sistema recusa.
- [ ] Dada uma matrícula "encerrada", quando eu tento registrar, então o sistema recusa.

**Origem:** RF05, RN02, RN03 · **Prioridade:** Must

### US10 — Registrar presença

Como **funcionário**, quero registrar a presença do aluno, para acompanhar a frequência.

- [ ] Dada uma matrícula "ativa", quando eu registro, então a presença fica gravada com data e hora.
- [ ] Dada uma matrícula que não esteja "ativa", quando eu tento registrar, então o sistema bloqueia e informa o motivo.
- [ ] Dada uma matrícula de diária, quando eu registro, então a presença só é aceita no dia do pagamento.

**Origem:** RF06 · **Prioridade:** Must

### US11 — Consultar plano, pagamentos e frequência

Como **aluno**, quero consultar meu plano, meus pagamentos e minha frequência, para acompanhar minha situação.

- [ ] Dado que estou logado como aluno, quando eu consulto, então vejo apenas os meus dados.
- [ ] Dado outro aluno, quando eu tento ver os dados dele, então o sistema bloqueia.

**Origem:** RF01, RF05, RF06 · **Prioridade:** Must

### US12 — Ver relatórios gerenciais

Como **administrador**, quero ver relatórios de alunos ativos, matrículas pendentes e inadimplentes, para tomar decisões.

- [ ] Dados cadastrados, quando eu abro o relatório, então vejo as quantidades e a lista de cada grupo.
- [ ] Dada uma matrícula ativa cujo vencimento passou sem pagamento registrado, quando eu abro o relatório, então o aluno aparece como inadimplente.
- [ ] Um funcionário ou aluno não consegue acessar os relatórios.

**Origem:** RF07 · **Prioridade:** Must

### US13 — Associar treino ao aluno

Como **funcionário**, quero associar um treino a um aluno, para orientar a rotina dele.

- [ ] Dado um aluno com matrícula ativa, quando eu associo um treino, então ele aparece na consulta do aluno.

**Origem:** RF06 · **Prioridade:** Should

### US14 — Consultar histórico de pagamentos de um aluno

Como **funcionário**, quero ver o histórico de pagamentos de um aluno, para resolver dúvidas de cobrança.

- [ ] Dado um aluno, quando eu consulto, então vejo os pagamentos em ordem de data, com valor, desconto e situação (em dia ou em atraso).

**Origem:** RF05 · **Prioridade:** Should

### US15 — Arquivar aluno

Como **funcionário**, quero arquivar um aluno, para tirá-lo das listas sem apagar o histórico.

- [ ] Dado um aluno sem matrícula ativa, quando eu arquivo, então ele some das listas comuns.
- [ ] Dado um aluno com matrícula ativa, quando eu tento arquivar, então o sistema recusa.

**Origem:** RF02 · **Prioridade:** Should

### US16 — Trocar a própria senha

Como **administrador, funcionário ou aluno**, quero trocar minha senha, para manter minha conta segura.

- [ ] Dada a senha atual correta, quando eu informo uma nova válida, então ela é atualizada com hash.
- [ ] Dada a senha atual errada, quando eu tento trocar, então o sistema recusa.

**Origem:** RF01 · **Prioridade:** Could
