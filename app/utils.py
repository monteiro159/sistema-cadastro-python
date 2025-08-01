import csv

def exportar_para_csv(usuarios, nome_arquivo):
    """
    Exporta uma lista de usuários para um arquivo CSV.
    Retorna True em caso de sucesso, False em caso de erro.
    """
    if not nome_arquivo.lower().endswith('.csv'):
        nome_arquivo += '.csv'
        
    try:
        with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
            # Define o cabeçalho do arquivo
            cabecalho = ['ID', 'NOME', 'EMAIL']
            escritor = csv.writer(arquivo_csv)
            
            # Escreve o cabeçalho
            escritor.writerow(cabecalho)
            
            # Escreve os dados dos usuários
            escritor.writerows(usuarios)
            
        return True
    except IOError:
        # Retorna False se houver um erro de escrita no disco
        return False

def obter_nome_arquivo_csv():
    """Pede ao usuário o nome do arquivo para exportação."""
    return input("Digite o nome do arquivo para salvar (ex: relatorio_usuarios): ")