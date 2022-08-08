# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7
alt = float(input("Digite a altura em metros:"))
i = int(input("Digite 1 para Homem e 2 para Mulher:"))
if i==1:
    pesoideal= (72.7*alt)-58
    print("O peso ideal é:", pesoideal, "kg")
if i==2:
    pesoideal= (62.1*alt) -44.7
    print("O peso ideal é:", pesoideal, "kg")