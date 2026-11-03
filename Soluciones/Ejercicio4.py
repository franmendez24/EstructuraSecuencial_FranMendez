#Fran Mendez Gonzalez
#Ejercicio3
#Dados dos números, mostrar la suma, resta, división y multiplicación de ambos
#3/11/2026

a = float(input("Primer número: "))
b = float(input("Segundo número: "))

print(f"Suma: {a + b}")
print(f"Resta: {a - b}")
print(f"Multiplicación: {a * b}")
if b != 0:
    print(f"División: {a / b}")
else:
    print("División: no se puede dividir entre 0")