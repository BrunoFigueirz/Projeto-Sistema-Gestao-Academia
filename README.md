# Sistema de Gestão de Academia

Projeto da disciplina **Análise e Projeto de Sistemas** (professor Anthony Irlan Marques Luz).

## Tema

Sistema web para gerenciar uma academia: alunos, funcionários, planos, matrículas, pagamentos, treinos e frequência. Três perfis de acesso: **Administrador**, **Funcionário** e **Aluno**.

## Integrantes

| Nome | Papel | GitHub |
|---|---|---|
| Bruno | PO e desenvolvedor | @BrunoFigueirz |
| Kaio | Desenvolvedor (infraestrutura e repositório) | @kaiodrigues3-art |
| Iohan | Desenvolvedor (modelagem UML) |@iohanbryandev |
| Inacio| Desenvolvedor (especificação e interface) | @InacioThiago |

## Tecnologias

- Python 3 e Flask
- SQLite (banco local, criado pelo próprio sistema)
- HTML, CSS e JavaScript nas telas
- Git e GitHub (issues e GitHub Projects como Product Backlog)



## Estrutura do projeto

```
Projeto-Sistema-Gestao-Academia/
├── README.md
├── requirements.txt
├── .github/ISSUE_TEMPLATE/     template de história de usuário
├── docs/
│   ├── historias-de-usuario.md
│   ├── casos-de-uso.md
│   └── diagramas/              diagramas (.png e arquivo-fonte)
└── Sistema-Academia/
    ├── app.py                  inicia a aplicação
    ├── rotas/                  rotas (blueprints) por área
    ├── dados/                  acesso ao banco de dados
    ├── templates/              páginas HTML
    └── static/                 CSS e JavaScript
```

## Instruções de Execução

- A partir da raiz do projeto, use o seguinte comando: ./.venv/bin/python ./Sistema-Academia/app.py
- Abra o link local que aparecer no terminal no navegador




## Documentação

- [Histórias de usuário](docs/historias-de-usuario.md)
- [Casos de uso](docs/casos-de-uso.md)
- [Diagrama de casos de uso](docs/diagramas/casos-de-uso.png)
- Product Backlog: aba **Projects** do repositório
