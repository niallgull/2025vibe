# songs_list.py 파일에 다음과 같은 내용이 있어야 합니다:
# songs = [ {"mood": ..., "genre": ..., ...}, ... ]
# 파일 이름은 반드시 songs_list.py 여야 하며, main 파일과 같은 디렉토리에 있어야 합니다.

from songs_list import songs  # 이 줄은 songs_list.py와 같은 폴더에 있어야만 정상 작동합니다.

import streamlit as st
import random

st.set_page_config(
    page_title="K-POP 노래 추천기",
    page_icon="🎵",
    layout="centered"
)

st.markdown("""
    <h1 style='color:#4B3621; text-align:center; animation: pulse 2s infinite;'>
        🎶 오늘의 기분으로 추천하는 K-POP 🎶
    </h1>
    <style>
        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.03); }
            100% { transform: scale(1); }
        }
        .stButton > button {
            background-color: #f5f1e6;
            color: #4B3621;
            border: none;
            padding: 0.6em 1.2em;
            border-radius: 10px;
            box-shadow: 2px 2px 5px #d2cfc4;
            transition: all 0.3s ease;
        }
        .stButton > button:hover {
            box-shadow: 2px 2px 12px #a48f77;
            background-color: #e8e3d4;
        }
    </style>
""", unsafe_allow_html=True)

mood = st.selectbox("지금 기분은 어떤가요?", sorted(set(song['mood'] for song in songs)))
genre = st.selectbox("듣고 싶은 장르는?", sorted(set(song['genre'] for song in songs)))

# 추천 기록 저장용 세션 상태 초기화
if "history" not in st.session_state:
    st.session_state.history = []

# 곡 추천 버튼
if st.button("🎲 아무거나 추천해줘!"):
    candidates = [song for song in songs if song['mood'] == mood and song['genre'] == genre]
    if candidates:
        # 이전에 추천된 곡 제외
        candidates = [c for c in candidates if c not in st.session_state.history]
        if candidates:
            song = random.choice(candidates)
        else:
            st.warning("추천 가능한 새로운 곡이 없어요! 기록을 초기화해 주세요.")
            song = None
        if song:
            st.session_state.history.append(song)
            st.image(song['image'], use_column_width=True)
            st.markdown(f"### 🎧 {song['title']} - {song['artist']}")
            st.markdown(f"[뮤직비디오 보러가기 🎬]({song['youtube']})")
    else:
        st.warning("선택한 조건에 맞는 곡이 없어요!")

# 기록 초기화 버튼
col1, col2 = st.columns([1, 5])
with col1:
    if st.button("🗑️ 기록 초기화"):
        st.session_state.history = []

# 추천 기록 출력
with col2:
    if st.session_state.history:
        st.markdown("### 📜 지금까지 추천받은 노래")
        for idx, s in enumerate(st.session_state.history[::-1], 1):
            st.markdown(f"{idx}. **{s['title']} - {s['artist']}**")
