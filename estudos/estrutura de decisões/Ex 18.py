dias = int(input('Digite um dia: '))
mes = int(input('Digite um mes: '))
ano = int(input('Digite um ano: '))

valida= False

#31 dias
if (mes == 1 or mes == 3 or mes == 5 or mes== 7 or mes == 8 or mes == 10 or mes == 12):
   if 1<= dias <=31:
     valida = True
elif (mes == 11 or mes == 4 or mes == 6 or mes == 9):
   if 1<= dias <= 30:
     valida = True
elif mes ==2:
   if (ano%4 == 0 and ano%100 != 0) or (ano%400 == 0):
     if 1<= dias <= 29:
       valida = True
   elif 1<= dias <=28:
     valida = True

if valida:
  print(f'{dias}/{mes}/{ano}')
else:
  print('não é valido')