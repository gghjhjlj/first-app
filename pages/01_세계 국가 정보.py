import streamlit as st
import pandas as pd
import json

st.set_page_config(page_title="🌍 전 세계 국가 비교", layout="wide")
st.title("전 세계 국가 비교 웹앱")
st.write("인구, 면적, 인구밀도, 환율, 범죄율, 관광명소 등을 비교할 수 있습니다.")

@st.cache_data
def load():
    df_c = pd.read_csv("countries.csv")
    df_cr = pd.read_csv("crime.csv")
    df_ex = pd.read_csv("currency.csv")
    with open("attractions.json", encoding="utf-8") as f:
        attractions = json.load(f)
    return df_c, df_cr, df_ex, attractions

df_c, df_cr, df_ex, attractions = load()

# 인구밀도 계산
df_c["density"] = (df_c["population"] / df_c["area_km2"]).round(2)

# 통합 테이블 생성
df = df_c.merge(df_cr, on="country", how="left") \
         .merge(df_ex, on="country", how="left")

st.subheader("국가별 인구·면적·밀도 비교표")
st.dataframe(df[["country","capital","population","area_km2","density"]], use_container_width=True)

# 상세 선택
st.subheader("🔍 국가 상세 정보")
country = st.selectbox("국가 선택", df["country"].sort_values())
info = df[df["country"]==country].iloc[0]

st.markdown(f"### {country}")
st.write(f"**수도:** {info['capital']}")
st.write(f"**인구:** {info['population']:,}명")
st.write(f"**면적:** {info['area_km2']:,} ㎢")
st.write(f"**인구밀도:** {info['density']:,} 명/㎢")
st.write(f"**환율 (1 USD):** {info.get('exchange_rate_usd','-')}")
st.write(f"**범죄 지수:** {info.get('crime_index','-')}")

st.write("**주요 관광명소:**")
for place in attractions.get(country, []):
    st.markdown(f"- {place}")
