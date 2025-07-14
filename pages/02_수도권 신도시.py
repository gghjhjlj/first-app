ㅁimport streamlit as st

st.set_page_config(page_title="수도권 신도시 종합 분석", layout="wide")
st.title("🏘️ 수도권 신도시 종합 분석 웹앱")
st.write("기수, 공급 호수, 개발 규모, 교통망, 개발연도를 기준으로 신도시를 비교할 수 있습니다.")

# 신도시 데이터 (기수 포함 + 상세 정보)
new_towns = {
    "1기": {
        "일산신도시": {
            "공급 호수": 100000,
            "개발 규모": 90.0,  # km²
            "교통망": ["지하철 3호선", "경의선", "외곽순환도로"],
            "개발 연도": "1996–2000"
        },
        "분당신도시": {
            "공급 호수": 110000,
            "개발 규모": 78.0,
            "교통망": ["지하철 분당선", "경부고속도로"],
            "개발 연도": "1989–1996"
        }
    },
    "2기": {
        "판교신도시": {
            "공급 호수": 29000,
            "개발 규모": 8.9,
            "교통망": ["신분당선", "경강선"],
            "개발 연도": "2003–2010"
        },
        "위례신도시": {
            "공급 호수": 42000,
            "개발 규모": 6.8,
            "교통망": ["지하철 8호선", "위례신사선(예정)"],
            "개발 연도": "2008–2020대"
        },
        "동탄2신도시": {
            "공급 호수": 119000,
            "개발 규모": 24.3,
            "교통망": ["SRT", "GTX‑A(예정)"],
            "개발 연도": "2008–2027(예정)"
        }
    },
    "3기": {
        "김포한강신도시": {
            "공급 호수": 50000,
            "개발 규모": 11.8,
            "교통망": ["김포골드라인", "제2순환고속도로"],
            "개발 연도": "2006–2015"
        },
        "검단신도시": {
            "공급 호수": 75000,
            "개발 규모": 11.2,
            "교통망": ["인천1호선 연장", "GTX‑D(예정)"],
            "개발 연도": "2007–2030(예정)"
        }
    }
}

# 기수 선택
generation = st.sidebar.selectbox("신도시 기수 선택", list(new_towns.keys()))
towns = new_towns[generation]

# 테이블 데이터 준비
rows = []
for name, info in towns.items():
    rows.append({
        "신도시": name,
        "공급 호수(호)": info["공급 호수"],
        "개발 규모(km²)": info["개발 규모"],
        "교통망": ", ".join(info["교통망"]),
        "개발 연도": info["개발 연도"]
    })

# 데이터프레임화 및 인구밀도 계산 없음
import pandas as pd
df = pd.DataFrame(rows)

st.subheader(f"{generation} 신도시 비교표")
st.dataframe(df, use_container_width=True)

# 공급 호수 기준 정렬
st.write("### 📊 공급 호수 기준 내림차순 정렬")
st.dataframe(df.sort_values("공급 호수(호)", ascending=False), use_container_width=True)

# 상세 신도시 선택
selected = st.selectbox("🔍 상세 정보를 보고 싶은 신도시를 선택하세요:", [""] + list(towns.keys()))
if selected:
    info = towns[selected]
    st.subheader(f"{selected} 상세 정보")
    st.write(f"**공급 호수:** {info['공급 호수']:,} 호")
    st.write(f"**개발 규모:** {info['개발 규모']} km²")
    st.write(f"**교통망:** {', '.join(info['교통망'])}")
    st.write(f"**개발 연도:** {info['개발 연도']}")

# 개발 규모 vs 공급 호수 차트
st.subheader("📈 개발 규모 vs 공급 호수 비교")
st.bar_chart(df.set_index("신도시")[["공급 호수(호)", "개발 규모(km²)"]])
