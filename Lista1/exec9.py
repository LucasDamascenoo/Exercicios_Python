# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo
# usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar,
# sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.

d = int(input('Quantos dias alugou o carro? '))
km = float(input('Quantos kms rodou? '))

preco = (d * 60) + (km * 0.15)

print(f'Você alugou o carro por {d} dias e andou {km} kms e o valor a pagar é R$ {preco}')

