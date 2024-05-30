import pandas as pd
import streamlit as st
import os

# Cargar el archivo XLSX (reemplaza 'mi_archivo.xlsx' con la ruta de tu archivo)
archivo_xlsx = 'datos_distancia.xlsx'
df = pd.read_excel(archivo_xlsx)

# Crear una lista desplegable con las columnas del DataFrame
#columna_seleccionada = st.selectbox("Selecciona una columna:", df.columns)

# Filtrar los datos según la columna seleccionada
#datos_filtrados = df[columna_seleccionada]

# Mostrar los datos filtrados en una tabla
#st.write(f"Datos de la columna '{columna_seleccionada}':")
#st.write(datos_filtrados)

