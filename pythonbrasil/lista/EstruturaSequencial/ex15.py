# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:
valor = float(input("Digite quanto ganha por hora:"))
horas = float(input("Digite quantas horas trabalhou no mês:"))
bruto = float(valor*horas)
ir =  float(bruto*0.11)
inss =  float(bruto*0.08)
sindicato =  float(bruto*0.05)
liquido =  float(bruto-ir-inss-sindicato)
print('+ Salário Bruto : R$ %.2f' %(bruto))
print(f'- IR (11%) : R$: {round(ir, 2)}')
print(f'- INSS (8%) : R$ {round(inss, 2)}')
print(f'- Sindicato (5%) : R$ {round(sindicato, 2)}')
print(f'= Salário Liquido : R$ %.2f' %(liquido))
