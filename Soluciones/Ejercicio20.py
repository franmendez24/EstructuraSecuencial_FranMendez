#Fran Mendez Gonzalez
#Ejercicio20
#Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos)
#después de pedirnos cuantas monedas tenemos (de 2€, 1€, 50 céntimos, 20
#céntimos o 10 céntimos).
#3/11/2026

monedas_2e = int(input("Monedas de 2 €: "))
monedas_1e = int(input("Monedas de 1 €: "))
monedas_50c = int(input("Monedas de 50 céntimos: "))
monedas_20c = int(input("Monedas de 20 céntimos: "))
monedas_10c = int(input("Monedas de 10 céntimos: "))

# Trabajamos en céntimos para evitar errores con decimales
total_centimos = (monedas_2e * 200 + monedas_1e * 100 + monedas_50c * 50
                  + monedas_20c * 20 + monedas_10c * 10)

euros = total_centimos // 100
centimos = total_centimos % 100

print(f"Tienes {euros} euros y {centimos} céntimos")