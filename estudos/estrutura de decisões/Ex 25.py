P1 = input('Telefonou para vítima? ')
P2 = input('Esteve no local do crime? ')
P3 = input('Mora perto da vítima? ')
P4 = input('Devia para vítima? ')
P5 = input('Já trabalhou para vítima? ')

resultado = 0
if P1 == 'sim':
    resultado += 1
if P2 == 'sim':
    resultado += 1
if P3 == 'sim':
    resultado +=1
if P4 == 'sim':
    resultado += 1
if P5 == 'sim':
    resultado += 1

print(f'Soma das perguntas: {resultado}')

if resultado == 2:
    print('Suspeito')
elif resultado == 3:
    print('Cumplice')
elif resultado == 4:
    print('Cumplice')
elif resultado == 5:
    print('Assassino')
else:
    print('Inocente')
