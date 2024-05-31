import pandas as pd
import streamlit as st
import os

# Cargar el archivo XLSX
@st.cache
def cargar_datos():
    df = pd.read_excel("datos_distancia.xlsx")
    return df

df = cargar_datos()

# Crear una lista desplegable con los IDs de cliente
cliente_seleccionado = st.selectbox("Selecciona un cliente:", df["client_id"])

# Filtrar los datos según el cliente seleccionado
datos_filtrados = df[df["client_id"] == cliente_seleccionado]

# Mostrar los datos en una tabla
st.write("Datos del cliente seleccionado:")
st.write(datos_filtrados)
