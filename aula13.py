nome = 'Nome'
altura_m = 1.80
peso_kg = 95
imc = peso_kg / altura_m ** 2

# f-strings
linha_1 = f'{nome} tem {altura_m:.2f}m de altura'
linha_2 = f'pesa {peso_kg:.1f}kg e seu IMC é:'
linha_3 = f'{imc:.2f}'
print(linha_1)
print(linha_2)
print(linha_3)
