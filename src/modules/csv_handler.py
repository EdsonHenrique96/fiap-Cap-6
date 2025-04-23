import csv
from typing import List

class MemoryTable:
    def __init__(self):
        self.data = []
        self.columns = []
    
    def set_columns(self, columns: List[str]):
        """Define as colunas da tabela"""
        self.columns = columns
    
    def add_row(self, row: List):
        """Adiciona uma linha de dados à tabela"""
        if len(row) != len(self.columns):
            raise ValueError(f"Row length ({len(row)}) doesn't match columns length ({len(self.columns)})")
        self.data.append(dict(zip(self.columns, row)))
    
    def get_data(self):
        """Retorna todos os dados da tabela"""
        return self.data

def ler_arquivo_csv(nome_arquivo: str) -> MemoryTable:
    """Lê um arquivo CSV e retorna os dados em uma tabela de memória"""
    tabela = MemoryTable()
    
    with open(nome_arquivo, 'r') as arquivo:
        leitor_csv = csv.reader(arquivo)
        colunas = next(leitor_csv)  # Lê o cabeçalho
        tabela.set_columns(colunas)
        
        for linha in leitor_csv:
            if len(linha) == len(colunas):  # Verificar se a linha tem o número correto de campos
                tabela.add_row(linha)
            else:
                print(f"Aviso: Linha ignorada por ter formato inválido: {linha}")
    
    return tabela 