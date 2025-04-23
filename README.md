# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# Nome do projeto


## Nome do grupo

## 👨‍🎓 Integrantes: 
- <a href="">Edson Henrique Felix Batista - RM: 566321</a>
- <a href="">Matheus José Parra -  RM: 561907</a>
- <a href="">Tiago Alves Cordeiro - RM: 561791</a> 

## 👩‍🏫 Professores:
### Tutor(a) 
- <a href="https://www.linkedin.com/company/inova-fusca">Lucas Gomes</a>
### Coordenador(a)
- <a href="https://www.linkedin.com/company/inova-fusca">André Godoi</a>


## 📜 Descrição

### Problema
Especialistas no setor indicam que o momento ideal para iniciar a colheita de cana é quando ela atinge a sua maturação, caracterizada como um processo fisiológico que envolve a formação de açúcares nas folhas e seu deslocamento e armazenamento nos colmos.  

Mas como definir o momento exato para a colheita de cana? Há algum método?

A resposta é sim. Hoje em dia já existem muitas maneiras de refinar o momento exato da colheita da cana-de-açúcar.

Existe um método que faz a avaliação da maturidade da planta em relação à quantidade de açúcares presente no colmo da cana-de-açúcar. Neste caso usa-se um refratômetro de campo, que faz a leitura do valor de graus Brix do colmo.

Para a determinação do Brix, deve ser feita uma média dos resultados obtidos de 3 partes do colmo (base, meio e ponta), com a colheita devendo ocorrer quando essa média for maior que 18.

Feita a leitura, procede-se com a determinação do índice de maturação, onde o Brix do topo deve ser dividido pelo Brix da base vezes 100.

IndícedeMaturação (IM) = Brixdotopodocolmo/brixdabasedocolmo*100

Neste caso, a colheita deve ocorrer quando o IM for próximo a 1. 

Fonte - https://blog.chbagro.com.br/perdas-na-colheita-de-cana-voce-sabe-como-reduzi-las

### Solução

Através de uma panilha com os dados coletados diariamente pelo refratômetro de campo, o programa faz a leitura e analise dos valores de grau de Brix coletados e salva no banco de dados as informações, indicando se está na maturação ideal para colheita

## 📁 Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- <b>.github</b>: Nesta pasta ficarão os arquivos de configuração específicos do GitHub que ajudam a gerenciar e automatizar processos no repositório.

- <b>assets</b>: aqui estão os arquivos relacionados a elementos não-estruturados deste repositório, como imagens.

- <b>config</b>: Posicione aqui arquivos de configuração que são usados para definir parâmetros e ajustes do projeto.

- <b>document</b>: aqui estão todos os documentos do projeto que as atividades poderão pedir. Na subpasta "other", adicione documentos complementares e menos importantes.

- <b>scripts</b>: Posicione aqui scripts auxiliares para tarefas específicas do seu projeto. Exemplo: deploy, migrações de banco de dados, backups.

- <b>src</b>: Todo o código fonte criado para o desenvolvimento do projeto ao longo das 7 fases.

- <b>README.md</b>: arquivo que serve como guia e explicação geral sobre o projeto (o mesmo que você está lendo agora).

## 🔧 Como executar o código

1. Subir o banco de dados local.
```sh
./scripts/run-db.sh
```

2. Gerar as envs (Contem as credenciais do banco de dados).
```sh
cp .env.example .env
```

3. Gerar o ambiente python e instala as dependencias.
```sh
python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt
```

4. Executar a aplicação.
```sh
# Executar aplicação python
python3 ./src/main.py ./config/data/exemplo.csv
```

5.

- Os dados serão salvos no banco de dados
- E será gerado o resultado o processamento em `/config/data/exemplo_resultado.json`

## 🗃 Histórico de lançamentos



## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>


