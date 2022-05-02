hora = float(input('Digite o valor da hora: '))
hora_trabalhada = float(input('Digite quantas horas trabalhou no mês: '))

salario_bruto = hora * hora_trabalhada

if salario_bruto <= 900:
    ir = 0
    inss = salario_bruto * 0.1
    fgts = salario_bruto * 0.11
    desconto = inss + ir
    salario_liquido = salario_bruto - desconto
    print(f'O seu sálario bruto é: R$ {salario_bruto}, o inss = {inss}, ir = isento, descontos = R$ {desconto}, salário líquido = R$ {salario_liquido}')
elif 900 < salario_bruto <= 1500:
    ir = salario_bruto * 0.05
    inss = salario_bruto * 0.1
    fgts = salario_bruto * 0.11
    desconto = inss + ir
    salario_liquido = salario_bruto - desconto
    print(f'O seu sálario bruto é: R$ {salario_bruto}, o inss = {inss}, ir = R$ {ir}, descontos = R$ {desconto}, salário líquido = R$ {salario_liquido}')
elif 1500 < salario_bruto <= 2500:
    ir = salario_bruto * 0.1
    inss = salario_bruto * 0.1
    fgts = salario_bruto * 0.11
    desconto = inss + ir
    salario_liquido = salario_bruto - desconto
    print(f'O seu sálario bruto é: R$ {salario_bruto}, o inss = {inss}, ir = R$ {ir}, descontos = R$ {desconto}, salário líquido = R$ {salario_liquido}')
elif salario_bruto > 2500:
    ir = salario_bruto * 0.2
    inss = salario_bruto * 0.1
    fgts = salario_bruto * 0.11
    desconto = inss + ir
    salario_liquido = salario_bruto - desconto
    print(f'O seu sálario bruto é: R$ {salario_bruto}, o inss = {inss}, ir = R$ {ir}, descontos = R$ {desconto}, salário líquido = R$ {salario_liquido}')
