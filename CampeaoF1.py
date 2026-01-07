import pandas as pd

tabelaPilotos = pd.read_excel("CampeaoF1.xlsx", sheet_name="Temporada2025")
tabelaPontuacao = pd.read_excel("CampeaoF1.xlsx", sheet_name="Pontuação")
tabelaPontuacaoSprint = pd.read_excel("CampeaoF1.xlsx", sheet_name= "PontuaçãoSprint")

pontuacaoTotal = tabelaPilotos['Total de Pontos']
tabelaPilotos['Pontos_sprint_totais'] = tabelaPilotos[['SPRINT da China (Xangai)', 'SPRINT de Miami (Miami)', 'SPRINT da Bélgica (Spa-Francorchamps)']].sum(axis=1)
tabelaPilotos['Pontos_normais_totais'] = pontuacaoTotal - tabelaPilotos['Pontos_sprint_totais']

corridasRealizadas = int(input("Quantas corridas já se passaram: ")) # até o GP da Bélgica: 13
sprintsRealizadas = int(input("Quantas sprints já se passaram: ")) # até o GP da Bélgica: 3
totalCorridas = 24
totalSprints = 6

corridasRestantes = totalCorridas - corridasRealizadas
sprintsRestantes = totalSprints - sprintsRealizadas

tabelaPilotos = tabelaPilotos.sort_values(by='Total de Pontos', ascending=False).reset_index(drop=True)
liderPontos = tabelaPilotos.iloc[0]['Total de Pontos']
liderNome = tabelaPilotos.iloc[0]['Piloto']

print(f"\nLíder atual: {liderNome} com {liderPontos} pontos\n")

pontosMaxCorrida = tabelaPontuacao['Pontos'].max()
pontosMaxSprint = tabelaPontuacaoSprint['Pontos'].max()

pontosRestantes = (pontosMaxCorrida * corridasRestantes) + (pontosMaxSprint * sprintsRestantes)

def AvaliaChances(pontosAtual):
    return (pontosAtual + pontosRestantes) > liderPontos

tabelaPilotos['Tem chance'] = tabelaPilotos['Total de Pontos'].apply(AvaliaChances)

pilotosComChance = tabelaPilotos[tabelaPilotos['Tem chance'] == True].head(5)

print("Pilotos com chances de vencer o campeonato:")
for i, row in pilotosComChance.iterrows():
    print(f"{i+1}. {row['Piloto']} - {row['Total de Pontos']} pontos")

print("\nProbabilidade estimada de ser campeão entre os 5 primeiros:")

top5 = tabelaPilotos.head(5)
totalPontosPossiveis = top5['Total de Pontos'].max() + pontosRestantes

for i, row in top5.iterrows():
    probabilidade = (row['Total de Pontos'] / totalPontosPossiveis) * 100
    print(f"{i+1}. {row['Piloto']} - {probabilidade:.2f}% de chance")
