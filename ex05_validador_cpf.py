cpf = input('Informe o CPF: ')

digitos_separados = [char for char in cpf if char.isdigit()]
digitos_repetidos = digitos_separados[0] * len(digitos_separados)

while len(digitos_separados) != 11 or digitos_repetidos == ''.join(digitos_repetidos):
    cpf = input('CPF inválido, digite novamente: ')
    digitos_separados = [char for char in cpf if char.isdigit()]

digitos_separados = digitos_separados[:9]
digito_1 = 0
contador = len(digitos_separados) + 1

for indice, digito in enumerate(digitos_separados, start=0):
    digito_1 += int(digito) * (contador - indice)
    
digito_1 = (digito_1 * 10) % 11
digito_1 = str(0 if digito_1 > 9 else digito_1)

digitos_separados.append(digito_1)

digito_2 = 0
contador = len(digitos_separados) + 1

for indice, digito in enumerate(digitos_separados, start=0):
    digito_2 += int(digito) * (contador - indice)

digito_2 = (digito_2 * 10) % 11
digito_2 = str(0 if digito_2 > 9 else digito_2)

if cpf[9] == digito_1 and cpf[10] == digito_2:
    print('CPF válido')
else:
    print('CPF inválido')