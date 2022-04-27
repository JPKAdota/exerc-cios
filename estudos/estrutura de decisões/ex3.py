sexo = input('Digite F, M ou I: ').upper()

if sexo == 'F':
    print('Feminino')
elif sexo == 'M':
    print('Masculino')
elif sexo == 'I':
    print('Indefinido')
else:
    print('inválido')