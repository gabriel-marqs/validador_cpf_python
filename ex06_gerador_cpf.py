import random

cpf = []

for digito in range(9):
    numero = str(random.randint(0, 9))
    cpf.append(numero)


digito_1 = 0
contador = len(cpf) + 1

for indice, digito in enumerate(cpf, start=0):
    digito_1 += int(digito) * (contador - indice)
    
digito_1 = (digito_1 * 10) % 11
digito_1 = str(0 if digito_1 > 9 else digito_1)

cpf.append(digito_1)

digito_2 = 0
contador = len(cpf) + 1

for indice, digito in enumerate(cpf, start=0):
    digito_2 += int(digito) * (contador - indice)

digito_2 = (digito_2 * 10) % 11
digito_2 = str(0 if digito_2 > 9 else digito_2)

cpf.append(digito_2)
cpf = ''.join(cpf)

print(cpf)