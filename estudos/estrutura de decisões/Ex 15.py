a = float(input('Digite o primeiro lado: '))
b = float(input('Digite o segundo lado: '))
c = float(input('Digite o terceiro lado: '))

if (a + b < c) or (a + c < b ):
    print('Não é um triângulo')
elif a == b == c:
    print('É triângulo equilátero')
elif a==b or b==c or c==a:
    print('É triângulo isóceles')
else:
    print('É triângulo escaleno')