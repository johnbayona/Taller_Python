
print("Bienvenido al Programa Validar Contraseña")

contraseña = input("Ingrese la contraseña")


intentos = 0
contraseña = "python123"

while contraseña != contraseña:
    intentos += 1
    intentos = intentos + 1
    print("Contraseña Incorrecta")

contraseña = input("Ingrese la Contraseña Nuevamente")
intentos += 1
print("Contraseña Correcta")
print(f"Cantidad de Intentos {intentos}")
