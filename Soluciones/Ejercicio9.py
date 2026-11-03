#Fran Mendez Gonzalez
#Ejercicio9
#Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente
#desea saber cuánto deberá pagar finalmente por su compra
#3/11/2026

total_compra = float(input("Total de la compra: "))

descuento = total_compra * 0.15
total_a_pagar = total_compra - descuento

print(f"Descuento (15%): {descuento:.2f}")
print(f"Total a pagar: {total_a_pagar:.2f}")