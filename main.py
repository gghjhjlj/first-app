import streamlit as st

# 제목
st.title("MBTI 기반 직업 추천기")
st.write("당신의 MBTI를 선택하면 적합한 직업 3가지를 추천해드려요!")

# MBTI 리스트
mbti_list = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

# MBTI 선택
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요:", mbti_list)

# MBTI별 추천 직업 딕셔너리
mbti_jobs = {
    "ISTJ": ["회계사", "공무원", "데이터 분석가"],
    "ISFJ": ["간호사", "사회복지사", "초등교사"],
    "INFJ": ["심리상담사", "작가", "교수"],
    "INTJ": ["전략 컨설턴트", "연구원", "개발자"],
    "ISTP": ["엔지니어", "파일럿", "자동차 정비사"],
    "ISFP": ["디자이너", "조경사", "플로리스트"],
    "INFP": ["작가", "예술가", "상담가"],
    "INTP": ["연구원", "개발자", "철학자"],
    "ESTP": ["영업사원", "기업가", "구조대원"],
    "ESFP": ["배우", "가수", "이벤트 플래너"],
    "ENFP": ["마케터", "방송인", "기획자"],
    "ENTP": ["벤처 창업가", "기획자", "변호사"],
    "ESTJ": ["경영자", "군인", "프로젝트 매니저"],
    "ESFJ": ["간호사", "교사", "HR 매니저"],
    "ENFJ": ["멘토", "강사", "상담가"],
    "ENTJ": ["CEO", "전략기획자", "경영 컨설턴트"]
}

# 추천 결과 출력
if selected_mbti:
    st.subheader(f"{selected_mbti}에게 어울리는 직업 추천:")
    for idx, job in enumerate(mbti_jobs[selected_mbti], start=1):
        st.write(f"{idx}. {job}")
