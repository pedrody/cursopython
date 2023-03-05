#  if / elif / else

# entrada = input('Você quer "entrar" ou "sair"? ')
# if entrada == "entrar":
#     print('Você entrou no sistema')
# elif entrada == "sair":
#     print('Você saiu do sistema')
# else:
#     print('Você não digitou nem entrar e nem sair.')
# print('fora dos blocos')

# teste painel de login:
login = 'admin'
password = '123'

user_login = input('Login: ')
user_password = input('Password: ')

if user_login == login:
    if user_password == password:
        print('[!] ACCESS ALLOWED [!]')

    elif user_password != password:
        print('[!] ACCESS DENIED [!]')
else:
    print('[!] ACCESS DENIED [!]')