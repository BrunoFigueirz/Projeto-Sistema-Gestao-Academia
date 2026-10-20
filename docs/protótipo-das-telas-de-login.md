# Protótipo da tela de login — Sistema de Gestão de Academia

Protótipo de baixa fidelidade da tela de **login**. Serve para validar o fluxo de entrada no sistema com a equipe e como base para a implementação em Flask.

- **Arquivo navegável:** [`prototipos/prototipo.html`](prototipos/prototipo.html) (abrir no navegador, sem instalar nada)
- **Capturas de tela:** pasta [`prototipos/`](prototipos/)
- **Caso de uso relacionado:** UC01 (Entrar no sistema), descrito em [`casos-de-uso.md`](casos-de-uso.md)

## Como usar o protótipo

1. Abra o arquivo `prototipo.html` no navegador.
2. Entre com uma das contas de demonstração (senha de todas: `123`). Os botões abaixo do formulário preenchem os campos automaticamente.

| Perfil | E-mail |
|---|---|
| Aluno | `aluno@academia.com` |
| Funcionário | `funcionario@academia.com` |
| Administrador | `admin@academia.com` |

## Tela de login (UC01)

![Tela de login](prototipos/01-login.png)

- Campos de e-mail e senha (com o texto da senha oculto) e botão "Entrar".
- Com credenciais inválidas, a tela mostra uma mensagem única, sem informar qual dado está errado (critério da US01).

![Login com credenciais inválidas](prototipos/02-login-erro.png)

- Com credenciais válidas, o protótipo apenas confirma o acesso e o perfil identificado. A tela inicial de cada perfil será prototipada na próxima etapa.
- Não há "Esqueci a senha" nem "Cadastre-se": nenhuma história de usuário pede isso, e os acessos são criados pelo Administrador (UC03).

## Rastreabilidade

| Tela | Caso de uso | História |
|---|---|---|
| Login | UC01 | US01 |

## Limitações

- Os e-mails e a senha são fictícios, e a autenticação é simulada no navegador, sem banco de dados.
- O protótipo só mostra a aparência. Na implementação em Flask, a senha deve ser armazenada com hash, e cada rota deve verificar o perfil no servidor e bloquear o acesso não autorizado (US01).

## Estrutura de arquivos sugerida no repositório

```
docs/
├── casos-de-uso.md
├── prototipo.md
└── prototipos/
    ├── prototipo.html
    ├── 01-login.png
    └── 02-login-erro.png
```
