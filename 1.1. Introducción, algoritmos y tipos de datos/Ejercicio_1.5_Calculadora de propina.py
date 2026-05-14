
print("Bienvenidos al Programa de Calcular Propinas")

cuenta = float(input("Ingresa el Valor Total de la Cuenta: "))
porcentaje = float(input("Porcentaje de Propina (10, 15, 20): "))

monto_propina = cuenta * (porcentaje / 100)

total_pagar = cuenta + monto_propina

print(f"Desglose Completo")
print(f"Cuenta: ${cuenta:.2f}")
print(f"Propina ({porcentaje}%): ${monto_propina:.2f}")
print(f"Total a pagar: ${total_pagar:.2f}")
print("Gracias por Usar el Programa de Calcular Propinas.")
