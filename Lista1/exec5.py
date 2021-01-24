# Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o
# preço a pagar.

preco_prod = float(input('Digete o preço do produto: '))

preco_desconto = preco_prod - (preco_prod * 7 / 100)

print(f'O seu produto custa R$ {preco_prod} reais e com um desconto de 7% você vai pagar R${preco_desconto:.2f} reais')

