import streamlit as st
import pandas as pd

# Carga el archivo xlsx
file_path = 'datos_distancia.xlsx'  # Reemplaza con la ruta de tu archivo xlsx
data = pd.read_excel(file_path)

# Elimina la primera columna (índice 0)
data.drop(data.columns[0], axis=1, inplace=True)

# Elimina las columnas no deseadas
data.drop(columns=['distancia_metros', 'distancia_minutos'], inplace=True)

# Crea una lista de diccionarios, cada uno con los datos de una fila
dropdown_options = data.to_dict('records')
st.write('Data: ', dropdown_options[0["client_id"])

# Organiza los elementos en dos columnas
left_column, right_column = st.columns([1, 1.5], gap = "large")  # Cambio en la especificación de ancho

# En la columna izquierda, muestra el menú desplegable
with left_column:
    selected_rows = st.multiselect('Selecciona comunidades a insertar:', dropdown_options)

# En la columna derecha, muestra la tabla con las filas seleccionadas
with right_column:
    if selected_rows:
        st.write('Comunidades seleccionadas:')
        st.dataframe(pd.DataFrame(selected_rows), width=None)

        # Suma los datos de la columna "tiempo"
        total_tiempo = sum(row['tiempo'] for row in selected_rows)
        st.write(f'Tiempo total: **{total_tiempo}**')
