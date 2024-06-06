palabra = 'python'
lista = []

for letra in palabra:
    lista.append(letra)

print(lista)

lista2 = [letra for letra in palabra]
print(lista2)

lista3 = [letra for letra in 'Java']
print(lista3)

lista4 = [numero for numero in range(0,11,2)]
print(lista4)

lista5 = [numero / 2 for numero in range(0,11,2)]
print(lista5)

lista6 = [numero for numero in range(0,11,2) if numero * 2 > 10 ]
print(lista6)

lista7 = [numero if numero * 2 > 10 else 'NO' for numero in range(0,11,2)  ]
print(lista7)

pies = [10,20,30,40,50]
metros = [i / 3.281 for i in pies ]
print(metros)

###EXAMEN###

valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_cuadrado = [valor ** 2 for valor in valores]
print(valores_cuadrado)

valores = [1, 2, 3, 4, 5, 6, 9.5] 
valores_pares = [valor for valor in valores if valor % 2 == 0]
print(valores_pares)

temperatura_fahrenheit = [32, 212, 275]
grados_celsius = [(i-32)*(5/9) for i in temperatura_fahrenheit]
print(grados_celsius)