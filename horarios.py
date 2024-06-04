import streamlit as st
import pandas as pd
import numpy as np

# Carga el archivo xlsx
file_path = 'datos_distancia.xlsx'  # Reemplaza con la ruta de tu archivo xlsx
data = pd.read_excel(file_path)

# Elimina la primera columna (índice 0)
data.drop(data.columns[0], axis=1, inplace=True)

# Selecciona solo las columnas deseadas
selected_columns = ['client_id', 'client_id_destino', 'distancia', 'unidad_metrica', 'tiempo', 'unidad_temporal']
data_filtered = data[selected_columns]

# Reemplaza los valores None con 0
data_filtered.fillna(0, inplace=True)

# Convierte la columna "tiempo" a números (si es posible)
data_filtered['tiempo'] = pd.to_numeric(data_filtered['tiempo'], errors='coerce')

# Crea una lista de diccionarios, cada uno con los datos de una fila
dropdown_options = data_filtered.to_numpy().tolist()

# Organiza los elementos en dos columnas
left_column, right_column = st.columns([1, 1.5], gap="large")

# En la columna izquierda, muestra el menú desplegable
with left_column:
    selected_rows = st.multiselect('Selecciona comunidades a insertar:', dropdown_options)

# En la columna derecha, muestra la tabla con las filas seleccionadas
with right_column:
    if selected_rows:
        st.write('Comunidades seleccionadas:')
        st.dataframe(pd.DataFrame(selected_rows, columns=selected_columns), width=None)

        # Suma los datos de la columna "tiempo"
        #total_tiempo = sum(row['tiempo'] for row in selected_rows)
        #st.write(f'Tiempo total: **{total_tiempo}**')
    
    # Calcula la suma de la columna "tiempo" para las filas seleccionadas
    if selected_rows:
        tiempo_sum = sum(row['tiempo'] for row in selected_rows)
        st.write(f'Suma de tiempo: {tiempo_sum:.2f}')

