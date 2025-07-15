import streamlit as st
import folium
from streamlit_folium import st_folium
import json
import pandas as pd

st.set_page_config(page_title="서울 도로 혼잡도 지도", layout="wide")
st.title("🚦 서울 도로 혼잡도 시각화")

# 로컬 파일 대신 테스트용 GeoJSON 예시 (파일이 없을 때 대비)
try:
    with open("roads_seoul.geojson", "r", encoding="utf-8") as f:
        roads = json.load(f)
except FileNotFoundError:
    # 간단한 도로 GeoJSON 테스트용 예시
    roads = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "properties": {"name": "세종대로", "congestion": 85},
                "geometry": {
                    "type": "LineString",
                    "coordinates": [[126.9723, 37.5668], [126.9775, 37.5700]]
                }
            },
            {
                "type": "Feature",
                "properties": {"name": "을지로", "congestion": 55},
                "geometry": {
                    "type": "LineString",
                    "coordinates": [[126.986, 37.566], [126.990, 37.568]]
                }
            },
            {
                "type": "Feature",
                "properties": {"name": "신촌로", "congestion": 25},
                "geometry": {
                    "type": "LineString",
                    "coordinates": [[126.935, 37.559], [126.940, 37.561]]
                }
            }
        ]
    }

# 혼잡도 색상 매핑
def get_color(cong):
    if cong >= 80:
        return "red"
    elif cong >= 40:
        return "orange"
    else:
        return "green"

# 스타일 함수
def style_function(feature):
    cong = feature["properties"].get("congestion", 0)
    return {
        "color": get_color(cong),
        "weight": 3,
        "opacity": 0.8
    }

# 지도 생성
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

# 통계 요약
stats = []
for ft in roads["features"]:
    cong = ft["properties"].get("congestion", 0)
    if cong >= 80:
        stats.append(("정체", 1))
    elif cong >= 40:
        stats.append(("지체", 1))
    else:
        stats.append(("원활", 1))

df_stat = pd.DataFrame(stats, columns=["상태", "count"]).groupby("상태").sum().reset_index()
st.subheader("📊 상태별 도로 구간 수")
st.bar_chart(df_stat.set_index("상태"))
