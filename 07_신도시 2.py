import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import plotly.express as px

st.set_page_config(page_title="신도시 CO₂ 배출량", layout="wide")
st.title("🏙️ 대한민국 주요 신도시 CO₂ 배출량 시각화")

# 📌 신도시 예시 데이터
data = {
    '신도시': ['판교신도시', '동탄신도시', '위례신도시', '광교신도시', '세종시', '김포한강신도시'],
    '행정구역': ['성남시', '화성시', '성남시', '수원시', '세종시', '김포시'],
    '위도': [37.3925, 37.2083, 37.4673, 37.3020, 36.4801, 37.6151],
    '경도': [127.1310, 127.1087, 127.1246, 127.0336, 127.2890, 126.7159],
    'co2': [320, 410, 290, 350, 400, 330]  # 예시 단위: 천 톤
}
df = pd.DataFrame(data)

# 🌍 Folium 지도
m = folium.Map(location=[36.5, 127.8], zoom_start=7, tiles='cartodbpositron')

for _, row in df.iterrows():
    folium.CircleMarker(
        location=(row['위도'], row['경도']),
        radius=row['co2'] / 50,
        color='red',
        fill=True,
        fill_opacity=0.6,
        tooltip=f"{row['신도시']}<br>CO₂: {row['co2']} kt"
    ).add_to(m)

st.subheader("📌 신도시별 CO₂ 배출량 지도 (예시)")
st_folium(m, width=900, height=600)

# 📊 Plotly 막대그래프
st.subheader("📈 신도시 CO₂ 배출량 비교")
fig = px.bar(
    df.sort_values("co2", ascending=False),
    x="신도시", y="co2",
    color="신도시",
    labels={"co2": "이산화탄소 배출량 (천 톤)"},
    title="신도시별 이산화탄소 배출량"
)
st.plotly_chart(fig, use_container_width=True)
