#import pandas as pd
#import streamlit as st
#import os

import streamlit as st
import pandas as pd

# Cargar el archivo XLSX
@st.cache
def cargar_datos():
    df = pd.read_excel("datos_distancia.xlsx")
    return df

df = cargar_datos()

# Crear una lista desplegable con los valores concatenados de cada columna
columnas_concatenadas = []
for columna in df.columns:
    valores_columna = df[columna].values
    valores_concatenados = " | ".join(map(str, valores_columna))
    columnas_concatenadas.append(valores_concatenados)

fila_seleccionada = st.selectbox("Selecciona una fila:", columnas_concatenadas)

# Crear una tabla para mostrar los datos seleccionados
st.write("Datos seleccionados:")
st.table(df.loc[df.apply(lambda row: any(val in fila_seleccionada for val in row.values), axis=1)])


