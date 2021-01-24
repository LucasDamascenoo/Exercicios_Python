# Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a
# quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante
# perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o
# total de dias

cigarros = int(input('Quantos cigarros você fuma por dia? '))

anos = int(input('Quantos anos você já fuma?' ))

total = anos * 365 * cigarros
dias = total / 144

print(f'você fumou um tota de {total} cigarros e você perdeu {dias:.2f} dias da sua vida')

