import streamlit as st
import pandas as pd

# Carga el archivo xlsx
file_path = 'datos_distancia.xlsx'  # Reemplaza con la ruta de tu archivo xlsx
data = pd.read_excel(file_path)

# Crea una lista de diccionarios, cada uno con los datos de una fila
dropdown_options = data.to_dict('records')

# Crea un menú desplegable para seleccionar una fila del archivo xlsx
selected_option = st.selectbox('Selecciona una fila:', dropdown_options)

# Muestra los detalles de la opción seleccionada
st.write('Detalles de la fila seleccionada:')
st.json(selected_option)
