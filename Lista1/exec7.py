#Converta uma temperatura digitada em Celsius para Fahrenheit. F = 9*C/5 + 32

temp = float(input('Digete a temperatura que deseja converter: '))

c_toF = (temp * 9/5) + 32

print(f'A temperatura em celsius {temp} convertida é {c_toF}')

