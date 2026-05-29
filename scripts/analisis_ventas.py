import pandas as pd
import matplotlib.pyplot as plt

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

# Producto más vendido
producto_mas_vendido = datos.groupby("producto")["cantidad"].sum()

print("\nPRODUCTO MÁS VENDIDO:")
print(producto_mas_vendido)

# Crear gráfico
producto_mas_vendido.plot(kind="bar")

# Título y etiquetas
plt.title("Ventas por Producto")
plt.xlabel("Producto")
plt.ylabel("Cantidad Vendida")

# Guardar gráfico
plt.savefig("../resultados/grafico_ventas.png")

# Mostrar gráfico
plt.show()
