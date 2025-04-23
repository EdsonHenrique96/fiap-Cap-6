-- Criação da tabela de análise de cana-de-açúcar
-- Migração inicial - 001

CREATE TABLE analise_cana (
    id_planta VARCHAR2(50),
    brix_base NUMBER(10,2),
    brix_meio NUMBER(10,2),
    brix_topo NUMBER(10,2),
    media_brix NUMBER(10,2),
    indice_maturacao NUMBER(10,2),
    deve_colher CHAR(1),
    data_leitura VARCHAR2(50)
) 