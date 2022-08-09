#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
metros=float(input("Metros quadrados a serem pintados:"))
litrosnecessarios=float(metros/3)
latas=float(litrosnecessarios/18)
if ((litrosnecessarios%18)!=0):
    latas=float((litrosnecessarios//18)+1)
preco=float(latas*80)
print(f'Latas: %.0f' %(latas))
print(f'Preço Total: R$ %.2f' %(preco))
