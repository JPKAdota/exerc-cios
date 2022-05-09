numero = 305

cent_str = dez_str = und_str = ''

cent_int, numero = divmod(numero,100)

partes = 0

if cent_int ==1:
  cent_str = '1 centena'
  partes += 1
elif cent_int >1:
  cent_str = f'{cent_int} centenas'
  partes += 1

dez_int, numero = divmod(numero,10)

if dez_int ==1:
  dez_str = '1 dezena'
  partes += 1
elif dez_int >1:
  dez_str = f'{dez_int} dezenas'
  partes += 1


if numero ==1:
  und_str = '1 unidade'
  partes += 1
elif numero >1:
  und_str = f'{numero} unidades'
  partes += 1


if partes == 0:
  print('Não possui centena, dezena e unidades')
elif partes == 3:
  print(f'{cent_str}, {dez_str} e  {und_str}')
elif partes ==1:
  print(cent_str + dez_str + und_str)
elif partes == 2:
  if cent_str != '':
    segunda_parte = dez_str + und_str
    print(f'{cent_str} e {segunda_parte}')
  else:
     print(f'{dez_str} e {und_str}')