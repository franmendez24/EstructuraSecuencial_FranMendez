#Fran Mendez Gonzalez
#Ejercicio16
#Dos vehículos viajan a diferentes velocidades (v1 y v2) y están distanciados por
#una distancia d. El que está detrás viaja a una velocidad mayor. Se pide hacer un
#algoritmo para ingresar la distancia entre los dos vehículos (km) y sus respectivas
#velocidades (km/h) y con esto determinar y mostrar en que tiempo (minutos)
#alcanzará el vehículo más rápido al otro.
#3/11/2026

distancia = float(input("Distancia entre los vehículos (km): "))
v1 = float(input("Velocidad del vehículo de atrás, el más rápido (km/h): "))
v2 = float(input("Velocidad del vehículo de delante (km/h): "))

if v1 <= v2:
    print("El vehículo de atrás debe ir más rápido que el de delante para alcanzarlo.")
else:
    # Velocidad a la que se acercan = v1 - v2
    tiempo_horas = distancia / (v1 - v2)
    tiempo_minutos = tiempo_horas * 60
    print(f"El vehículo más rápido alcanzará al otro en {tiempo_minutos:.2f} minutos")