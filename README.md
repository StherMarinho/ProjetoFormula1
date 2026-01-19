# 🏎️ Projeto Fórmula 1 — Análise de Chances no Campeonato de 2025

Este projeto realiza uma análise do campeonato de Fórmula 1 a partir de dados de pontuação de corridas e sprints, avaliando quais pilotos ainda possuem chances matemáticas de conquistar o título e apresentando uma estimativa de probabilidade entre os cinco primeiros colocados.

## Funcionalidades

- Leitura de dados de uma planilha Excel
- Cálculo de pontos totais, pontos de sprint e pontos de corridas normais
- Identificação do líder atual do campeonato
- Avaliação de chances matemáticas de título
- Listagem dos cinco pilotos com chance de vencer o campeonato
- Estimativa percentual de chance de título entre os cinco primeiros

## Lógica do Cálculo

A chance de um piloto ser campeão é calculada somando seus pontos atuais com o máximo de pontos ainda possíveis nas corridas e sprints restantes.  
Caso esse valor ultrapasse a pontuação do líder atual, o piloto é considerado com chance matemática de título.

A probabilidade exibida é uma estimativa simples, baseada na proporção dos pontos atuais em relação ao total máximo possível.

## Observações

- As probabilidades apresentadas são apenas estimativas.
- O projeto possui finalidade educacional e analítica.

## Tecnologias Utilizadas

- Python
- Pandas
- Excel
