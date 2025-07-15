import streamlit as st
import pandas as pd

st.set_page_config(page_title="OECD 국가 CO₂ 배출 비교", layout="wide")

st.title("🌍 OECD 국가 이산화탄소(CO₂) 배출 비교")
st.write("주요 OECD 국가들의 연간 CO₂ 배출 총량과 1인당 배출량을 비교합니다.")

# 예시 데이터 (실제 수치는 공개된 자료 기준 대략적임)
data = [
    {"국가": "미국", "총배출량(Mt)": 5000, "1인당 배출량(t)": 15.2},
    {"국가": "일본", "총배출량(Mt)": 1100, "1인당 배출량(t)": 8.7},
    {"국가": "독일", "총배출량(Mt)": 750, "1인당 배출량(t)": 9.1},
    {"국가": "한국", "총배출량(Mt)": 650, "1인당 배출량(t)": 12.4},
    {"국가": "프랑스", "총배출량(Mt)": 320, "1인당 배출량(t)": 4.9},
    {"국가": "영국", "총배출량(Mt)": 400, "1인당 배출량(t)": 5.8},
    {"국가": "캐나다", "총배출량(Mt)": 550, "1인당 배출량(t)": 14.6},
    {"국가": "호주", "총배출량(Mt)": 400, "1인당 배출량(t)": 16.9},
    {"국가": "이탈리아", "총배출량(Mt)": 350, "1인당 배출량(t)": 5.7},
    {"국가": "스페인", "총배출량(Mt)": 280, "1인당 배출량(t)": 5.9}
]

df = pd.DataFrame(data)

# 표 표시
st.subheader("📊 OECD 주요국 CO₂ 배출 데이터")
st.dataframe(df, use_container_width=True)

# 국가 선택
st.subheader("🔍 국가별 상세 정보")
selected = st.selectbox("국가를 선택하세요:", df["국가"])

country = df[df["국가"] == selected].iloc[0]
st.markdown(f"### 🌎 {country['국가']}")
st.write(f"**총 CO₂ 배출량**: {country['총배출량(Mt)']:,} Mt")
st.write(f"**1인당 CO₂ 배출량**: {country['1인당 배출량(t)']} t") 
