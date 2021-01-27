#faça um jogo de dados que sorteia um numero de 1,6 e compara com o numero que o usuario digitou

import random

r = 'sim'

while r == 'sim':
    palmite = int(input('digete um numero de 1 a 6: '))
    n = random.randint(1, 6)
    print(n)
    r = str(input('Deseja continuar? [S/N] '))
    if n == palmite:
        print(f'VOCÊ GANHOU!!! Seu palmite foi {palmite} e o numero sorteado foi {n}')
    else:
        print('Você perdeu!!!')
else:
    print('obrigado por jogar com a gente')