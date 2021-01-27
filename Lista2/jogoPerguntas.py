#Jogo ao o usuario tem que responder perguntas com algumas opções, e no fim ele ver a % de acertos

print('Resposda as pergunta escolhendo as opções a,b ou c e teste seus conhecimnetos. ')
print('-' *78)


perguntas = {
    'pergunta1': {
        'pergunta': 'Quanto é 5*5?',
        'resposta': {'a': '25', 'b': '20', 'c': '30'},
        'resposta_certa':'a',

    },
     'pergunta2': {
        'pergunta': 'Em qual ano ocorreu o descobrimento do Brasil?',
        'resposta': {'a': '1501', 'b': '1499', 'c': 1500},
        'resposta_certa':'c',

    },
     'pergunta3': {
        'pergunta': 'Qual simbolo abaixo simboliza uma lista?',
        'resposta': {'a': '()', 'b': '[]', 'c': '([])'},
        'resposta_certa':'b',

    },
    'pergunta4': {
        'pergunta': 'Qual casa pertence Harry potter?',
        'resposta': {'a': 'lufa-lufa', 'b': 'Grifinória', 'c':'Corvinal '},
        'resposta_certa':'b',

    },

}


print()

respostas_certas = 0

for pk,pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')

    print('Respostas: ')
    for rk,rv in pv['resposta'].items():
        print(f'[{rk}]: {rv}')

    resposta_usuario = input('Digete sua resposta: ')
    if resposta_usuario == pv['resposta_certa']:
        print("Uhuuuuu: você ACERTOU!!!")
        respostas_certas += 1
    else:
         print('Que pena, você ERROW!!!')

    print()

qt_perguntas = len(perguntas)
pct_acerto = respostas_certas / qt_perguntas * 100
print(f'Você acertou {respostas_certas} respostas.')
print(f'Sua porcentagem de acerto foi {pct_acerto}%.')