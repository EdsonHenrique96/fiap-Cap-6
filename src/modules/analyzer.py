from typing import List, Dict, Tuple

def calcular_indice_maturacao(brix_base: float, brix_meio: float, brix_topo: float) -> Tuple[float, float, bool]:
    """
    Calcula o índice de maturação e determina se a colheita deve ser feita
    
    Args:
        brix_base: Valor do Brix na base do colmo
        brix_meio: Valor do Brix no meio do colmo
        brix_topo: Valor do Brix no topo do colmo
        
    Returns:
        Tupla contendo (média do Brix, índice de maturação, recomendação de colheita)
    """
    # Cálculo da média de Brix
    media_brix = (brix_base + brix_meio + brix_topo) / 3
    
    # Cálculo do índice de maturação (IM)
    indice_maturacao = (brix_topo / brix_base) * 100
    
    # Critérios para determinar se a colheita deve ser feita
    # 1. Média de Brix > 18
    # 2. IM próximo a 1 (entre 0.95 e 1.05, ou seja, 95% a 105%)
    colheita_por_media = media_brix > 18
    colheita_por_indice = 95 <= indice_maturacao <= 105
    
    deve_colher = colheita_por_media and colheita_por_indice
    
    return media_brix, indice_maturacao, deve_colher

def analisar_dados(dados: List[Dict]) -> List[Dict]:
    """
    Analisa os dados brutos das plantas e retorna os resultados da análise
    
    Args:
        dados: Lista de dicionários com os dados das plantas
        
    Returns:
        Lista de dicionários com os resultados da análise
    """
    resultados = []
    
    for registro in dados:
        # Extrair dados da planta
        id_planta = registro['ID da planta']
        
        # Dividir o valor do Brix em três partes (base, meio, topo)
        try:
            brix_valores = registro['Valor do Brix'].split(';')
            if len(brix_valores) != 3:
                print(f"Erro: Formato inválido para o Brix da planta {id_planta}. Esperado 3 valores separados por ';'.")
                continue
            
            brix_base = float(brix_valores[0])
            brix_meio = float(brix_valores[1])
            brix_topo = float(brix_valores[2])
        except (ValueError, KeyError) as e:
            print(f"Erro ao processar os valores de Brix para a planta {id_planta}: {str(e)}")
            continue
        
        data_leitura = registro['Data e hora da leitura']
        
        # Calcular índices
        media_brix, indice_maturacao, deve_colher = calcular_indice_maturacao(brix_base, brix_meio, brix_topo)
        
        # Armazenar resultados
        resultado = {
            'id_planta': id_planta,
            'brix_base': brix_base,
            'brix_meio': brix_meio,
            'brix_topo': brix_topo,
            'media_brix': media_brix,
            'indice_maturacao': indice_maturacao,
            'deve_colher': deve_colher,
            'data_leitura': data_leitura
        }
        
        resultados.append(resultado)
        
        # Exibir resultado na tela
        print(f"\nAnálise da planta {id_planta}:")
        print(f"  Brix (base/meio/topo): {brix_base:.2f}/{brix_meio:.2f}/{brix_topo:.2f}")
        print(f"  Média Brix: {media_brix:.2f}")
        print(f"  Índice de Maturação: {indice_maturacao:.2f}%")
        print(f"  Recomendação: {'COLHER' if deve_colher else 'NÃO COLHER'}")
    
    return resultados 