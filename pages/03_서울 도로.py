import streamlit as st
import pandas as pd
import folium
from streamlit.components.v1 import html

st.set_page_config(layout="wide")
st.title("🚦 서울 혼잡 도로 지도 (Folium)")

# 서울 혼잡 도로 예시
roads = pd.DataFrame({
    "도로명": ["강남대로", "올림픽대로", "서부간선도로"],
    "위도": [37.4981, 37.5202, 37.4833],
    "경도": [127.0276, 127.1033, 126.8829],
})

# folium 지도 생성
m = folium.Map(location=[37.5, 127.0], zoom_start=11)

# 마커 추가
for _, row in roads.iterrows():
    folium.Marker(
        location=[row["위도"], row["경도"]],
        popup=row["도로명"],
        tooltip=row["도로명"],
        icon=folium.Icon(color="red")
    ).add_to(m)

# 지도 출력
html(m._repr_html_(), height=600)
