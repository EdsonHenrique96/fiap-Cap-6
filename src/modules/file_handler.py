import json
from typing import List, Dict

def exportar_para_json(dados: List[Dict], nome_arquivo: str):
    """
    Exporta os dados para um arquivo JSON
    
    Args:
        dados: Lista de dicionários com os dados a serem exportados
        nome_arquivo: Nome do arquivo JSON a ser gerado
    """
    with open(nome_arquivo, 'w') as arquivo:
        json.dump(dados, arquivo, indent=4)
    print(f"Dados exportados para {nome_arquivo}") 