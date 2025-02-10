#Loops es un bucle que recorre las posicion de cada elemento
lista = ['a','b','c']
for letra in lista:
    numero_letra = lista.index(letra) +1
    print(f"La letra {numero_letra}: {letra}")


lista = ['juan', 'carlos','eduardo','messi','ronaldo','valentina','laura','luis']
for nombre in lista:
    if nombre.startswith('l'):
        print(nombre)
    else:
        print(f"{nombre} no empieza con 'l'")


numeros = [1,2,3,4,5]
mi_valor = 0

for numero in numeros:
    mi_valor = mi_valor + numero
    print(mi_valor)
print(mi_valor)

palabra = 'python es genial'
for letra in palabra:
    print(letra)
print("\n")
for letra in 'JavaScript':
    print(letra)

print("\n")
for numero in [1,2,3,4]:
    print(numero)

print("\n")
for objeto in [[1, 2, 3, 4], [5, 6, 7, 8]]:
    print(objeto)
print("\n")
for a,b,c,d in [[1, 2, 3, 4], [5, 6, 7, 8]]:
    print(a)


dic = {'calve1':'a','clave2':'b','clave3':'c'}
for item in dic.items():#para ver los valores es .values
    print(item)

dic = {'calve1':'a','clave2':'b','clave3':'c'}
for a,b in dic.items():
    print(a,b)

###EXAMEN###

alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]
for alumno in alumnos_clase:
    print("Hola " + alumno)


lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_numeros = 0
for numero in lista_numeros:
    suma_numeros = suma_numeros + numero
    print(numero)
    print(suma_numeros)

#Suma de pares y suma de impares

lista_numeros = [1, 5, 8, 7, 6, 8, 2, 5, 2, 6, 4, 8, 5, 9, 8, 3, 5, 4, 2, 5, 6, 4]
suma_pares = 0
suma_impares = 0

for numero in lista_numeros:
    if numero % 2 == 0:
        suma_pares = suma_pares + numero
    else:
        numero % 2 == 1
        suma_impares = suma_impares + numero

print(suma_pares)
print(suma_impares)
