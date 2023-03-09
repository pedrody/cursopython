"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

# num = input('Digite um número inteiro: ')
# try:
#     if num.isdigit:
#         num = int(num)
#         if num % 2 == 0:
#             print('O número digitado é PAR!')
#         else:
#             print('O número digitado é IMPAR!')
# except:
#     print('Isso não é um número inteiro [!]')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

# hora = input('Qual o horário? ')
# try:
#     hora = int(hora)
#     if hora >= 0 and hora <= 11:
#         print('Bom DIA!')
#     elif hora >= 12 and hora <= 17:
#         print('Boa TARDE!')
#     elif hora >= 18 and hora <= 23:
#         print('Boa NOITE!')
#     else:
#         print('Digite um horário válido [!]')
# except:
#     print('Digite apenas números inteiros [!]')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome_usuario = len(input('Informe seu nome: ').replace(' ', ''))

if nome_usuario > 1 and nome_usuario <= 4:
    print('Seu nome é CURTO.')
elif nome_usuario >= 5 and nome_usuario <= 6:
    print('Seu nome é NORMAL.')
elif nome_usuario > 7:
    print('Seu nome é MUITO GRANDE.')
else:
    print('Digite mais de uma letra.')
    