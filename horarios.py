import pandas as pd
import streamlit as st
import os

# Cargar el archivo XLSX
@st.cache
def load_data():
    df = pd.read_excel('datos_distancia.xlsx')
    return df

df = load_data()

# Crear una lista desplegable con todos los valores de la fila
selected_row = st.selectbox('Selecciona una fila:', df.index)

# Filtrar los datos según la fila seleccionada
filtered_data = df.loc[selected_row]

# Mostrar los datos en una tabla
st.table(filtered_data)

# Acumular los datos seleccionados en una tabla
st.write('Datos seleccionados:')
st.dataframe(filtered_data)


