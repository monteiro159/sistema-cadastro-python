# Código completo para o arquivo app/interface.py

from rich.console import Console
from rich.table import Table
import re

console = Console()

def exibir_menu():
    """Mostra o menu de opções CRUD."""
    console.print("\n--- PAINEL DE CONTROLE ---", style="bold cyan")
    print("1 - Cadastrar novo usuário")
    print("2 - Listar todos os usuários")
    print("3 - Buscar usuário por nome")
    print("4 - Atualizar usuário")
    print("5 - Deletar usuário")
    print("6 - Exportar usuários para CSV")
    print("7 - Fazer Logout (Voltar para tela inicial)")
    return input("Escolha uma opção: ")

def obter_dados_usuario():
    """Pede nome, email e senha para um novo cadastro."""
    nome = input("Digite o nome do usuário: ")
    email = obter_email_valido()
    senha = input("Digite uma senha: ")
    return nome, email, senha

def obter_dados_usuario_para_update():
    """Pede os dados para uma atualização. A senha é opcional."""
    nome = input("Digite o NOVO nome do usuário: ")
    email = obter_email_valido("Digite o NOVO email do usuário: ")
    senha = input("Digite a NOVA senha (deixe em branco para não alterar): ")
    return nome, email, senha

def obter_email_valido(prompt="Digite o email do usuário: "):
    """Pede um email ao usuário e valida seu formato até estar correto."""
    padrao_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    while True:
        email = input(prompt)
        if re.match(padrao_email, email):
            return email
        else:
            console.print("Formato de email inválido. Por favor, tente novamente.", style="bold red")

def mostrar_lista_usuarios(usuarios):
    """Exibe uma lista de usuários em uma tabela formatada."""
    tabela = Table(title="Lista de Usuários Cadastrados", show_header=True, header_style="bold magenta")
    tabela.add_column("ID", style="dim", width=5, justify="center")
    tabela.add_column("NOME", style="bold", min_width=20)
    tabela.add_column("EMAIL", min_width=20)
    
    if not usuarios:
        console.print("Nenhum usuário cadastrado ainda.", style="yellow")
    else:
        for usuario in usuarios:
            tabela.add_row(str(usuario[0]), str(usuario[1]), str(usuario[2]))
        console.print(tabela)

def obter_id_usuario(acao):
    """Pede ao usuário o ID para uma ação específica."""
    return input(f"Digite o ID do usuário que você deseja {acao}: ")

def obter_termo_busca():
    """Pede ao usuário o termo para a busca de nome."""
    return input("Digite o nome (ou parte do nome) que deseja buscar: ")

def pedir_confirmacao(acao):
    """Pede confirmação para uma ação destrutiva."""
    confirm = input(f"Tem certeza que deseja {acao} este usuário? [s/n]: ").lower()
    return confirm == 's'

def exibir_mensagem(mensagem, tipo="info"):
    """Exibe uma mensagem formatada de acordo com o tipo."""
    if tipo == "sucesso":
        console.print(f"✅ {mensagem}", style="bold green")
    elif tipo == "erro":
        console.print(f"⚠️ {mensagem}", style="bold red")
    elif tipo == "aviso":
        console.print(f"[!] {mensagem}", style="yellow")
    else:
        console.print(mensagem)

def obter_credenciais_login():
    """Pede o email e a senha para o login."""
    email = input("Email: ")
    senha = input("Senha: ")
    return email, senha