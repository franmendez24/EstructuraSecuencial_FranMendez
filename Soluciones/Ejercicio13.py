#Fran Mendez Gonzalez
#Ejercicio13
#Realizar un algoritmo que lea un número y que muestre su raíz cuadrada y su raíz
#cúbica. Python3 no tiene ninguna función predefinida que permita calcular la raíz
#cúbica, ¿Cómo se puede calcular?
#3/11/2026

import math

numero = float(input("Introduce un número: "))

# Raíz cuadrada (solo existe en los reales para números >= 0)
if numero >= 0:
    print(f"Raíz cuadrada: {math.sqrt(numero):.4f}")
else:
    print("Raíz cuadrada: no existe para números negativos")

# Raíz cúbica: elevar a 1/3. Para negativos se calcula con el valor absoluto
# y se vuelve a poner el signo, porque (-8) ** (1/3) daría un número complejo.
if numero >= 0:
    raiz_cubica = numero ** (1 / 3)
else:
    raiz_cubica = -((-numero) ** (1 / 3))

print(f"Raíz cúbica: {raiz_cubica:.4f}")