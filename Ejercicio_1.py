peso = float(input("Ingrese tu peso corporal: "))
altura = float(input("Ingrese tu altura: "))

IMC = (peso / altura **2)

print (f"Tu IMC es: {IMC:.2F}")

if IMC < 18.5: print("Bajo peso")
elif 18.5 <= IMC <= 24.9: print("Peso normal")
elif 25 >= IMC <= 29.9: print("Sobrepeso")
else : print("Obesidad")
