import pandas as pd

# Leer archivo CSV
datos = pd.read_csv("datos/ventas.csv")

# Mostrar datos
print("DATOS DE VENTAS")
print(datos)

# Crear columna total
datos["total"] = datos["cantidad"] * datos["precio"]

# Calcular ventas totales
ventas_totales = datos["total"].sum()

print("\nVENTAS TOTALES:")
print(ventas_totales)
