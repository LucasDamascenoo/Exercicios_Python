#Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule
#o total em segundos.

d = int(input('dias: '))
h = int(input('horas: '))
m = int(input('minutos: '))
s = int(input('segundos: '))

total = d*24*60*60 + h*60*60 + m*60 + s

print(total)