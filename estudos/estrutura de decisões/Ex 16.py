a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))

delta = (b**2) - (4*a*c)

if a == 0:
    print('A equação não é de segundo grau')
elif delta < 0:
    print('Não possui raizes reais')
elif delta == 0:
    print('Possui uma raiz real')
elif delta >0:
    print('Possui duas raizes reais')