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

## Execução