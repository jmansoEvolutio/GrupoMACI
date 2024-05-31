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
    #selected_option = st.selectbox('Selecciona una fila:', dropdown_options)
    #st.write('Detalles de la fila seleccionada:')
    #st.json(selected_option)

# En la columna derecha, muestra la tabla con las filas seleccionadas
with right_column:
    #selected_rows = st.multiselect('Selecciona filas adicionales:', dropdown_options)
    if selected_rows:
        st.write('Tabla de datos acumulados:')
        st.table(pd.DataFrame(selected_rows))
