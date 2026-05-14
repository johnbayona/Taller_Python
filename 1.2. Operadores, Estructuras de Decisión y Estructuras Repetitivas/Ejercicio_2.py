
print("Bienvenido al programa de Calcular descuentos")

compra = float(input("Ingrese el Valor de la Compra: "))

descuento = 0

if compra  > 100000:
    descuento = compra * 0.15
elif compra > 50000:
    descuento = compra * 0.1
elif compra > 20000:
    descuento = compra * 0.5
else:
    descuento = 0
total = compra - descuento

print(f"Descuento: {descuento} ")
print(f"El Total a Pagar es de: {total}")