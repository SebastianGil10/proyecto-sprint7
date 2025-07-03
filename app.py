import pandas as pd
import plotly.express as px
import streamlit as st

import os


# Encabezado
st.header('Análisis de anuncios de vehículos en EE.UU...')

# Cargar datos
car_data = pd.read_csv('vehicles_us.csv')

# Botón para histograma
hist_button = st.button('Construir histograma')
if hist_button:
    st.write('Histograma del odómetro (kilometraje)')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

# Botón para gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')
if scatter_button:
    st.write('Gráfico de dispersión: precio vs año del modelo')
    fig2 = px.scatter(car_data, x='model_year', y='price', color='condition')
    st.plotly_chart(fig2, use_container_width=True)
# Botón de sugerencias
suggestion_button = st.button("Dame sugerencias")

if suggestion_button:
    st.subheader("🔍 Sugerencias de análisis")

    # Puedes personalizar estas sugerencias con base en el DataFrame
    st.write("- Considera analizar la relación entre el odómetro y el precio.")
    st.write("- Podrías comparar precios por tipo de combustible o transmisión.")
    st.write("- Observa cómo cambia el precio con el año del modelo.")
    st.write("- Filtra los autos en excelente estado y analiza sus precios.")

# Botón para mostrar el DataFrame completo
table_button = st.button("📊 Mostrar todos los datos")
if table_button:
    st.write("Vista completa del conjunto de datos:")
    st.dataframe(car_data)

# Botón para mostrar el Top 10 autos más caros
top10_button = st.button("💰 Ver Top 10 autos más caros")
if top10_button:
    st.write("Top 10 autos con el precio más alto:")
    top_10 = car_data.sort_values(by='price', ascending=False).head(10)
    st.dataframe(top_10)

