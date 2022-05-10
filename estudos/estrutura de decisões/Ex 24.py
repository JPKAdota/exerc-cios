"""fazer um programa que leia 2 números"""

n1 = int(input('Digite um número: '))
n2 = int(input('Dgite outro número: '))

operacao = input('Escolha uma operação + , - , / ou *:  ')

if operacao == '+':
    r = n1 + n2
elif operacao == '-':
    r = n1 - n2
elif operacao == '/':
    r = n1 / n2
elif operacao == '*':
    r = n1 * n2

print(f'Resultado:{r}')

if r % 2 == 0:
    print('par')
else:
    print('impar')
if r < 0:
    print('negativo')
else:
    print('Postivo')
if r == round(r):
    print('inteiro')
else:
    print('Decimal')
