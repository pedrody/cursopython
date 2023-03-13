"""
Faça uma lista de compra com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com
erros de índices inexistentes na lista
"""

import os
itens_lista_compras = []

while True:
    print('\nSelecione uma opção')
    opcao_menu = input('[i]nserir [a]pagar [l]istar [s]air: ').lower()
    if opcao_menu in ['i', 'inserir']:
        itens_lista_compras.append(input('Produto: '))
        os.system('cls')

    elif opcao_menu in ['a', 'apagar']:
        try:
            i = int(input('Escolha o índice para apagar: '))
            del itens_lista_compras[i]
            os.system('cls')
        except ValueError:
            os.system('cls')
            print('Escolha um índice válido. [!]')
            continue
        except IndexError:
            os.system('cls')
            print('Índice inexistente. [!]')
        except Exception:
            os.system('cls')
            print('Erro desconhecido [!]')

    elif opcao_menu in ['l', 'listar']:
        os.system('cls')
        for indice, produto in enumerate(itens_lista_compras):
            print(f'{indice} - {produto}')
    elif opcao_menu in ['s', 'sair']:
        os.system('cls')
        print('Até mais!\n')
        break
    else:
        os.system('cls')
        print('Escolha uma opção válida. [!]')
        continue
