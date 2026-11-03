#Fran Mendez Gonzalez
#Ejercicio10
#Un alumno desea saber cuál será su calificación final en la materia de Algoritmos.
#Dicha calificación se compone de los siguientes porcentajes:
# 55% del promedio de sus tres calificaciones parciales.
# 30% de la calificación del examen final.
# 15% de la calificación de un trabajo final.
#3/11/2026

parcial1 = float(input("Calificación del primer parcial: "))
parcial2 = float(input("Calificación del segundo parcial: "))
parcial3 = float(input("Calificación del tercer parcial: "))
examen_final = float(input("Calificación del examen final: "))
trabajo_final = float(input("Calificación del trabajo final: "))

promedio_parciales = (parcial1 + parcial2 + parcial3) / 3

calificacion_final = (promedio_parciales * 0.55
                      + examen_final * 0.30
                      + trabajo_final * 0.15)

print(f"Promedio de los parciales: {promedio_parciales:.2f}")
print(f"Calificación final en Algoritmos: {calificacion_final:.2f}")