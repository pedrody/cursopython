contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
       print('*')
       continue

    if contador >= 10 and contador <= 27:
        print('*')
        continue

    print(contador)
    if contador == 40:
        break
    
print('Acabou')

