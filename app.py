
import pandas as pd
import plotly.express as px
import streamlit as st

# Configuración de la aplicación
st.set_page_config(
    page_title="Análisis de vehículos usados",
    page_icon="🚗",
    layout="wide"
)

st.title("Análisis exploratorio de vehículos usados")
st.write("Visualización interactiva de anuncios de vehículos en Estados Unidos")

# Cargar el conjunto de datos
@st.cache_data
def cargar_datos():
    return pd.read_csv("vehicles_us.csv")

car_data = cargar_datos()

# Crear casillas de verificación
build_histogram = st.checkbox("Construir un histograma")
build_scatter = st.checkbox("Construir un gráfico de dispersión")

# HISTOGRAMA
if build_histogram:

    st.write("Distribución del kilometraje de los vehículos anunciados")

    fig_hist = px.histogram(
        car_data,
        x="odometer",
        nbins=60,
        title="Distribución del kilometraje de vehículos",
        labels={"odometer": "Kilometraje (millas)"},
        marginal="box"
    )

    st.plotly_chart(fig_hist, width="stretch")


# GRÁFICO DE DISPERSIÓN
if build_scatter:

    st.write("Relación entre kilometraje y precio de los vehículos")

    fig_scatter = px.scatter(
        car_data,
        x="odometer",
        y="price",
        color="condition",
        opacity=0.5,
        title="Relación entre kilometraje y precio",
        labels={
            "odometer": "Kilometraje (millas)",
            "price": "Precio (USD)",
            "condition": "Condición del vehículo"
        }
    )

    st.plotly_chart(fig_scatter, width="stretch")
