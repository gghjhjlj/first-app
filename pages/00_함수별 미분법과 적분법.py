import streamlit as st

# 제목
st.title("함수 유형별 미분법 & 적분법 안내기")
st.write("함수의 종류를 선택하면 적절한 미분법과 적분법을 알려드려요!")

# 함수 유형 목록
function_types = {
    "다항함수": {
        "미분법": "항별로 미분 (거듭제곱의 미분: d/dx [xⁿ] = n·xⁿ⁻¹)",
        "적분법": "항별로 적분 (거듭제곱의 적분: ∫xⁿ dx = xⁿ⁺¹ / (n+1) + C)"
    },
    "지수함수": {
        "미분법": "지수함수의 미분 (d/dx [eˣ] = eˣ, d/dx [aˣ] = aˣ·ln(a))",
        "적분법": "지수함수의 적분 (∫eˣ dx = eˣ + C, ∫aˣ dx = aˣ / ln(a) + C)"
    },
    "로그함수": {
        "미분법": "로그함수의 미분 (d/dx [ln(x)] = 1/x)",
        "적분법": "로그함수의 적분 (∫1/x dx = ln|x| + C)"
    },
    "삼각함수": {
        "미분법": "삼각함수의 미분 (예: d/dx [sin(x)] = cos(x), d/dx [cos(x)] = -sin(x))",
        "적분법": "삼각함수의 적분 (예: ∫sin(x) dx = -cos(x) + C, ∫cos(x) dx = sin(x) + C)"
    },
    "역삼각함수": {
        "미분법": "역삼각함수의 미분 (예: d/dx [arcsin(x)] = 1/√(1−x²))",
        "적분법": "역삼각함수의 적분 (예: ∫1/√(1−x²) dx = arcsin(x) + C)"
    },
    "하이퍼볼릭 함수": {
        "미분법": "쌍곡함수의 미분 (예: d/dx [sinh(x)] = cosh(x))",
        "적분법": "쌍곡함수의 적분 (예: ∫cosh(x) dx = sinh(x) + C)"
    }
}

# 선택 UI
selected_type = st.selectbox("함수의 유형을 선택하세요:", list(function_types.keys()))

# 결과 출력
if selected_type:
    st.subheader(f"✅ {selected_type}에 적합한 미분법과 적분법")
    st.markdown(f"**📘 미분법:** {function_types[selected_type]['미분법']}")
    st.markdown(f"**📗 적분법:** {function_types[selected_type]['적분법']}")
