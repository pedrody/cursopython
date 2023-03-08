"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""

num_str = input('Irei dobrar o número digitado: ')

# Não é muito prudente usar o try/except dessa maneira.
# Apenas seguindo a aula...
try:
    print(num_str, type(num_str))
    num_float = float(num_str)
    print(num_float, type(num_float))
    print(f'{num_str} -> {num_float * 2:.2f}')
except:
    print('Isso não é um número.')

# if num_str.isdigit():
#     num_float = float(num_str)
#     print(f'{num_str} -> {num_float * 2:.2f}')
# else:
#     print('Isso não é um número.')