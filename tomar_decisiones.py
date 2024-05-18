
if 10 == 5:
    print("Es correcto")
else:
    print("Esto no es correcto")

mascota = "perro"

if mascota == "gato":
    print("Tienes un gato")
elif mascota == "perro":
    print("Tienes un perro")
else:
    print("No se que animales tienes")

edad = 18
calificacion = 10
if edad >= 18:
    print("Eres mayor de edad")
    if calificacion >= 10:
        print("Tu calificación es excelente")
    elif calificacion >=7:
        print("Muy bien")
    elif calificacion >=5:
        print("Puedes mejorar")
    else:
        print("Reprobaste")
else:
    print("Eres menor de edad")

###EXAMEN####
num1 = int(input("Ingresa un número:"))
num2 = int(input("Ingresa otro número:"))

if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num2 > num1:
    print(f"{num2} es mayor que {num1}")
else:
    print(f"{num1} y {num2} son iguales")



edad = 16
tiene_licencia = False

"Puedes conducir"

"No puedes conducir aún. Debes tener 18 años y contar con una licencia"

"No puedes conducir. Necesitas contar con una licencia"

if edad < 18:
    print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")
elif edad >= 18 and tiene_licencia==False:
    print("No puedes conducir. Necesitas contar con una licencia")
else:
    print("Puedes conducir")




habla_ingles = True
sabe_python = False

"Cumples con los requisitos para postularte"

"Para postularte, necesitas saber programar en Python y tener conocimientos de inglés"

"Para postularte, necesitas tener conocimientos de inglés"

"Para postularte, necesitas saber programar en Python"

if sabe_python==True and habla_ingles==True:
    print("Cumples con los requisitos para postularte")
elif sabe_python==True and habla_ingles==False:
    print("Para postularte, necesitas tener conocimientos de inglés")
elif sabe_python==False and habla_ingles==True:
    print("Para postularte, necesitas saber programar en Python")
else:
    print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")