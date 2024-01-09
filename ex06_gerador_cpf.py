import random

def gerador_digito(cpf):
    digito = 0
    for indice, numero in enumerate(cpf, start=0):
        digito += int(numero) * (len(cpf) + 1 - indice)
    digito = (digito * 10) % 11
    cpf.append(str(0 if digito > 9 else digito))

cpf = []

for digito in range(9):
    numero = str(random.randint(0, 9))
    cpf.append(numero)

gerador_digito(cpf)
gerador_digito(cpf)
print(''.join(cpf))