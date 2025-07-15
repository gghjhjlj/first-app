import streamlit as st
import numpy as np
import sympy as sp
import plotly.graph_objects as go

# Streamlit 설정
st.set_page_config(page_title="📈 미분 시각화", layout="centered")
st.title("📐 함수 · 도함수 · 접선 시각화")

# 사용자 입력
func_input = st.text_input("함수를 입력하세요 (예: sin(x), x**2 + 3*x):", "x**2")
x_val = st.slider("접선을 그릴 x 위치 선택", -10, 10, value=1)

# 수학 준비
x = sp.Symbol('x')
try:
    func_expr = sp.sympify(func_input)
    deriv_expr = sp.diff(func_expr, x)

    f = sp.lambdify(x, func_expr, 'numpy')
    f_prime = sp.lambdify(x, deriv_expr, 'numpy')

    # x 값 범위
    x_vals = np.linspace(x_val - 5, x_val + 5, 400)
    y_vals = f(x_vals)
    slope = f_prime(x_val)
    tangent_y = slope * (x_vals - x_val) + f(x_val)

    # 그래프 그리기
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x_vals, y=y_vals, name="함수", line=dict(color='blue')))
    fig.add_trace(go.Scatter(x=x_vals, y=tangent_y, name="접선", line=dict(color='red', dash='dash')))
    fig.add_trace(go.Scatter(x=[x_val], y=[f(x_val)], mode='markers+text', name='접점',
                             marker=dict(size=8, color='black'),
                             text=[f"x={x_val}, f(x)={f(x_val):.2f}"],
                             textposition="top right"))

    fig.update_layout(title=f"f(x) = {func_expr}, f'(x) = {deriv_expr}, 기울기 = {slope:.2f}",
                      xaxis_title="x", yaxis_title="y",
                      height=500)

    st.plotly_chart(fig, use_container_width=True)

except Exception as e:
    st.error(f"입력 오류: {e}")
