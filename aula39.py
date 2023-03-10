"""
Iterando strings com while
"""

# Minha solução:
nome = input('Digite seu nome: ')
novo_nome = '*'
c = 0

while c < len(nome):
    novo_nome += nome[c] + '*'
    c += 1
print(novo_nome)

# Solução professor:
# nome = 'Luiz Otávio'
# novo_nome = ''
# indice = 0

# while indice < len(nome):
#     letra = nome[indice]
#     novo_nome +=  f'*{letra}'
#     indice += 1

# novo_nome += '*'
# print(novo_nome)
