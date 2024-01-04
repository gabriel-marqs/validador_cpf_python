cpf = input('Informe o CPF: ')

digitos_separados = [char for char in cpf if char.isdigit()]
tamanho_lista = len(digitos_separados)

while tamanho_lista != 11:
    cpf = input('CPF inválido, digite novamente: ')
    digitos_separados = [char for char in cpf if char.isdigit()]
    tamanho_lista = len(digitos_separados)

multiplo = 10
total = 0

for digito in digitos_separados[:9]:
    total += int(digito) * multiplo
    multiplo -= 1

total = (total * 10) % 11
digito_1 = 0 if total > 9 else total

if digito_1 == int(digitos_separados[9]):
    print('1º dígito do CPF válido')
else:
    print('1º dígito do CPF inválido')