n1 = float(input('Digite uma nota: '))
n2 = float(input('Digite outro nota: '))

media = (n1 + n2) / 2

if media >= 9:
    print(f'Sua média foi: {media} e seu conceito foi A, APROVADO')
elif 7.5 <= media < 9:
    print(f'Sua média foi: {media} e seu conceito foi b , APROVADO')
elif 6 <= media < 7.5:
    print(f'Sua média foi: {media} e seu conceito foi c, APROVADO')
elif 4 <= media < 6:
    print(f'Sua média foi: {media} e seu conceito foi d, REPROVADO')
elif 0 <= media < 4:
    print(f'Sua média foi: {media} e seu conceito foi e, reprovado')
