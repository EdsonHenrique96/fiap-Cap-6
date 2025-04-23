import os
from typing import List, Dict

# Carregar variáveis de ambiente do arquivo .env, se existir
try:
    from dotenv import load_dotenv
    load_dotenv()  # carrega variáveis do arquivo .env
except ImportError:
    print("Aviso: Módulo python-dotenv não encontrado. As variáveis de ambiente devem ser definidas manualmente.")

# Tenta importar oracledb, mas não falha se não estiver disponível
try:
    import oracledb
    ORACLE_AVAILABLE = True
except ImportError:
    ORACLE_AVAILABLE = False
    print("Aviso: Módulo oracledb não encontrado. A conexão com o banco de dados Oracle não estará disponível.")

def conectar_bd():
    """
    Conecta ao banco de dados Oracle
    
    Returns:
        Conexão com o banco de dados Oracle ou None em caso de erro
    """
    if not ORACLE_AVAILABLE:
        print("Erro: Módulo oracledb não está instalado. Instale-o com 'pip install oracledb'.")
        return None
        
    try:
        # Obter informações de conexão do ambiente ou usar valores padrão
        host = os.environ.get('ORACLE_HOST', 'localhost')
        port = os.environ.get('ORACLE_PORT', '1521')
        service = os.environ.get('ORACLE_SERVICE', 'xe')
        user = os.environ.get('ORACLE_USER', 'system')
        password = os.environ.get('ORACLE_PASSWORD', 'oracle')
        
        # Verificar se deve usar modo thick (requer Oracle Client)
        use_thick_mode = os.environ.get('ORACLE_THICK_MODE', '').lower() in ('true', '1', 'yes')
        
        # Criar string de conexão
        dsn = f"{host}:{port}/{service}"
        
        if hasattr(oracledb, 'thin'):
            conexao = oracledb.connect(user=user, password=password, dsn=dsn, thin=True)
        else:
            # Versões mais antigas podem não ter parâmetro 'thin'
            # Configura o modo thin globalmente
            oracledb.defaults.config_dir = None
            conexao = oracledb.connect(user=user, password=password, dsn=dsn)
    
        print(f"Conectado ao banco de dados Oracle: {user}@{host}:{port}/{service}")
        return conexao
    except oracledb.Error as erro:
        print(f"Erro ao conectar ao banco de dados Oracle: {erro}")
        return None

def executar_migracao(conexao, arquivo_sql):
    """
    Executa um arquivo de migração SQL
    
    Args:
        conexao: Conexão com o banco de dados Oracle
        arquivo_sql: Caminho do arquivo SQL a ser executado
    """
    if not conexao:
        print(f"Erro: Não é possível executar a migração {arquivo_sql} sem conexão com o banco")
        return False
        
    try:
        print(f"Executando migração: {arquivo_sql}")
        
        # Ler o conteúdo do arquivo SQL
        with open(arquivo_sql, 'r') as f:
            sql = f.read()
            
        # Executar o script SQL
        cursor = conexao.cursor()
        try:
            # Tenta executar o SQL completo
            cursor.execute(sql)
            conexao.commit()
        except Exception as e:
            # Se falhar, tenta executar linha por linha
            print(f"Tentando executar SQL linha por linha devido ao erro: {e}")
            # Executar os comandos um a um
            for comando in sql.split(';'):
                comando = comando.strip()
                if comando and not comando.startswith('--'):
                    try:
                        cursor.execute(comando)
                        conexao.commit()
                    except oracledb.Error as e:
                        if "ORA-00942" in str(e) or "ORA-00955" in str(e):
                            # Ignora erros de "tabela não existe" ou "nome já existe"
                            print(f"  Info: {e}")
                        else:
                            print(f"  Erro ao executar: {comando}")
                            print(f"  Erro: {e}")
                            raise
        
        print(f"Migração {arquivo_sql} executada com sucesso!")
        cursor.close()
        return True
    except Exception as e:
        print(f"Erro ao executar migração {arquivo_sql}: {str(e)}")
        if e.__class__.__module__ == 'oracledb':
            help_url = "https://docs.oracle.com/error-help/db/ora-"
            error_code = str(e).split(':')[0].strip()
            if error_code.startswith('ORA-'):
                error_num = error_code[4:].zfill(5)
                print(f"Consulte: {help_url}{error_num}/")
        return False

def executar_migracoes(conexao, diretorio_migracoes):
    """
    Executa todas as migrações SQL encontradas no diretório especificado
    
    Args:
        conexao: Conexão com o banco de dados Oracle
        diretorio_migracoes: Diretório onde estão os arquivos de migração
        
    Returns:
        True se todas as migrações foram executadas com sucesso, False caso contrário
    """

    
    if not os.path.exists(diretorio_migracoes):
        print(f"Aviso: Diretório de migrações '{diretorio_migracoes}' não encontrado")
        return False
        
    # Listar todos os arquivos .sql no diretório de migrações, ordenados por nome
    arquivos_sql = sorted([os.path.join(diretorio_migracoes, f) 
                          for f in os.listdir(diretorio_migracoes) 
                          if f.endswith('.sql')])
    
    if not arquivos_sql:
        print(f"Aviso: Nenhum arquivo de migração encontrado em '{diretorio_migracoes}'")
        return False
    
    # Executar cada migração
    sucesso = True
    for arquivo in arquivos_sql:
        if not executar_migracao(conexao, arquivo):
            sucesso = False
    
    return sucesso

def salvar_dados_bd(conexao, dados: List[Dict]):
    """
    Salva os dados no banco de dados Oracle
    
    Args:
        conexao: Conexão com o banco de dados Oracle
        dados: Lista de dicionários com os dados a serem salvos
    """
    if not ORACLE_AVAILABLE:
        print("Erro: Módulo oracledb não está instalado. Instale-o com 'pip install oracledb'.")
        return
        
    if not conexao:
        print("Erro: Conexão com o banco de dados não estabelecida")
        return
    
    cursor = conexao.cursor()
    try:
        # Preparar e executar a inserção para cada registro
        for dado in dados:
            # Converter o tipo booleano para 'S' ou 'N'
            deve_colher = 'S' if dado['deve_colher'] else 'N'
            
            cursor.execute("""
                INSERT INTO analise_cana 
                (id_planta, brix_base, brix_meio, brix_topo, media_brix, indice_maturacao, deve_colher, data_leitura)
                VALUES (:1, :2, :3, :4, :5, :6, :7, :8)
            """, (
                dado['id_planta'],
                dado['brix_base'],
                dado['brix_meio'],
                dado['brix_topo'],
                dado['media_brix'],
                dado['indice_maturacao'],
                deve_colher,
                dado['data_leitura']
            ))
        
        conexao.commit()
        print(f"Total de {len(dados)} registros salvos no banco de dados")
    except Exception as erro:
        print(f"Erro ao salvar dados no banco de dados: {erro}")
        if hasattr(conexao, 'rollback'):
            conexao.rollback()
    finally:
        if hasattr(cursor, 'close'):
            cursor.close() 