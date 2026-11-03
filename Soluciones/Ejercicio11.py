#Fran Mendez Gonzalez
#Ejercicio11
#Pide al usuario dos números y muestra la “distancia” entre ellos (el valor absoluto
#de su diferencia, de modo que el resultado sea siempre positivo)
#3/11/2026

a = float(input("Primer número: "))
b = float(input("Segundo número: "))

distancia = abs(a - b)

print(f"La distancia entre {a} y {b} es {distancia}")