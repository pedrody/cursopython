# Calculadora com while

# Minha solução:
num_1 = 0
num_2 = 0
total = 0
while True:
    try:
        num_1 = float(input('Digite um número: '))
        num_2 = float(input('Digite outro número: '))
    except:
        print('Apenas números [!]')
        continue
    operador = input('Digite o operador (+ - / *): ')

    if operador == '+':
        total = num_1 + num_2
        print(f'{num_1} + {num_2} = {total:.2f}')
    elif operador == '-':
        total = num_1 - num_2
        print(f'{num_1} - {num_2} = {total:.2f}')
    elif operador == '/':
        total = num_1 / num_2
        print(f'{num_1} / {num_2} = {total:.2f}')
    elif operador == '*':
        total = num_1 * num_2
        print(f'{num_1} * {num_2} = {total:.2f}')
    else:
        print('Operador desconhecido [!]')
    
    sair = input('Deseja sair? [s]im -> ').lower()
    if sair == 'sim' or sair == 's':
        break

# Solução professor:
# while True:
#     numero_1 = input('Digite um número: ')
#     numero_2 = input('Digite outro número: ')
#     operador = input('Digite o operador (+-/*): ')

#     numeros_validos = None

#     try:
#         num_1_float = float(numero_1)
#         num_2_float = float(numero_2)
#         numeros_validos = True
#     except:
#         numeros_validos = None

#     if numeros_validos is None:
#         print('Um ou ambos os números digitados são inválidos.')
#         continue

#     operadores_permitidos = '+-/*'

#     if operador not in operadores_permitidos:
#         print('Operador inválido.')
#         continue

#     if len(operador) > 1:
#         print('Digite apenas um operador.')
#         continue

#     sair = input('Quer sair? [s]im: ').lower().startswith('s')

#     if sair is True:
#         break