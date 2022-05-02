salario_antigo = float(input('Digite o salário sem aumento: '))

if salario_antigo <= 280:
    aumento20 = salario_antigo * 1.2
    print(f'O seu sálario de r$ {salario_antigo}, aumentou em 20% e foi para r$ {aumento20}')
elif 280 < salario_antigo <= 700:
    aumento15 = salario_antigo * 1.15
    print(f'O seu sálario de r$ {salario_antigo}, aumentou em 15% e foi para r$ {aumento15}')
elif 700 < salario_antigo <= 1500:
    aumento10 = salario_antigo * 1.10
    print(f'O seu sálario de r$ {salario_antigo}, aumentou em 10% e foi para r$ {aumento10}')
elif salario_antigo > 1500:
    aumento5 = salario_antigo * 1.05
    print(f'O seu sálario de r$ {salario_antigo}, aumentou em 5% e foi para r$ {aumento5}')

