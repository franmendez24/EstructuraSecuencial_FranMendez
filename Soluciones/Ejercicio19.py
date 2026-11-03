#Fran Mendez Gonzalez
#Ejercicio19
#Escribir un algoritmo para calcular la nota final de un estudiante, considerando
#que: por cada respuesta correcta 5 puntos, por una incorrecta -1 y por respuestas
#en blanco 0. Imprime el resultado obtenido por el estudiante.
#3/11/2026

correctas = int(input("Número de respuestas correctas: "))
incorrectas = int(input("Número de respuestas incorrectas: "))
en_blanco = int(input("Número de respuestas en blanco: "))

nota = correctas * 5 + incorrectas * (-1) + en_blanco * 0

print(f"La nota final del estudiante es: {nota} puntos")