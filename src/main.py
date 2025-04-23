from dotenv import load_dotenv
import os
import sys
from modules.csv_handler import ler_arquivo_csv
from modules.analyzer import analisar_dados
from modules.file_handler import exportar_para_json
from modules.db_handler import conectar_bd, salvar_dados_bd, executar_migracoes


load_dotenv()
def processar_arquivo(nome_arquivo: str):
    """Processa um arquivo CSV e realiza a análise"""
    # Verificar se o arquivo existe
    if not os.path.exists(nome_arquivo):
        print(f"Erro: Arquivo {nome_arquivo} não encontrado.")
        return
    
    # Ler arquivo
    try:
        tabela = ler_arquivo_csv(nome_arquivo)
        dados = tabela.get_data()
        
        if not dados:
            print("Nenhum dado encontrado no arquivo.")
            return
            
        # Processar dados e obter resultados
        resultados = analisar_dados(dados)
        
        # Exportar para JSON
        nome_json = os.path.splitext(nome_arquivo)[0] + '_resultados.json'
        exportar_para_json(resultados, nome_json)
        
        # Conexão com o banco de dados Oracle
        conexao = conectar_bd()
        if conexao:
            # Executar migrações antes de salvar dados
            migrations_dir = os.path.join(os.path.dirname(__file__), '..', 'config', 'migrations')
            executar_migracoes(conexao, migrations_dir)
            
            # Salvar dados no banco
            salvar_dados_bd(conexao, resultados)
            conexao.close()
            print("Dados salvos no banco de dados Oracle com sucesso!")
        else:
            print("Aviso: Não foi possível conectar ao banco de dados Oracle.")
    
    except Exception as e:
        print(f"Erro ao processar o arquivo: {str(e)}")

if __name__ == "__main__":
    print("==== Sistema de Análise de Maturação de Cana-de-Açúcar ====")
    if len(sys.argv) > 1:
        arquivo = sys.argv[1]
        print(f"Processando arquivo: {arquivo}")
        processar_arquivo(arquivo)
    else:
        arquivo = input("Digite o nome do arquivo CSV a ser processado: ")
        processar_arquivo(arquivo) 