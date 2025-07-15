import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="신도시 공급 분석", layout="wide")
st.title("🏙️ 신도시 공급호수 및 분양가 시각화")

# 예시 신도시 데이터
data = {
    "신도시": ["동탄", "세종", "위례", "김포한강", "검단", "양주", "파주운정"],
    "분양가(만원/m²)": [1200, 1150, 1300, 1100, 1050, 1000, 950],
    "공급호수(호)": [80000, 90000, 60000, 50000, 70000, 40000, 45000]
}
df = pd.DataFrame(data)

# Plotly 이중축 그래프
fig = go.Figure()

# 공급호수 - 막대
fig.add_trace(go.Bar(
    x=df["신도시"],
    y=df["공급호수(호)"],
    name="공급호수(호)",
    yaxis='y1',
    marker_color='skyblue'
))

# 분양가 - 선
fig.add_trace(go.Scatter(
    x=df["신도시"],
    y=df["분양가(만원/m²)"],
    name="분양가(만원/m²)",
    yaxis='y2',
    mode='lines+markers',
    line=dict(color='red', width=3)
))

# 레이아웃
fig.update_layout(
    title="신도시별 공급호수 및 평균 분양가",
    xaxis=dict(title="신도시"),
    yaxis=dict(title="공급호수(호)", side='left'),
    yaxis2=dict(
        title="분양가(만원/m²)",
        overlaying='y',
        side='right'
    ),
    legend=dict(x=0.01, y=0.99),
    template="plotly_white"
)

st.plotly_chart(fig, use_container_width=True)
