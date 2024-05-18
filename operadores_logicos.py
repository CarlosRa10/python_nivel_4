mi_bool = (8 < 5) and (3 < 6)#Ambas tienen que ser verdadera
print(mi_bool)
mi_bool = (1 == 10) or (3 == 3) #le da igual solo le interesa que una de las dos sea verdadera
print(mi_bool)
texto = "Esta frase en breve"
mi_bool = 'frase' in texto and 'breve' in texto
print(mi_bool)
mi_bool = not 'a' == 'a'
print(mi_bool)


###EXAMEN####
num1 = 36
num2 = 36
num3 = 48
mi_bool = num1 > num2 and num1 < num3

num1 = 36
num2 = 36
num3 = 48
mi_bool = num1 > num2 or num1 < num3

frase = "Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan"
palabra1 = "éxito"
palabra2 = "tecnología"
mi_bool =  (palabra1 not in frase) and (palabra2 not in frase)
print(mi_bool)
