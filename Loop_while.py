monedas = 5

while monedas > 0:
    print(f"Tengo {monedas} monedas")
    monedas -= 1
else:
    print("No tengo mas dinero")

respuesta = 's'

while respuesta == 's':
    respuesta = input("Quieres Seguir? (s/n)").lower()
else:
    print("Gracias!!")

#pass es pasar,break es interrumpir, continue es continuar

nombre = input("Tu nombre: ")

for letra in nombre:
    if letra == 'y':
        break
    print(letra)

###EXAMEN###

numero = 10

while numero >= 0:
    print(numero)
    numero -= 1

numero = 50


while numero >= 0:
    if numero % 5 == 0:
        print(numero)
        numero -= 1
    else:
        numero -= 1

lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]

for lista in lista_numeros:
    if lista < 0:
        break
    else:
        print(lista)
