import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# 페이지 설정
st.set_page_config(page_title="세계 이산화탄소 배출량", layout="wide")
st.title("🌍 세계 국가별 이산화탄소 배출량 시각화")

# 데이터 업로드 또는 예제 데이터 불러오기
uploaded_file = st.file_uploader("CSV 파일 업로드 (country, co2 columns 포함)", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
else:
    # 예제 데이터 (나라명과 CO2 배출량 - 실제 분석에는 정확한 데이터를 사용하세요)
    df = pd.DataFrame({
        'country': ['United States', 'China', 'India', 'Russia', 'Germany', 'South Korea'],
        'co2': [5000, 10000, 3000, 2000, 1500, 700]
    })

# 국가명 → ISO 3-letter 코드 변환
import pycountry

def get_country_code(name):
    try:
        return pycountry.countries.lookup(name).alpha_3
    except:
        return None

df["iso_code"] = df["country"].apply(get_country_code)
df = df.dropna(subset=["iso_code"])

# GeoJSON 데이터 불러오기 (세계 지도)
import json
import requests
url = "https://raw.githubusercontent.com/python-visualization/folium/master/examples/data/world-countries.json"
geo_json = requests.get(url).json()

# folium 지도 생성
m = folium.Map(location=[20, 0], zoom_start=2, tiles="cartodbpositron")

# Choropleth 레이어 추가
folium.Choropleth(
    geo_data=geo_json,
    name='choropleth',
    data=df,
    columns=['iso_code', 'co2'],
    key_on='feature.id',
    fill_color='YlOrRd',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='이산화탄소 배출량 (단위: 백만 톤)',
).add_to(m)

# 지도 표시
st.subheader("📌 국가별 CO₂ 배출 지도")
st_data = st_folium(m, width=900)
