nombres = ['Carlos','Eduardo','Adruskary']
edades = [25,18,52]
ciudades = ['Caracas','Maracay','Yaracuy']
#integrar dos listas en una
combinados = list(zip(nombres,edades,ciudades))

print(combinados)

for nombre,edad,ciudad in combinados:
    print(f"{nombre} tiene {edad} años y vive en {ciudad}")

###EXAMEN###

capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]
combinados = list(zip(paises,capitales))

for pais,capital in combinados:
    print(f"La capital de {pais} es {capital}")


marcas = ['Nike','Toyota','Iphone']
productos = ['Zapatos','Carros','Telefonos']
mi_zip = zip(marcas,productos)



español = ['uno','dos','tres','cuatro','cinco']
portugues = ['um','dois','três','quatro','cinco']
ingles = ['one','two','three','four','five']
numeros = list(zip(español,portugues,ingles))
print(numeros)