"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
"""
string = 'teste'
outra_variavel = f'{string[:2]}ABC{string[3:]}'
print(string)
print(outra_variavel)
print(string.capitalize())
print(string.zfill(10))
