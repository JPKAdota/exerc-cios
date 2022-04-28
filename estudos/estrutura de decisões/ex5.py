n1 = int(input('digite sua nota:'))
n2 = int(input('Digite outra nota: '))
media = (n1 + n2)/2
print(f'Sua média foi: {media}')

if media < 7:
    print('reprovado')
elif media == 10:
    print('Aprovado com distinção')
else:
    print('Arpovado')
