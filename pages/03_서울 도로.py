import streamlit as st
import folium
from streamlit.components.v1 import components

st.set_page_config(page_title="서울에서 가장 붐비는 도로", layout="wide")
st.title("🚦 서울에서 가장 혼잡한 도로 시각화 (Folium)")

# 가장 혼잡한 서울 도로 예시 (강남대로 구간)
road_name = "강남대로"
location = [37.498095, 127.027610]  # 강남역 인근

# 지도 생성
m = folium.Map(location=location, zoom_start=15)
folium.Marker(
    location,
    popup=f"{road_name} (혼잡도 상위)",
    tooltip="강남대로",
    icon=folium.Icon(color="red")
).add_to(m)

# HTML로 렌더링
folium_html = m._repr_html_()
components.html(folium_html, height=500)
