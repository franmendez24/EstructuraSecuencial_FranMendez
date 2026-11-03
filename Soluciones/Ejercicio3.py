#Fran Mendez Gonzalez
#Ejercicio3
#Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
#3/11/2026

import math

cateto1 = float(input("Primer cateto: "))
cateto2 = float(input("Segundo cateto: "))

hipotenusa = math.sqrt(cateto1 ** 2 + cateto2 ** 2)

print(f"La hipotenusa mide {hipotenusa:.2f}")