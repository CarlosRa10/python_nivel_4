from random import *

aleatorio = randint(1,50)#Entero
print(aleatorio)

aleatorio = round(uniform(1,50),1)#Float
print(aleatorio)

aleatorio = random()
print(aleatorio)

colores = ['azul','rojo','verde','amarillo']
aleatorio = choice(colores)#para elegir de manera random string en una lista o colección
print(aleatorio)


numeros = list(range(5,50,5))
shuffle(numeros)#Barajear.... solo modifica en el lugar 
print(numeros)

###EXAMEN###

from random import randint

aleatorio = randint(1,10)
print(aleatorio)


from random import random
aleatorio = random()
print(aleatorio)


from random import choice
nombres = ["Carlos", "Julia", "Nicole", "Laura", "Mailen"]
sorteo = choice(nombres)
print(sorteo)