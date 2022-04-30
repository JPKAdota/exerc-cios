p1 = float(input('Digite o primeiro prduto: r$ '))
p2 = float(input('Digite o segundo prduto: r$ '))
p3 = float(input('Digite o terceiro prduto: r$ '))

menor = p1

if p2 < p1:
    menor = p2
if p3 < p1:
    menor = p3
print('O menor preço é: r$ ', menor)