import streamlit as st
import pandas as pd
import folium
from streamlit.components.v1 import html

# Streamlit 기본 설정
st.set_page_config(layout="wide")
st.title("🗺️ 서울 25개 자치구 인구 시각화")

# 데이터 불러오기
@st.cache_data
def load_data():
    df = pd.read_csv("population.csv")
    geo = open("seoul_geo.json", encoding="utf-8").read()
    return df, geo

data, geo_json = load_data()

# 지도 중심 좌표 (서울)
m = folium.Map(location=[37.5665, 126.9780], zoom_start=11)

# Choropleth 추가
folium.Choropleth(
    geo_data=geo_json,
    name="choropleth",
    data=data,
    columns=["자치구", "인구수"],
    key_on="feature.properties.name",
    fill_color="YlOrRd",
    fill_opacity=0.7,
    line_opacity=0.3,
    legend_name="서울 자치구별 인구 수",
).add_to(m)

# 자치구 마커 표시 (선택사항)
for idx, row in data.iterrows():
    folium.Marker(
        location=[],  # 생략 가능
        tooltip=f"{row['자치구']}: {row['인구수']:,}명"
    )

# HTML 삽입
html(m._repr_html_(), height=600)
