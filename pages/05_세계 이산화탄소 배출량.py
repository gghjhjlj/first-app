import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import pycountry
import requests

st.set_page_config(page_title="세계 CO₂ 배출량", layout="wide")
st.title("🌍 세계 국가별 이산화탄소 배출량 시각화")

# 주요 국가 CO2 배출량 예시 데이터
data = {
    'country': [
        'China', 'United States', 'India', 'Russia', 'Japan',
        'Germany', 'Iran', 'South Korea', 'Canada', 'Brazil',
        'Indonesia', 'Saudi Arabia', 'Mexico', 'South Africa',
        'Australia', 'Turkey', 'United Kingdom', 'Italy', 'France', 'Thailand'
    ],
    'co2': [
        10000, 5000, 3000, 2000, 1500,
        1300, 1200, 700, 600, 500,
        500, 450, 400, 390, 380,
        370, 360, 350, 340, 330
    ]
}

df = pd.DataFrame(data)

# 국가 이름을 ISO 3-letter 코드로 변환
def get_country_code(name):
    try:
        return pycountry.countries.lookup(name).alpha_3
    except:
        return None

df["iso_code"] = df["country"].apply(get_country_code)
df = df.dropna(subset=["iso_code"])

# 세계 지도 GeoJSON
geo_url = "https://raw.githubusercontent.com/python-visualization/folium/master/examples/data/world-countries.json"
geo_json = requests.get(geo_url).json()

# Folium 지도 생성
m = folium.Map(location=[20, 0], zoom_start=2, tiles="cartodbpositron")

folium.Choropleth(
    geo_data=geo_json,
    name='choropleth',
    data=df,
    columns=['iso_code', 'co2'],
    key_on='feature.id',
    fill_color='YlOrRd',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='CO₂ 배출량 (단위: 백만 톤)',
).add_to(m)

# Streamlit에 지도 표시
st.subheader("📌 주요 국가 CO₂ 배출 지도")
st_data = st_folium(m, width=900, height=600)
