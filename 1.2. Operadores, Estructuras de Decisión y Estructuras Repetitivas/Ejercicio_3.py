print("Bienvenido al Programa Contador de Pares")

numero = int(input("Ingrese el Numero a Contar: "))

contador = 0

for i in range(1, numero +1 ):

    if i % 2 == 0:
        print(i)
        contador += 1
print("La Cantidad de numeros pares es: ",contador)