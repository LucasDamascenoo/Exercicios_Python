# faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule
# e mostre o total do seu salário no referido mês, sabendo se que são descontados 11% para o Imposto de Renda,
# 8% para o INSS e 5% para o sindicato, faça um programa que nos dê o salário bruto, quanto pagou ao INSS,quanto pagou ao sindicato e
# o salário líquido

ganho_hora = float(input('Quanto você ganha por hora? '))
horas_trabalhadas = int(input('Quantas horas por mês voê trabalha? ' ))

bruto = ganho_hora * horas_trabalhadas

ir = bruto * 0.11
inss = bruto * 0.08
sid = bruto * 0.05

liquido = bruto - ir - inss - sid

print(f'Seu salario bruto é R$ {bruto} ')
print(f'Tem um desconto de IR de R$ {ir:.2f}')
print(f'Tem um desconto de inss de R$ {inss:.2f}')
print(f'Tem um desconto de sid de R$ {sid:.2f}')
print(f'Apos esses desconto seu salario é {liquido:.2f}')



