"""
Listas em Python
Tipo list - Mutável
suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, ...
"""
#         01234
#        -54321
string = 'ABCDE'  # 5 caracteres
# print(bool([]))  # falsy
# print(lista, type(lista))

#         0     1      2      3    4
lista = [123, True, 'Teste', 1.2, []]
#        -5    -4     -3     -2   -1
lista[-3] = '*****'
print(lista)
print(lista[2])
