
def area_cuadrado(lado):

    return lado * lado


def area_rectangulo(base, altura):

    return base * altura


def area_triangulo(base, altura):

    return (base * altura) / 2


def area_circulo(radio):

    pi = 3.14159

    return pi * (radio * radio)


while True:

    print("\n--- MENÚ ---")
    print("1. Área cuadrado")
    print("2. Área rectángulo")
    print("3. Área triángulo")
    print("4. Área círculo")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":

        lado = float(input("Ingrese el lado: "))

        resultado = area_cuadrado(lado)

        print("Área:", resultado)

    elif opcion == "2":

        base = float(input("Ingrese la base: "))
        altura = float(input("Ingrese la altura: "))

        resultado = area_rectangulo(base, altura)

        print("Área:", resultado)

    elif opcion == "3":

        base = float(input("Ingrese la base: "))
        altura = float(input("Ingrese la altura: "))

        resultado = area_triangulo(base, altura)

        print("Área:", resultado)

    elif opcion == "4":

        radio = float(input("Ingrese el radio: "))

        resultado = area_circulo(radio)

        print("Área:", resultado)

    elif opcion == "5":

        print("Programa finalizado")
        break

    else:

        print("Opción inválida")