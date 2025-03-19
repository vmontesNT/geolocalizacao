import streamlit as st
import folium
from streamlit_folium import st_folium
from folium.plugins import LocateControl
from geopy.distance import geodesic

# Função para calcular os limites com base na localização e raio (100 km)
def calculate_bounds(lat, lon, radius_km):
    # Definindo o raio (em metros)
    radius = radius_km * 1000  # Convertendo para metros
    # Calculando os limites de lat e lon, criando uma caixa quadrada
    north = lat + (radius / 111320)  # Aproximadamente 1° de latitude = 111,320 metros
    south = lat - (radius / 111320)
    east = lon + (radius / (40008000 / 360))  # Aproximadamente 1° de longitude = 40,008 km
    west = lon - (radius / (40008000 / 360))
    
    return [[south, west], [north, east]]

# Configuração do Streamlit
st.set_page_config(page_title="Mapa Interativo", layout="wide")

st.title("📍 Mapa Interativo com Localização Automática e Limitação de Movimento")

# Criando o mapa inicial (ponto arbitrário)
m = folium.Map(location=[0, 0], zoom_start=15, tiles="cartodbpositron")

# Adicionando o controle de localização
LocateControl(auto_start=True, keepCurrentZoomLevel=True, drawMarker=True).add_to(m)

# Adicionando o evento para capturar a localização do usuário
# Use a função `onLocationFound` para capturar a localização e definir os limites
m.on_location_found = lambda e: set_max_bounds(e.latlng)

# Função para definir os limites do mapa com base na localização
def set_max_bounds(location):
    lat = location["lat"]
    lon = location["lng"]
    
    # Calculando os limites do mapa com 100 km de raio
    bounds = calculate_bounds(lat, lon, 100)
    
    # Definindo os limites máximos do mapa
    m.fit_bounds(bounds)
    
    # Definindo o maxBounds para impedir o movimento além do limite
    m.options['maxBounds'] = bounds
    m.options['maxBoundsViscosity'] = 1.0

# Renderizando o mapa no Streamlit
st_folium(m, width=800, height=500)
