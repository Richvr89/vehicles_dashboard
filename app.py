import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8501))
    import streamlit.web.bootstrap
    streamlit.web.bootstrap.run("app.py", f"--server.port={port}", [])



import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar los datos
@st.cache_data
def load_data():
    return pd.read_csv('vehicles_us.csv')

car_data = load_data()

# Encabezado
st.title("Dashboard de Anuncios de Coches")
st.markdown("Explora los datos de anuncios de coches en Estados Unidos.")

# Selección de análisis
st.sidebar.header("Opciones de análisis")
option = st.sidebar.radio(
    "Selecciona una opción:",
    ('Distribución del Odómetro', 'Relación Odómetro vs Precio')
)

# Mostrar gráfico según selección
if option == 'Distribución del Odómetro':
    st.subheader("Distribución del Odómetro")
    fig = px.histogram(car_data, x="odometer", title="Distribución del Odómetro")
    st.plotly_chart(fig, use_container_width=True)

elif option == 'Relación Odómetro vs Precio':
    st.subheader("Relación entre Odómetro y Precio")
    fig = px.scatter(car_data, x="odometer", y="price", title="Relación entre Odómetro y Precio")
    st.plotly_chart(fig, use_container_width=True)