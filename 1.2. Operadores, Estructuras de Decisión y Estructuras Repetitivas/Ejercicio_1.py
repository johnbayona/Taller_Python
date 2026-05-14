
print("Bienvenido al Programa de Clasificador de Edades")

edad = int(input("Ingrese su edad: "))

if edad >= 0 and edad <= 12:
    print("Esta persona es: un niño")
elif edad >= 13 and edad <= 17:
    print("la persona es: Adolecente") 
elif edad >= 18 and edad <= 64:
    print("Esta persona es un: Adulto")
else: 
    edad >= 65
    print("Esta persona es: Adulto Mayor")

