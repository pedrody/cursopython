# Introdução ao desempacotamento

# nome1, nome2, nomes3 = nomes = ['Maria', 'Helena', 'Luiz']
nome, *_ = ['Maria', 'Helena', 'Luiz']  # underline indica que não iremos utilizar essa variável.
_, nome, *_ = ['Maria', 'Helena', 'Luiz']
_, _, nome, *_ = ['Maria', 'Helena', 'Luiz']
print(nome, _)

