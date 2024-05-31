import streamlit as st
import pandas as pd

# Carga el archivo xlsx
file_path = 'datos_distancia.xlsx'  # Reemplaza con la ruta de tu archivo xlsx
data = pd.read_excel(file_path)

# Crea una lista de diccionarios, cada uno con los datos de una fila
dropdown_options = data.to_dict('records')

# Crea un menú desplegable para seleccionar una fila del archivo xlsx
#selected_option = st.selectbox('Selecciona una fila:', dropdown_options)

# Muestra los detalles de la opción seleccionada
#st.write('Detalles de la fila seleccionada:')
#st.json(selected_option)

# Crea una tabla para mostrar los datos de todas las filas seleccionadas
selected_rows = st.multiselect('Selecciona filas adicionales:', dropdown_options)
if selected_rows:
    st.write('Tabla de datos acumulados:')
    st.table(pd.DataFrame(selected_rows))

# Añade un botón para deseleccionar todas las filas
if st.button('Deseleccionar todas las filas'):
    selected_rows = []

# Muestra los detalles de las filas deseleccionadas
#if selected_rows:
#    st.write('Filas deseleccionadas:')
 #   st.json(selected_rows)
