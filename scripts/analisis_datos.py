
import pandas as pd
import matplotlib.pyplot as plt
import os

# 1. Cargar los datos usando rutas relativas
# Sube un nivel desde /scripts y entra a /datos
ruta_csv = os.path.join('..', 'datos', 'sales_sample_2024.csv')
df = pd.read_csv(ruta_csv)

# Convertir la columna de fecha a formato datetime
df['sales_date'] = pd.to_datetime(df['sales_date'])
df = df.sort_values('sales_date')

# 2. Procesamiento de datos
ventas_totales = df['sales_amount'].sum()

# Encontrar la fecha donde se registró el monto más alto de venta
dia_max_ventas = df.loc[df['sales_amount'].idxmax(), 'sales_date'].strftime('%Y-%m-%d')
monto_max_ventas = df['sales_amount'].max()

# 3. Mostrar el reporte en consola
print(f"\n==========================================")
print(f"       REPORTE DE ANALÍTICA COMERCIAL     ")
print(f"==========================================")
print(f"Ingresos Totales del Periodo : ${ventas_totales:,}")
print(f"Día con Mayor Venta          : {dia_max_ventas} (${monto_max_ventas:,})")
print(f"Total de Registros Evaluados : {len(df)} transacciones.")
print(f"==========================================\n")

# 4. Generar gráfico de evolución temporal y guardarlo en /resultados
plt.figure(figsize=(12, 6))
plt.plot(df['sales_date'], df['sales_amount'], marker='o', linestyle='-', color='#2ca02c', markersize=4)

plt.title('Evolución Temporal de Montos de Venta (sales_amount)', fontsize=14, fontweight='bold')
plt.xlabel('Fecha de Venta (sales_date)', fontsize=12)
plt.ylabel('Monto en Unidades / Dinero', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.xticks(rotation=45)
plt.tight_layout()

# Guardar el gráfico subiendo un nivel y entrando a /resultados
ruta_grafico = os.path.join('..', 'resultados', 'grafico_ventas.png')
plt.savefig(ruta_grafico)
print(f"[OK] Gráfico exportado exitosamente a: {ruta_grafico}")
