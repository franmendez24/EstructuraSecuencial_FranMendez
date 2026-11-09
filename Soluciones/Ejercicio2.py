#Fran Mendez Gonzalez
#Ejercicio2
#Calcular el perímetro y área de un rectángulo dada su base y su altura.
#3/11/2026

base = float(input("Base del rectángulo: "))
altura = float(input("Altura del rectángulo: "))

perimetro = 2 * (base + altura)
area = base * altura

print(f"Perímetro: {perimetro:.2f}")
print(f"Área: {area:.2f}")