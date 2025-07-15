import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="TomTom Traffic Index 분석", layout="wide")
st.title("🚗 TomTom Traffic Index - 국가/도시별 혼잡도 분석")

# 1. CSV 업로드
uploaded_file = st.file_uploader("CSV 파일 업로드", type=["csv"])

if uploaded_file is not None:
    # 2. 파일 로딩
    try:
        df = pd.read_csv(uploaded_file)
        st.success("✅ CSV 파일 업로드 성공!")
        
        # 3. 필수 컬럼 존재 확인
        expected_cols = ["country", "city", "year", "month", "day", "weekday", "hour", "congestion_index"]
        if not all(col in df.columns for col in expected_cols):
            st.error("❌ 필수 컬럼이 누락되어 있습니다.")
            st.stop()

        # 4. 컬럼 이름 변경
        df = df[expected_cols]
        df.columns = ["국가", "도시", "연도", "월", "일", "요일", "시간", "혼잡도"]

        st.subheader("📊 데이터 미리보기")
        st.dataframe(df.head())

        # 5. 국가/도시 선택
        country = st.selectbox("국가 선택", df["국가"].unique())
        city = st.selectbox("도시 선택", df[df["국가"] == country]["도시"].unique())

        # 6. 혼잡도 시간 추이
        sub = df[(df["국가"] == country) & (df["도시"] == city)]
        fig = px.line(sub, x="시간", y="혼잡도", color="요일", markers=True)
        st.plotly_chart(fig, use_container_width=True)

        # 7. 혼잡도 Top 10 도시
        top10 = df.groupby(["국가", "도시"])["혼잡도"].mean().reset_index().sort_values("혼잡도", ascending=False).head(10)
        fig2 = px.bar(top10, x="도시", y="혼잡도", color="국가")
        st.subheader("🚦 혼잡도 Top 10 도시")
        st.plotly_chart(fig2, use_container_width=True)

        # 8. 연도별 평균 혼잡도
        trend = df.groupby("연도")["혼잡도"].mean().reset_index()
        fig3 = px.line(trend, x="연도", y="혼잡도", markers=True)
        st.subheader("📈 연도별 평균 혼잡도 변화")
        st.plotly_chart(fig3, use_container_width=True)

    except Exception as e:
        st.error(f"❌ 파일을 처리하는 중 오류 발생: {e}")
else:
    st.info("📂 CSV 파일을 업로드해주세요.")
