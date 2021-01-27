#Faça um Programa que leia três números e mostre o menor deles

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))
n3 = int(input('Digite um numero: '))

if n1 <= n2 and n1 <= n3:
    print(f'Maior {n1}')
elif n2 <=n3:
    print(f'Maior {n2}')
else:
    print(f'Maior {n3}')