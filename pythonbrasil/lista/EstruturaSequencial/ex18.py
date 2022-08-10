# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
tamanhoMB = float(input('Digite o o tamanho do arquivo para download (em MB):'))
velocidadeMbps =float(input('Digite a velocidade de um link de Internet (em Mbps):'))
tamanhoMb = float(tamanhoMB*8)
temposeg=float(tamanhoMb/velocidadeMbps)
tempomin=float(temposeg//60)
temposeg=float(temposeg%60)
print(tempomin,'minutos e ',temposeg,'segundos')