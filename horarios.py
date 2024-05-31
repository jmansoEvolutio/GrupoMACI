import pandas as pd
import streamlit as st
import os

# Cargar el archivo XLSX
@st.cache
def load_data():
    df = pd.read_excel('datos_distancia.xlsx')
    return df

df = load_data()

# Crear una lista desplegable con valores únicos de la columna 'client_id'
client_ids = df['client_id'].unique()
selected_client_id = st.selectbox('Selecciona un client_id:', client_ids)

# Filtrar los datos según el client_id seleccionado
filtered_data = df[df['client_id'] == selected_client_id]

# Mostrar los datos en una tabla
st.table(filtered_data)

# Acumular los datos seleccionados en una tabla
st.write('Datos seleccionados:')
st.dataframe(filtered_data)

