#Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a
#porcentagem do aumento. Exiba o valor do aumento e do novo salário.

salario = float(input('Digete seu salario: '))

aumento = salario + (salario * 15 / 100)

print(f'Seu salario R${salario} reais com um aumento de 15% fica em R$ {aumento} reais')

