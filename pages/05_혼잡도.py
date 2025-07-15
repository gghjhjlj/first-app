
st.set_page_config(page_title="TomTom Traffic Index 분석", layout="wide")
st.title("🚗 TomTom Traffic Index - 국가/도시별 혼잡도 분석")
st.write("Kaggle에서 제공하는 TomTom 교통 혼잡도 데이터를 가져와 시각화합니다.")

@st.cache_data
def load_data():
    df = dataset_load(
        KaggleDatasetAdapter.PANDAS,
        "bwandowando/tomtom-traffic-data-55-countries-387-cities",
        "tomtom_traffic_index.csv"
    )
    return df

df = load_data()
st.write("데이터 프레임 샘플:")
st.dataframe(df.head())

# 주요 컬럼 정리
expected_cols = ["country", "city", "year", "month", "day", "weekday", "hour", "congestion_index"]
df = df[expected_cols]
df.columns = ["국가","도시","연도","월","일","요일","시간","혼잡도"]

st.subheader("📊 연도/국가/도시 기준 통계")
country = st.selectbox("국가 선택", df["국가"].unique())
city = st.selectbox("도시 선택", df[df["국가"] == country]["도시"].unique())

sub = df[(df["국가"] == country) & (df["도시"] == city)]
st.write(f"### {country} - {city} 교통 혼잡도 추이")
fig = px.line(sub, x="시간", y="혼잡도", color="요일", markers=True,
              labels={"혼잡도":"혼잡도(%)","시간":"시간대"})
st.plotly_chart(fig, use_container_width=True)

st.subheader("🚦 혼잡도 Top 10 도시 (평균 기준)")
agg = df.groupby(["국가","도시"])["혼잡도"].mean().reset_index()
top10 = agg.sort_values("혼잡도", ascending=False).head(10)
fig2 = px.bar(top10, x="도시", y="혼잡도", color="국가")
st.plotly_chart(fig2, use_container_width=True)

st.subheader("📈 연도별 평균 혼잡도 변화 (국가/도시 전체)")
trend = df.groupby("연도")["혼잡도"].mean().reset_index()
fig3 = px.line(trend, x="연도", y="혼잡도", markers=True)
st.plotly_chart(fig3, use_container_width=True)
