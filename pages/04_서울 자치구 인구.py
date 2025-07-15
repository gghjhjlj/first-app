import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import requests

st.set_page_config(page_title="서울 자치구 인구", layout="wide")
st.title("🗺️ 서울 25개 자치구 인구 시각화")

# 자치구 인구 (2023년 기준 샘플)
data = {
    "자치구": [
        "강남구", "강동구", "강북구", "강서구", "관악구", "광진구", "구로구", "금천구", "노원구",
        "도봉구", "동대문구", "동작구", "마포구", "서대문구", "서초구", "성동구", "성북구", "송파구",
        "양천구", "영등포구", "용산구", "은평구", "종로구", "중구", "중랑구"
    ],
    "인구": [
        537824, 428547, 310364, 578458, 492375, 351586, 405453, 248928, 497973,
        316128, 341582, 390934, 373629, 309425, 423120, 301642, 442786, 643254,
        464379, 372721, 238029, 482406, 144654, 120998, 378804
    ]
}
df = pd.DataFrame(data)

# ✅ GeoJSON 데이터 자동 가져오기
geo_url = (
    "https://raw.githubusercontent.com/southkorea/southkorea-maps/master/"
    "kostat/2013/json/skorea_municipalities_geo_simple.json"
)
seoul_geo = requests.get(geo_url).json()

# Folium 지도 준비
m = folium.Map(location=[37.5665, 126.9780], zoom_start=11, tiles="cartodbpositron")
folium.Choropleth(
    geo_data=seoul_geo,
    data=df,
    columns=["자치구", "인구"],
    key_on="feature.properties.name",
    fill_color="YlOrRd",
    fill_opacity=0.7,
    line_opacity=0.3,
    legend_name="서울 자치구별 인구 수"
).add_to(m)

st.subheader("📍 서울 자치구 인구 지도")
st_data = st_folium(m, width=800, height=600)

# 인구 표도 함께 제공
st.subheader("📋 자치구별 인구 DataFrame")
st.dataframe(df, use_container_width=True)
