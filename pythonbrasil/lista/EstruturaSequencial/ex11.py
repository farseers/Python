#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#a) o produto do dobro do primeiro com metade do segundo .
#b) a soma do triplo do primeiro com o terceiro.
#c) o terceiro elevado ao cubo.

I1	=	int(input('Digite um número inteiro:'))
I2	=	int(input('Digite um número inteiro:'))
F1	=	float(input('Digite um número real:'))
x = (I1*2)*(I2/2)
y= (3*I1+F1)
z= F1**3
print('Produto do dobro do primeiro com metade do segundo', x)
print('Soma do triplo do primeiro com o terceiro', y)
print('Terceiro elevado ao cubo', z)