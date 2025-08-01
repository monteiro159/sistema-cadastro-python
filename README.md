# 💻 Sistema de Cadastro de Usuários em Python

Este é um projeto de aplicação de console completo, desenvolvido em Python, que simula um sistema de gerenciamento de usuários com funcionalidades de CRUD (Create, Read, Update, Delete), autenticação segura e muito mais. O projeto foi estruturado seguindo boas práticas de engenharia de software para garantir manutenibilidade e escalabilidade.

---

## ✨ Funcionalidades

-   [1] **Autenticação Segura:** Sistema de Login com senhas criptografadas usando hashing com `bcrypt`.
-   [2] **CRUD Completo:** Crie, Liste, Atualize e Delete usuários no banco de dados.
-   [3] **Busca Inteligente:** Filtre usuários por nome ou parte do nome.
-   [4] **Interface Rica:** Interface de linha de comando (CLI) bonita e intuitiva, construída com a biblioteca `rich`.
-   [5] **Validação de Dados:** Validação de formato de email com Expressões Regulares (Regex) e tratamento de erros de entrada do usuário.
-   [6] **Exportação de Dados:** Exporte a lista completa de usuários para um arquivo `.csv` padrão.
-   [7] **Ambiente Virtual:** Projeto configurado com um ambiente virtual (`.venv`) para gerenciar dependências de forma isolada.

---

## 🚀 Tecnologias Utilizadas

-   **Python 3**
-   **SQLite 3** (para o banco de dados)
-   **rich** (para a interface de console)
-   **bcrypt** (para hashing de senhas)

---

## 🔧 Como Executar o Projeto

Para rodar este projeto em sua máquina local, siga os passos abaixo:

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/monteiro159/sistema-cadastro-python.git
    ```

2.  **Navegue até a pasta do projeto:**
    ```bash
    cd cadastro_projeto
    ```

3.  **Crie e ative o ambiente virtual:**
    ```bash
    # Crie o ambiente
    python -m venv .venv

    # Ative o ambiente (Windows)
    .\.venv\Scripts\Activate.ps1

    # Ative o ambiente (Linux/macOS)
    source .venv/bin/activate
    ```

4.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Execute a aplicação:**
    ```bash
    python app/main.py
    ```