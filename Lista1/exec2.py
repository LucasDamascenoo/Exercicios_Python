#Escreva um programa que leia um valor em metros e o exiba convertido em milímetros

metros = float(input('Digete quantos metros deseja converter: '))

convert = metros * 1000

print(f'{metros} metros em miletros é: {convert:.0f}')