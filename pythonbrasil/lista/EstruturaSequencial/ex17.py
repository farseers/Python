
metros=float(input("Metros quadrados a serem pintados:"))
metros=float(metros*1.1)
litrosnecessarios=float(metros/6)
latas=float(litrosnecessarios/18)
if ((litrosnecessarios%18)!=0):
    latas=float((litrosnecessarios//18)+1)
preco1=float(latas*80)
print(f'Ao comprar apenas latas de 18 litros')
print(f'Latas: %.0f' %(latas))
print(f'Preço Total: R$ %.2f' %(preco1))

galoes=float(litrosnecessarios/3.6)
if ((litrosnecessarios%3.6)!=0): 
    galoes=float((litrosnecessarios//3.6)+1)
preco2=float(galoes*25)
print(f'Ao comprar apenas galões de 3,6 litros')
print(f'Galões: %.0f' %(galoes))
print(f'Preço Total: R$ %.2f' %(preco2))

latas=float(litrosnecessarios//18)
galoes = float((litrosnecessarios%18))
if (((litrosnecessarios%18)%3.6)!=0):
    galoes=float(((litrosnecessarios%18)//3.6)+1)
preco1=float(latas*80)
preco2=float(galoes*25)
print(f'Caso compre latas e galões')
print(f'Latas: %.0f' %(latas))
print(f'Galões: %.0f' %(galoes))
print(f'Preço Total: R$ %.2f' %(preco2+preco1))
