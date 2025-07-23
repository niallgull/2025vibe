# ✅ 필요한 라이브러리 임포트
import streamlit as st
import random
from songs_list import songs 

# ✅ 세션 상태 초기화 (중복 방지와 기록 보관용)
if "history" not in st.session_state:
    st.session_state.history = []

# ✅ 폰트와 스타일 지정 (포근한 아이보리 테마 + 애니메이션 효과)
st.markdown("""
    <style>
    @import url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2104@1.0/NanumSquareRound.css');
    html, body, [class*="css"]  {
        font-family: 'NanumSquareRound', sans-serif !important;
        background-color: #fffdf7;
    }
    .stButton > button {
        background-color: #f5e8d6;
        color: #4a2c2a;
        border-radius: 10px;
        border: 1px solid #e3d5c0;
        padding: 0.5em 1.2em;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        background-color: #ecdcc4;
        box-shadow: 0 0 8px #a9745f;
    }
    .title-animated {
        font-size: 2.5em;
        font-weight: bold;
        color: #4a2c2a;
        animation: float 3s ease-in-out infinite;
    }
    @keyframes float {
        0% {transform: translateY(0px);}
        50% {transform: translateY(-5px);}
        100% {transform: translateY(0px);}
    }
    </style>
""", unsafe_allow_html=True)

# ✅ 앱 제목
st.markdown('<h1 class="title-animated">🎵 K-POP 아이돌 노래 추천기</h1>', unsafe_allow_html=True)

# ✅ 기분과 장르 선택
moods = ["설렘", "쓸쓸함", "자신감", "기분전환", "우울함", "신남", "힐링", "위로받고 싶음", "비 오는 날", "친구들과 함께", "추억에 잠기고 싶을 때"]
genres = ["댄스", "인디팝", "발라드", "록", "힙합", "R&B", "EDM", "시티팝", "어쿠스틱", "라틴팝", "팝"]

selected_mood = st.selectbox("기분을 골라주세요", moods)
selected_genre = st.selectbox("장르를 골라주세요", genres)

# ✅ 조건 기반 추천
if st.button("🔍 추천받기"):
    filtered = [s for s in songs if s["mood"] == selected_mood and s["genre"] == selected_genre]
    if filtered:
        song = random.choice(filtered)
        st.session_state.history.append(song)
        st.success("✨ 추천 노래 ✨")
        st.image(song["image"], width=300, caption=f"{song['title']} - {song['artist']}")
        st.markdown(f"[유튜브에서 보기 🎮]({song['youtube']})", unsafe_allow_html=True)
    else:
        st.warning("해당 조건에 맞는 곡이 없어요. 😭")

# ✅ 아무거나 추천하기
st.markdown("## 🎲 아무것도 추천받기")
if st.button(":game_die: 아무거나 추천해줘!"):
    remaining = [s for s in songs if s not in st.session_state.history]
    if not remaining:
        st.warning("모든 곡을 추천했어요! 기록을 초기화할게요.")
        st.session_state.history = []
        remaining = songs[:]
    s = random.choice(remaining)
    st.session_state.history.append(s)
    st.toast("✨ 새로운 노래를 추천할게요!", icon="🎵")
    st.image(s["image"], width=300, caption=f"{s['title']} - {s['artist']}")
    st.markdown(f"**🎶 {s['title']}** by *{s['artist']}*")
    st.markdown(f"[유튜브에서 보기 🎮]({s['youtube']})", unsafe_allow_html=True)

# ✅ 기록 초기화 버튼과 함께 추천 내역 보여주기
col1, col2 = st.columns([1, 5])
with col1:
    if st.button("🪹 기록 초기화"):
        st.session_state.history = []
        st.success("추천 기록이 초기화되었어요!")

with col2:
    st.markdown("### 📜 지금까지 추천받은 노래")
    if st.session_state.history:
        for idx, h in enumerate(st.session_state.history[::-1], 1):
            st.markdown(f"{idx}. **{h['title']}** by *{h['artist']}*")
    else:
        st.markdown("아직 추천받은 노래가 없어요!")

