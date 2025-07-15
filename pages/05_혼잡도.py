import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="TomTom Traffic Index 분석", layout="wide")
st.title("🚗 TomTom Traffic Index - 국가/도시별 혼잡도 분석")
st.write("TomTom 교통 혼잡도 데이터를 업로드하면 시각화됩니다.")

# ✅ 파일 업로드
uploaded_file = st.file_uploader("CSV 파일 업로드", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # ✅ 컬럼 존재 여부 확인 후 필터링
    expected_cols = ["country", "city", "year", "month", "day", "weekday", "hour", "congestion_index"]
    if all(col in df.columns for col in expected_cols):
        df = df[expected_cols]
        df.columns = ["국가","도시","연도","월","일","요일","시간","혼잡도"]

        st.write("데이터 샘플:")
        st.dataframe(df.head())

        # 📊 연도/국가/도시 선택
        country = st.selectbox("국가 선택", sorted(df["국가"].unique()))
        city = st.selectbox("도시 선택", sorted(df[df["국가"] == country]["도시"].unique()))

        sub = df[(df["국가"] == country) & (df["도시"] == city)]

        st.write(f"### {country} - {city} 교통 혼잡도 추이")
        fig = px.line(sub, x="시간", y="혼잡도", color="요일", markers=True,
                      labels={"혼잡도":"혼잡도(%)","시간":"시간대"})
        st.plotly_chart(fig, use_container_width=True)

        # 🚦 혼잡도 Top 10 도시
        st.subheader("🚦 혼잡도 Top 10 도시 (평균 기준)")
        agg = df.groupby(["국가","도시"])["혼잡도"].mean().reset_index()
        top10 = agg.sort_values("혼잡도", ascending=False).head(10)
        fig2 = px.bar(top10, x="도시", y="혼잡도", color="국가")
        st.plotly_chart(fig2, use_container_width=True)

        # 📈 연도별 평균 혼잡도 변화
        st.subheader("📈 연도별 평균 혼잡도 변화")
        trend = df.groupby("연도")["혼잡도"].mean().reset_index()
        fig3 = px.line(trend, x="연도", y="혼잡도", markers=True)
        st.plotly_chart(fig3, use_container_width=True)

    else:
        st.error("필요한 컬럼이 데이터에 없습니다. 다음 컬럼이 필요
