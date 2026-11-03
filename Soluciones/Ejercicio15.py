#Fran Mendez Gonzalez
#Ejercicio15
#Dadas dos variables numéricas A y B, que el usuario debe teclear, se pide realizar
#un algoritmo que intercambie los valores de ambas variables y muestre cuánto
#valen al final las dos variables.
#3/11/2026

a = float(input("Valor de A: "))
b = float(input("Valor de B: "))

print(f"Antes del intercambio: A = {a}, B = {b}")

# Intercambio con una variable auxiliar
auxiliar = a
a = b
b = auxiliar

print(f"Después del intercambio: A = {a}, B = {b}")