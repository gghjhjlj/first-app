import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="도시 혼잡도 시각화", layout="wide")
st.title("🚦 TomTom 도시 혼잡도 분석")

# GitHub의 원시 CSV 경로 (본인의 깃헙 URL로 교체)
CSV_URL = "https://raw.githubusercontent.com/your-username/your-repo/main/congestion_by_city.csv"

@st.cache_data
def load_data():
    return pd.read_csv(CSV_URL)

# 데이터 로드
try:
    df = load_data()
    st.success("✅ 데이터 로드 성공!")

    st.subheader("데이터 미리보기")
    st.dataframe(df.head(), use_container_width=True)

    # 도시 선택 및 시각화
    if "City" in df.columns and "Year" in df.columns:
        selected_city = st.selectbox("도시 선택", df["City"].unique())
        city_data = df[df["City"] == selected_city]

        st.subheader(f"📈 {selected_city} 혼잡도 추이")
        if "Congestion Level (%)" in df.columns:
            fig = px.line(
                city_data,
                x="Year",
                y="Congestion Level (%)",
                title=f"{selected_city} 혼잡도 변화",
                markers=True
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.error("❌ 'Congestion Level (%)' 열이 없습니다.")
    else:
        st.error("❌ 'City' 또는 'Year' 열이 누락되었습니다.")

except Exception as e:
    st.error(f"🚨 데이터 불러오기 실패: {e}")
