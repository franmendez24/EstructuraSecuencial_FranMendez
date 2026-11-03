#Fran Mendez Gonzalez
#Ejercicio14
#Dado un número de dos cifras, diseñe un algoritmo que permita obtener el
#número invertido. Ejemplo, si se introduce 23 que muestre 32.
#3/11/2026

numero = int(input("Introduce un número de dos cifras (10-99): "))

if 10 <= numero <= 99:
    decenas = numero // 10
    unidades = numero % 10
    # Se muestra con dos cifras para que 10 se invierta como 01
    print(f"El número invertido es {unidades}{decenas}")
else:
    print("El número no tiene dos cifras")