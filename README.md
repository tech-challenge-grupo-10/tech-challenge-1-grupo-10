# Tech Challenge Grupo 10

Este repositório contém o caderno análise para o Tech Challenge da Fase 1 da pós IA para Devs da FIAP do ano de 2025

## O Grupo 10
O grupo 10 consiste dos seguintes alunos da pós:

- Felipe Almeida Lima Machado - RM 366360
- Hipólito Douglas França Moreira - RM 366361
- Ítalo Bruno de Morais Barretto - RM 366363
- Leonardo Machado de Andrade - RM 366359

## Roteiro

1. Primeira parte é identificar a pergunta
2. Processo de limpeza, adequação e prepação de amostras
3. Treinamento com os algoritmos de ML
4. Comparação
5. Explicar os resultados

## Instalação

Para rodar este projeto, é necessário instalar a ferramenta `uv` para organização das dependencias e dar mais velocidade na instalação de pacotes, clonar o repositório e instalar as dependências.

### Instalação UV

O guia de instalação completo está disponível em:

https://docs.astral.sh/uv/getting-started/installation

Nesse documento será adotado a instalação de linux por conta do Dockerfile, que pode ser executado também localmente.

Use `curl` para baixar original script e executar com sh:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Caso não tenha `curl`, tem a alternatia de usar o `wget`:

```bash
wget -qO- https://astral.sh/uv/install.sh | sh
```

### Clonar repositório e instalar as dependências

Clonar o repositório:

```bash
git clone https://github.com/tech-challenge-grupo-10/tech-challenge-1-grupo-10

cd tech-challenge-1-grupo-10

uv sync
```

## Jupyter Notebook

A execução do jupyter notebook para as análises foi feita com a IDE VSCode e o plugin da Microsoft para o Jupyter Notebook

Microsoft Visual Studio Code:

https://code.visualstudio.com

Plugin Jupyter da Microsoft: 

https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter

Após instalar as dependências, você pode executar o notebook que está dentro da pasta notebooks

```
notebooks/analysis.ipynb
```

## Execução

Para executar o modelo instalado localmente com a massa de avaliação:

```bash
uv run main.py
```

Para executar usando uma massa de avaliação com os parâmetros específicos vindos da linha de comando:

```bash
uv run main.py \
--radius_mean=17.99 \
--texture_mean=10.38 \
--perimeter_mean=122.8 \
--area_mean=1001 \
--smoothness_mean=0.1184 \
--compactness_mean=0.2776 \
--concavity_mean=0.3001 \
--concave_points_mean=0.1471 \
--symmetry_mean=0.2419 \
--fractal_dimension_mean=0.07871
```

## Docker

Para rodar o modelo no script em `main.py` executar o build da imagem docker:

```bash
docker build -t tech_challenge_fase_1 . 
```

Rodar a aplicação no container, com a massa de avaliação:

```bash
docker run -it --rm tech_challenge_fase_1 uv run main.py
```
Rodar a aplicação no container, com dados preenchidos pela linha de comando:

```bash
docker run -it --rm tech_challenge_fase_1 uv run main.py \
--radius_mean=17.99 \
--texture_mean=10.38 \
--perimeter_mean=122.8 \
--area_mean=1001 \
--smoothness_mean=0.1184 \
--compactness_mean=0.2776 \
--concavity_mean=0.3001 \
--concave_points_mean=0.1471 \
--symmetry_mean=0.2419 \
--fractal_dimension_mean=0.07871
```
