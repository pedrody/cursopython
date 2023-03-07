# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 
#  T e s t e
# -5-4-3-2-1

# nome = 'Teste'
# print(nome[2])
# print(nome[-4])
# print('ste' in nome)  # True
# print('asd' in nome)  # False
# print(10 * '-')
# print('ste' not in nome)  # False
# print('asd' not in nome)  # True

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
    