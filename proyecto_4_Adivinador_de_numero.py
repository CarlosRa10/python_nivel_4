from random import *

intentos = 0
estimado = 0
numero_secreto = randint(1,100)
nombre_usuario = input('Dime tu nombre: ')

print(f"Hola {nombre_usuario}, he pensado un numero entre 1 y el 100\nTienes 8 intentos para adivinar ")

while intentos < 8:
    estimado = int(input('Cual es el numero: '))
    intentos += 1
    if estimado not in range(1,101):
        print('Tu numero no se encuentra en el rango del 1 al 100')
    elif estimado < numero_secreto:
        print('Mi numero es mas alto')
    elif estimado > numero_secreto:
        print('Mi numero es mas bajo')
    else:
        print(f"Felicitaciones {nombre_usuario}! Has adivinado en {intentos} intentos.")
        break
if estimado != numero_secreto:
    print(f"Lo siento, se han agotados los intentos. El numero secreto era {numero_secreto}")