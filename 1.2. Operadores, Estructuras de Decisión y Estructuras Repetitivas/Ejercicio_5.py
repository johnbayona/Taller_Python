
print("Bienvenido al Programa Menu de Opciones")

while True:
    print("\n--- MENÚ ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":

        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        resultado = num1 + num2

        print("Resultado:", resultado)

    elif opcion == "2":

        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        resultado = num1 - num2

        print("Resultado:", resultado)

    elif opcion == "3":

        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        resultado = num1 * num2

        print("Resultado:", resultado)

    elif opcion == "4":

        print("Saliendo del programa...")
        break

    else:

        print("Opción inválida")