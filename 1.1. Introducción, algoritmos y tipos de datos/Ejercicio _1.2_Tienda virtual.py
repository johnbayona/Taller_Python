
print("Bienvenidos al programa de Tienda Virtual")


producto = input("Ingrese el Nombre de producto que deseas comprar: ")
precio = float(input("Ingresa el valor del producto: "))
cantidad = int(input(" Ingrese la cantidad que deseas comprar: "))

subtotal = precio * cantidad
iva = subtotal * 0.19
total = subtotal + iva

print(f"producto {producto}")
print(f"subtotales: ${subtotal:.2f}")
print(f"el iva es de $:{iva:.2f}")
print(f"el valor total es: ${total:.2f}")
print("Gracias por Comprar en Nuestra Tienda Virtual")