"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os
import random

palavras = ['banana', 'maçã', 'perfume', 'cadeira', 'janela', 'sapato', 'computador',
            'celular', 'cabelo']
# Escolhendo uma palavra aleatória
palavra_secreta = palavras[random.randrange(9)]

palavra_formatada = ''
tentativas = 0
lista_palavra = []

# Formatando a palavra secreta
for letra in palavra_secreta:
    palavra_formatada += '*'

print(f'Tente adivinhar a palavra ({len(palavra_formatada)} letras) -> {palavra_formatada}')

# Uma bagunça meu raciocínio :(
while True:
    letra = input('Digite uma letra: ')
    tentativas += 1

    if len(letra) > 1:
        print('Digite apenas UMA letra.')
        continue

    if letra in palavra_formatada:
        print(palavra_formatada)
        continue
    
    elif letra not in palavra_formatada:
        for i in range(len(palavra_secreta)):
            if letra == palavra_secreta[i]:
                lista_palavra = list(palavra_formatada)
                lista_palavra[i] = letra
                palavra_formatada = "".join(lista_palavra)
        print(palavra_formatada)
    
    if palavra_secreta == palavra_formatada:
        os.system('cls')  # Limpando o terminal
        print(f'< PARABÉNS!!! >\nA palavra era: {palavra_secreta}\nTentativas: {tentativas}')
        quit()
