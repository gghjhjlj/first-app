import streamlit as st

st.set_page_config(page_title="세계 국가 정보 비교", layout="wide")
st.title("🌍 전 세계 국가 비교 웹앱")
st.write("200개국의 수도, 인구, 면적, 인구밀도, 환율, 범죄율, 관광명소 정보를 확인해보세요.")

# 200개국 샘플 데이터 생성 (실제 데이터 아님, 예제용)
country_capital_pairs = [
    ("대한민국", "서울"), ("일본", "도쿄"), ("미국", "워싱턴 D.C."), ("프랑스", "파리"),
    ("영국", "런던"), ("독일", "베를린"), ("중국", "베이징"), ("인도", "뉴델리"),
    ("호주", "캔버라"), ("브라질", "브라질리아"), ("캐나다", "오타와"), ("이탈리아", "로마"),
    ("스페인", "마드리드"), ("멕시코", "멕시코시티"), ("남아프리카공화국", "프리토리아")
]

countries = []
for i in range(200):
    name, capital = country_capital_pairs[i % len(country_capital_pairs)]
    country = {
        "국가": f"{name}_{i+1}",
        "수도": capital,
        "인구(명)": 1000000 + i * 100000,
        "면적(㎢)": 50000 + i * 1000,
        "환율": f"약 {100 + i % 100} CUR",
        "범죄율": ["낮음", "중간", "높음"][i % 3],
        "명소": [f"{name} 명소 {j+1}" for j in range(3)]
    }
    country["인구밀도(명/㎢)"] = round(country["인구(명)"] / country["면적(㎢)"], 2)
    countries.append(country)

# 📊 표로 요약 정보 제공
st.subheader("📈 국가별 인구, 면적, 인구밀도 비교")
st.dataframe(
    {
        "국가": [c["국가"] for c in countries],
        "수도": [c["수도"] for c in countries],
        "인구(명)": [c["인구(명)"] for c in countries],
        "면적(㎢)": [c["면적(㎢)"] for c in countries],
        "인구밀도(명/㎢)": [c["인구밀도(명/㎢)"] for c in countries],
    },
    use_container_width=True
)

# 🔍 선택한 국가 정보 상세 보기
st.subheader("🔎 국가 상세 정보")
selected = st.selectbox("국가를 선택하세요:", [c["국가"] for c in countries])

for c in countries:
    if c["국가"] == selected:
        st.markdown(f"### {c['국가']} 🇺🇳")
        st.write(f"**수도:** {c['수도']}")
        st.write(f"**환율:** {c['환율']}")
        st.write(f"**범죄율:** {c['범죄율']}")
        st.write("**주요 관광명소:**")
        for place in c["명소"]:
            st.markdown(f"- {place}")
        break
