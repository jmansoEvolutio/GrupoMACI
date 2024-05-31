import pandas as pd
import streamlit as st
import os

# Cargar el archivo XLSX
@st.cache
def cargar_datos():
    df = pd.read_excel("datos_distancia.xlsx")
    return df

df = cargar_datos()

# Crear una lista desplegable con los valores concatenados de cada fila
fila_seleccionada = st.selectbox("Selecciona una fila:", df.index)
valores_fila = df.iloc[fila_seleccionada].values
valores_concatenados = " | ".join(map(str, valores_fila))

st.write(f"Valores seleccionados: {valores_concatenados}")

# Crear una tabla para mostrar los datos seleccionados
st.write("Datos seleccionados:")
st.table(df.loc[df.index.isin(range(fila_seleccionada + 1))])

