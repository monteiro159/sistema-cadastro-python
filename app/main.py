# Código completo e final para o arquivo app/main.py

import database
import interface
import os
import utils
from rich.console import Console

# --- Funções Auxiliares ---
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# --- Menus da Aplicação ---
def menu_principal(conexao):
    """Loop do menu principal de CRUD, acessível após o login."""
    while True:
        limpar_tela()
        opcao = interface.exibir_menu()
        
        if opcao == '1': # CADASTRAR NOVO USUÁRIO (pelo admin logado)
            nome, email, senha = interface.obter_dados_usuario()
            if not nome or not email or not senha:
                interface.exibir_mensagem("Todos os campos são obrigatórios.", tipo="erro")
            elif database.cadastrar_usuario(conexao, nome, email, senha):
                interface.exibir_mensagem("Usuário cadastrado com sucesso!", tipo="sucesso")
            else:
                interface.exibir_mensagem("Erro: O email já está cadastrado.", tipo="erro")
            input("\nPressione Enter para continuar...")

        elif opcao == '2': # LISTAR TODOS OS USUÁRIOS
            usuarios = database.listar_usuarios(conexao)
            interface.mostrar_lista_usuarios(usuarios)
            input("\nPressione Enter para continuar...")
            
        elif opcao == '3': # BUSCAR USUÁRIO POR NOME
            termo = interface.obter_termo_busca()
            usuarios_encontrados = database.buscar_usuarios_por_nome(conexao, termo)
            interface.exibir_mensagem(f"Exibindo resultados para a busca: '{termo}'")
            interface.mostrar_lista_usuarios(usuarios_encontrados)
            input("\nPressione Enter para continuar...")

        elif opcao == '4': # ATUALIZAR USUÁRIO
            try:
                id_user = int(interface.obter_id_usuario("atualizar"))
                if database.verificar_existencia_usuario(conexao, id_user):
                    # No update, a senha é opcional. Se vazia, não a altera.
                    nome, email, senha = interface.obter_dados_usuario_para_update() 
                    if not nome or not email:
                        interface.exibir_mensagem("Nome e Email não podem ser vazios.", tipo="erro")
                    elif database.atualizar_usuario(conexao, id_user, nome, email, senha):
                        interface.exibir_mensagem("Usuário atualizado com sucesso!", tipo="sucesso")
                    else:
                        interface.exibir_mensagem("Erro: Novo email já cadastrado por outro usuário.", tipo="erro")
                else:
                    interface.exibir_mensagem(f"Erro: Usuário com ID {id_user} não encontrado.", tipo="erro")
            except ValueError:
                interface.exibir_mensagem("Erro: O ID deve ser um número.", tipo="erro")
            input("\nPressione Enter para continuar...")

        elif opcao == '5': # DELETAR USUÁRIO
            try:
                id_user = int(interface.obter_id_usuario("deletar"))
                if database.verificar_existencia_usuario(conexao, id_user):
                    if interface.pedir_confirmacao(f"deletar o usuário com ID {id_user}"):
                        database.deletar_usuario(conexao, id_user)
                        interface.exibir_mensagem("Usuário deletado com sucesso!", tipo="sucesso")
                    else:
                        interface.exibir_mensagem("Operação cancelada.", tipo="aviso")
                else:
                    interface.exibir_mensagem(f"Erro: Usuário com ID {id_user} não encontrado.", tipo="erro")
            except ValueError:
                interface.exibir_mensagem("Erro: O ID deve ser um número.", tipo="erro")
            input("\nPressione Enter para continuar...")
                
        elif opcao == '6': # EXPORTAR PARA CSV
            nome_arquivo = interface.obter_nome_arquivo_csv()
            if not nome_arquivo:
                interface.exibir_mensagem("Nome do arquivo não pode ser vazio.", tipo="erro")
            else:
                usuarios = database.listar_usuarios(conexao)
                if utils.exportar_para_csv(usuarios, nome_arquivo):
                    interface.exibir_mensagem(f"Dados exportados com sucesso para '{nome_arquivo}.csv'!", tipo="sucesso")
                else:
                    interface.exibir_mensagem("Ocorreu um erro ao exportar o arquivo.", tipo="erro")
            input("\nPressione Enter para continuar...")

        elif opcao == '7': # LOGOUT
            interface.exibir_mensagem("Fazendo logout...", tipo="aviso")
            break # Quebra o loop do menu principal e volta para a tela de login
        else:
            interface.exibir_mensagem("Opção inválida. Tente novamente.", tipo="erro")
            input("\nPressione Enter para continuar...")

def main():
    """Loop principal da aplicação, controla a tela de login inicial."""
    conexao = database.conectar_bd()
    database.criar_tabela_usuarios(conexao)
    
    while True:
        limpar_tela()
        console.print("--- BEM-VINDO AO SISTEMA DE CADASTRO MONTEIRO ---", style="bold blue")
        console.print("1 - Fazer Login")
        console.print("2 - Cadastrar Novo Usuário")
        console.print("3 - Sair do Programa")
        opcao_inicial = input("Escolha uma opção: ")

        if opcao_inicial == '1':
            email, senha = interface.obter_credenciais_login()
            if database.verificar_login(conexao, email, senha):
                interface.exibir_mensagem("Login realizado com sucesso!", tipo="sucesso")
                input("\nPressione Enter para acessar o sistema...")
                menu_principal(conexao) # Entra no menu CRUD
            else:
                interface.exibir_mensagem("Email ou senha incorretos.", tipo="erro")
                input("\nPressione Enter para continuar...")

        elif opcao_inicial == '2':
            nome, email, senha = interface.obter_dados_usuario()
            if not nome or not email or not senha:
                interface.exibir_mensagem("Todos os campos são obrigatórios.", tipo="erro")
            elif database.cadastrar_usuario(conexao, nome, email, senha):
                 interface.exibir_mensagem("Usuário cadastrado com sucesso! Agora você pode fazer login.", tipo="sucesso")
            else:
                 interface.exibir_mensagem("Erro: O email já está cadastrado.", tipo="erro")
            input("\nPressione Enter para continuar...")

        elif opcao_inicial == '3':
            interface.exibir_mensagem("Saindo do programa. Até mais!", tipo="sucesso")
            break
        else:
            interface.exibir_mensagem("Opção inválida.", tipo="erro")
            input("\nPressione Enter para continuar...")

    conexao.close()

console = Console()

if __name__ == "__main__":
    main()