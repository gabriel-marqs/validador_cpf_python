cpf = input('Informe o CPF: ')

digitos_separados = [char for char in cpf if char.isdigit()]
tamanho_lista = len(digitos_separados)

while tamanho_lista != 11:
    cpf = input('CPF inválido, digite novamente: ')
    digitos_separados = [char for char in cpf if char.isdigit()]
    tamanho_lista = len(digitos_separados)

total = 0

for indice, digito in enumerate(digitos_separados[:9], start=0):
    total += int(digito) * (10 - indice)    

digito_1 = (total * 10) % 11
digito_1 = 0 if digito_1 > 9 else digito_1

if digito_1 == int(digitos_separados[9]):
    print('1º dígito do CPF válido')
else:
    print('1º dígito do CPF inválido')