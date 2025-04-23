#!/usr/bin/env python3
"""
Script para executar as migrações do banco de dados.
"""

import sys
import os

# Adicionar o diretório atual ao PATH para importação de módulos
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from modules.db_handler import conectar_bd, executar_migracoes

def main():
    print("=== Executando Migrações do Banco de Dados ===")
    
    # Conectar ao banco de dados
    conexao = conectar_bd()
    if not conexao:
        print("Erro: Não foi possível conectar ao banco de dados.")
        sys.exit(1)
    
    # Executar migrações
    migrations_dir = os.path.join(os.path.dirname(__file__), '..', 'config', 'migrations')
    sucesso = executar_migracoes(conexao, migrations_dir)
    
    # Fechar conexão
    conexao.close()
    
    if sucesso:
        print("Todas as migrações foram executadas com sucesso!")
        sys.exit(0)
    else:
        print("Erros ocorreram durante a execução das migrações.")
        sys.exit(1)

if __name__ == "__main__":
    main() 