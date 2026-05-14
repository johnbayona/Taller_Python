
print("Bienvenido al Programa de Conversion de Tiempo")

total_minutos = int(input("Ingrese los Minutos a Convertir: "))

horas = total_minutos // 60
minutos_restantes = total_minutos % 60

print(f"{total_minutos} Minutos Equivalen a {horas} Horas y {minutos_restantes} Minutos. ")