#Fran Mendez Gonzalez
#Ejercicio12
#Pide al usuario dos pares de números x1,y2 y x2,y2, que representen dos puntos
#en el plano. Calcula y muestra la distancia entre ellos.
#3/11/2026

import math

x1 = float(input("x1: "))
y1 = float(input("y1: "))
x2 = float(input("x2: "))
y2 = float(input("y2: "))

distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print(f"La distancia entre ({x1}, {y1}) y ({x2}, {y2}) es {distancia:.2f}")
