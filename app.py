import streamlit as st
import folium
from streamlit_folium import st_folium
from folium.plugins import LocateControl

# Configuração do Streamlit
st.set_page_config(page_title="Mapa Interativo", layout="wide")

st.title("📍 Mapa Interativo com Localização Automática")

# Criando um mapa inicial (ponto arbitrário)
m = folium.Map(location=[0, 0], zoom_start=5, tiles="cartodbpositron")

# Adicionando o controle de localização
LocateControl(auto_start=True, keepCurrentZoomLevel=True, drawMarker=True).add_to(m)

# Renderizando o mapa no Streamlit
st_folium(m, width=800, height=500)
