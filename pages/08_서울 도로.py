import streamlit as st
import folium
from streamlit_folium import st_folium
import json

st.set_page_config(page_title="서울 도로 혼잡도 지도", layout="wide")
st.title("🚦 서울 도로 혼잡도 시각화")

# GeoJSON 파일 로드 (pages 폴더와 같은 위치에 있어야 합니다)
with open("roads_seoul.geojson", "r", encoding="utf-8") as f:
    roads = json.load(f)

# 혼잡도 기준 정의
def get_color(cong):
    if cong >= 80:
        return "red"    # Jam
    elif cong >= 40:
        return "orange" # Slow
    else:
        return "green"  # Free

# 스타일 함수
def style_function(feature):
    cong = feature["properties"].get("congestion", feature["properties"].get("speed", 0))
    return {
        "color": get_color(cong),
        "weight": 3,
        "opacity": 0.8
    }

# Folium 지도 생성
m = folium.Map(location=[37.5665, 126.9780], zoom_start=11, tiles="cartodbpositron")

folium.GeoJson(
    roads,
    style_function=style_function,
    tooltip=folium.GeoJsonTooltip(
        fields=["name", "congestion"],
        aliases=["도로명", "혼잡도(%)"],
        localize=True
    )
).add_to(m)

st.subheader("📍 서울 도로 혼잡도 지도 (빨강=정체, 주황=지체, 초록=원활)")
st_folium(m, width=800, height=600)

# 요약 통계: 혼잡도 분포
import pandas as pd
stats = []
for ft in roads["features"]:
    cong = ft["properties"].get("congestion", ft["properties"].get("speed", 0))
    if cong >= 80:
        stats.append(("정체", 1))
    elif cong >= 40:
        stats.append(("지체", 1))
    else:
        stats.append(("원활", 1))
df_stat = pd.DataFrame(stats, columns=["상태","count"]).groupby("상태").sum().reset_index()
st.subheader("📊 상태별 도로 구간 수")
st.bar_chart(df_stat.set_index("상태"))
