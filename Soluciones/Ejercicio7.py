#Fran Mendez Gonzalez
#Ejercicio5
#Realiza un programa que reciba una cantidad de minutos y muestre por pantalla
#a cuantas horas y minutos corresponde. Por ejemplo: 1000 minutos son 16 horas y 40 minutos.
#3/11/2026

total_minutos = int(input("Introduce una cantidad de minutos: "))

horas = total_minutos // 60
minutos = total_minutos % 60

print(f"{total_minutos} minutos son {horas} horas y {minutos} minutos")
