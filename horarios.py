import streamlit as st
import pandas as pd

# Carga el archivo xlsx
file_path = 'datos_distancia.xlsx'  # Reemplaza con la ruta de tu archivo xlsx
data = pd.read_excel(file_path)

# Crea una lista de diccionarios, cada uno con los datos de una fila
dropdown_options = data.to_dict('records')

# Organiza los elementos en dos columnas
left_column, right_column = st.columns(2)

# En la columna izquierda, muestra el menú desplegable
with left_column:
    selected_rows = st.multiselect('Selecciona filas adicionales:', dropdown_options)

# En la columna derecha, muestra la tabla con las filas seleccionadas
with right_column:
    if selected_rows:
        st.write('Tabla de datos acumulados:')
        st.dataframe(pd.DataFrame(selected_rows), width=None)  # Cambio a st.dataframe()

        # Suma los datos de la columna "tiempo"
        total_tiempo = sum(row['tiempo'] for row in selected_rows)
        st.write(f'Tiempo total acumulado: **{total_tiempo}**')
