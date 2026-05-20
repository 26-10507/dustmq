import streamlit as st
import pandas as pd

# 1. 페이지 설정
st.set_page_config(page_title="2026 시네마 처방", page_icon="🍿")

st.title("🎬 2026 최신 영화 맞춤 처방전")
st.write("지금 당신의 상태를 분석하여, 가장 트렌디한 영화를 추천해 드립니다.")

st.divider()

# 2. 사용자 감정 데이터 입력
st.sidebar.header("📊 분석 데이터 입력")
user_name = st.sidebar.text_input("이름", "홍길동")
energy = st.sidebar.slider("현재 활력 지수", 0, 100, 50)

mood = st.selectbox(
    "💡 지금 어떤 기분이신가요?",
    [
        "압도적인 몰입감이 필요해요", 
        "복잡한 세상, 귀여운 게 최고예요", 
        "가슴 벅찬 감동을 느끼고 싶어요", 
        "긴장감 넘치는 스릴을 원해요"
    ]
)

# 3. 최신 영화 데이터베이스 (2024-2026 트렌드 반영)
movie_db = {
    "압도적인 몰입감이 필요해요": {
        "제목": "듄: 파트 2 (Dune: Part Two)",
        "특징": "웅장한 영상미와 세계관",
        "처방": "현실을 잊게 만드는 거대한 스케일의 영상이 당신의 스트레스를 압도할 거예요.",
        "지표": {"시각효과": 100, "스토리": 85, "여운": 90}
    },
    "복잡한 세상, 귀여운 게 최고예요": {
        "제목": "인사이드 아웃 2 (Inside Out 2)",
        "특징": "나의 사춘기 불안이와 친구들",
        "처방": "새로운 감정들을 마주하며 스스로를 다독이는 소중한 시간을 선물합니다.",
        "지표": {"따뜻함": 98, "공감도": 95, "재미": 88}
    },
    "가슴 벅찬 감동을 느끼고 싶어요": {
        "제목": "파묘 (Exhuma)",
        "특징": "한국적 오컬트와 서사",
        "처방": "강렬한 서사와 긴장감 끝에 오는 깊은 몰입감을 경험해 보세요.",
        "지표": {"몰입도": 95, "신선함": 90, "긴장감": 92}
    },
    "긴장감 넘치는 스릴을 원해요": {
        "제목": "범죄도시 4 (The Roundup: Punishment)",
        "특징": "시원한 액션과 권선징악",
        "처방": "답답한 가슴을 뻥 뚫어주는 마석도의 액션 데이터가 당신의 활력을 높여줍니다.",
        "지표": {"액션": 98, "유머": 85, "통쾌함": 100}
    }
}

# 4. 결과 도출 및 시각화
if st.button("✨ 데이터 분석 및 영화 처방"):
    selected = movie_db[mood]
    
    st.balloons()
    st.subheader(f"📍 {user_name}님을 위한 처방: [{selected['제목']}]")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.write(f"**🌟 핵심 포인트:** {selected['특징']}")
        st.write(f"**💊 처방전:** {selected['처방']}")
        st.write(f"**⚡ 에너지 보정:** 당신의 활력({energy}%)에 최적화된 선택입니다.")
        
    with col2:
        # 데이터 시각화 (이과적 분석 요소)
        st.write("**📊 영화 분석 데이터**")
        chart_data = pd.DataFrame({
            "항목": list(selected['지표'].keys()),
            "수치": list(selected['지표'].values())
        })
        st.bar_chart(data=chart_data, x="항목", y="수치")

st.divider()
st.caption("제작: 2026 소프트웨어 수행평가 (데이터 기반 추천 알고리즘 구현)")
