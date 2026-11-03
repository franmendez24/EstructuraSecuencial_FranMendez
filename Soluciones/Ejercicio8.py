#Fran Mendez Gonzalez
#Ejercicio8
#Un vendedor recibe un sueldo base más un 10% extra por comisión de sus ventas,
#el vendedor desea saber cuánto dinero obtendrá por concepto de comisiones por
#las tres ventas que realiza en el mes y el total que recibirá en el mes tomando en
#cuenta su sueldo base y comisiones.
#3/11/2026

sueldo_base = float(input("Sueldo base: "))
venta1 = float(input("Importe de la primera venta: "))
venta2 = float(input("Importe de la segunda venta: "))
venta3 = float(input("Importe de la tercera venta: "))

comisiones = (venta1 + venta2 + venta3) * 0.10
total = sueldo_base + comisiones

print(f"Comisiones del mes: {comisiones:.2f}")
print(f"Total a recibir en el mes: {total:.2f}")


