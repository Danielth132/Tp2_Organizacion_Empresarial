
# TP2: Organización Empresarial - Célula de Desarrollo (Escenario B)

Este proyecto implementa un pipeline automatizado de analítica comercial para el procesamiento de datos de ventas.

## 📊 Estructura del Repositorio
* `/datos`: Carpeta contenedora del dataset de origen (ignorado por Git mediante .gitignore).
* `/scripts`: Código fuente en Python para el procesamiento de datos.
* `/resultados`: Gráficos e informes de analítica exportados.

## 📋 Requisitos del Dataset y Fuente de Datos
Debido a buenas prácticas de desarrollo e infraestructura, el archivo original de datos está oculto en este repositorio. Para poder ejecutar este proyecto, el usuario debe descargar el dataset manualmente.

* **Fuente de descarga oficial:** [Hacé clic acá para descargar el Dataset de Ventas](https://gist.github.com/khanusama20/ee33c2869dd5cf3cebdf020be1ca43f6)
* **Instrucciones:** Una vez descargado, el archivo debe guardarse obligatoriamente dentro de la carpeta `/datos` con el nombre `sales_sample_2024.csv`.

### Diccionario de Datos
* `id`: Identificador numérico entero de la transacción.
* `sales_date`: Fecha de la venta (Formato: `YYYY-MM-DD`).
* `sales_amount`: Monto total de la venta (Valor entero).

## 🚀 Instrucciones de Ejecución
Una vez colocado el archivo CSV en la carpeta `/datos`, ejecute desde la raíz del proyecto para correrlo de forma local en cualquier PC:
```bash
cd scripts
python analisis_datos.py
