import sqlite3
import bcrypt

# ESTA É A FUNÇÃO QUE ESTÁ FALTANDO. VERIFIQUE SE ELA ESTÁ EXATAMENTE ASSIM.
def conectar_bd():
    """Cria a conexão com o banco de dados SQLite."""
    conexao = sqlite3.connect('meu_banco.db')
    # Importante: O banco será criado na pasta raiz do projeto (cadastro_projeto)
    # Se quiser que ele seja criado dentro de 'app', use: sqlite3.connect('app/meu_banco.db')
    return conexao

def criar_tabela_usuarios(conexao):
    """Cria a tabela 'usuarios' com o novo campo 'senha_hash'."""
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            senha_hash TEXT NOT NULL
        );
    """)
    conexao.commit()

def cadastrar_usuario(conexao, nome, email, senha):
    """Insere um novo usuário com a senha hasheada."""
    cursor = conexao.cursor()

    # Gera o hash da senha
    senha_bytes = senha.encode('utf-8')
    senha_hash = bcrypt.hashpw(senha_bytes, bcrypt.gensalt())

    try:
        # Insere o hash decodificado como string no banco
        cursor.execute(
            "INSERT INTO usuarios (nome, email, senha_hash) VALUES (?, ?, ?);",
            (nome, email, senha_hash.decode('utf-8'))
        )
        conexao.commit()
        return True
    except sqlite3.IntegrityError:
        return False

def listar_usuarios(conexao):
    """Retorna uma lista de todos os usuários cadastrados."""
    cursor = conexao.cursor()
    cursor.execute("SELECT id, nome, email FROM usuarios;")
    return cursor.fetchall()

def atualizar_usuario(conexao, id_usuario, novo_nome, novo_email):
    """Atualiza o nome e o email de um usuário específico."""
    cursor = conexao.cursor()
    try:
        cursor.execute("""
            UPDATE usuarios 
            SET nome = ?, email = ? 
            WHERE id = ?
        """, (novo_nome, novo_email, id_usuario))
        conexao.commit()
        return cursor.rowcount > 0
    except sqlite3.IntegrityError:
        return False

def deletar_usuario(conexao, id_usuario):
    """Deleta um usuário específico do banco de dados."""
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM usuarios WHERE id = ?", (id_usuario,))
    conexao.commit()
    return cursor.rowcount > 0

def verificar_existencia_usuario(conexao, id_usuario):
    """Verifica se um usuário com o ID especificado existe no banco."""
    cursor = conexao.cursor()
    # Usamos "SELECT 1" por eficiência, não precisamos dos dados, só saber se existe.
    cursor.execute("SELECT 1 FROM usuarios WHERE id = ?", (id_usuario,))
    # fetchone() retornará None se nenhum registro for encontrado, ou uma tupla se encontrar.
    return cursor.fetchone() is not None

def buscar_usuarios_por_nome(conexao, nome_parcial):
    """Busca usuários cujo nome contém o texto fornecido."""
    cursor = conexao.cursor()
    # O sinal de '%' é um coringa no SQL que significa "qualquer sequência de caracteres".
    # Então, '%texto%' busca por qualquer registro que contenha "texto" em qualquer lugar do nome.
    termo_busca = f'%{nome_parcial}%'
    cursor.execute("SELECT id, nome, email FROM usuarios WHERE nome LIKE ?", (termo_busca,))
    return cursor.fetchall()

def verificar_login(conexao, email, senha):
    """Verifica se o email e a senha correspondem a um usuário."""
    cursor = conexao.cursor()
    cursor.execute("SELECT senha_hash FROM usuarios WHERE email = ?", (email,))
    resultado = cursor.fetchone()

    if resultado:
        senha_hash_armazenada = resultado[0].encode('utf-8')
        senha_fornecida_bytes = senha.encode('utf-8')

        # bcrypt.checkpw compara a senha fornecida com o hash do banco
        if bcrypt.checkpw(senha_fornecida_bytes, senha_hash_armazenada):
            return True # Senha correta

    return False # Usuário não encontrado ou senha incorreta