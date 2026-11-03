#Fran Mendez Gonzalez
#Ejercicio17
#Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. El
#tiempo de viaje hasta llegar a otra ciudad B es de T segundos. Escribir un
#algoritmo que determine la hora de llegada a la ciudad B.
#3/11/2026

hh = int(input("Hora de salida - horas: "))
mm = int(input("Hora de salida - minutos: "))
ss = int(input("Hora de salida - segundos: "))
t = int(input("Tiempo de viaje en segundos: "))

# Pasamos todo a segundos y sumamos
salida_en_segundos = hh * 3600 + mm * 60 + ss
llegada_en_segundos = salida_en_segundos + t

# Si se pasa de medianoche, contamos los días de más
dias = llegada_en_segundos // 86400
llegada_en_segundos = llegada_en_segundos % 86400

horas = llegada_en_segundos // 3600
minutos = (llegada_en_segundos % 3600) // 60
segundos = llegada_en_segundos % 60

print(f"Hora de llegada a la ciudad B: {horas:02d}:{minutos:02d}:{segundos:02d}")
if dias > 0:
    print(f"(Llega {dias} día(s) después de la salida)")