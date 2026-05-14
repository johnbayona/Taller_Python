
print ("Bienvenido al programa de Manupulacion de Texto")

frase = str(input("Ingrese la frase a Manipular: "))

print(f"Mayusculas {frase.upper()}")
print(f"Minusculas {frase.lower()}")

palabras = frase.split()

print(f"Numero de Palabras: {len(palabras)}")
print(f"Primera Palabra: {palabras[0]}")
print(f"Ultima Palabra: {palabras[-1]}")

print("Gracias por usar Nuestro Programa de Manipulacion de Texto.")



