retirada = int(input('Qual valor a ser sacado?: '))

nota_100, retirada = divmod(retirada, 100)
nota_50, retirada = divmod(retirada, 50)
nota_20, retirada = divmod(retirada, 20)
nota_10, retirada = divmod(retirada, 10)
nota_5, retirada = divmod(retirada, 5)
nota_1, retirada = divmod(retirada, 1)


if nota_100 > 0:
     print(f'{nota_100} nota(s) de 100')
if nota_50 > 0:
     print(f'{nota_50} nota(s) de 50')
if nota_20 > 0:
     print(f'{nota_100} nota(s) de 20')
if nota_10 > 0:
     print(f'{nota_10} nota(s) de 10')
if nota_5 > 0:
     print(f'{nota_5} nota(s) de 5')
if nota_1 > 0:
     print(f'{nota_1} nota(s) de 1')