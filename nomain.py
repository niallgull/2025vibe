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
songs_list.py
songs = [
    {'mood': '설렘', 'genre': '댄스', 'title': 'Cupid', 'artist': 'FIFTY FIFTY', 'youtube': 'https://youtu.be/6uvUTz0uP3k', 'image': 'https://i.ytimg.com/vi/6uvUTz0uP3k/hqdefault.jpg'},
    {'mood': '설렘', 'genre': '인디팝', 'title': 'LOVE SCENARIO', 'artist': 'iKON', 'youtube': 'https://youtu.be/vecSVX1QYbQ', 'image': 'https://i.ytimg.com/vi/vecSVX1QYbQ/hqdefault.jpg'},
    {'mood': '설렘', 'genre': '발라드', 'title': 'Love Dive', 'artist': 'IVE', 'youtube': 'https://youtu.be/Y8JFxS1HlDo', 'image': 'https://i.ytimg.com/vi/Y8JFxS1HlDo/hqdefault.jpg'},
    {'mood': '설렘', 'genre': '록', 'title': 'Polaroid Love', 'artist': 'ENHYPEN', 'youtube': 'https://youtu.be/HGt-I6_hDk4', 'image': 'https://i.ytimg.com/vi/HGt-I6_hDk4/hqdefault.jpg'},
    {'mood': '설렘', 'genre': '힙합', 'title': 'Love Shot', 'artist': 'EXO', 'youtube': 'https://youtu.be/pSudEWBAYRE', 'image': 'https://i.ytimg.com/vi/pSudEWBAYRE/hqdefault.jpg'},
    {'mood': '설렘', 'genre': 'R&B', 'title': 'Spring Day', 'artist': 'BTS', 'youtube': 'https://youtu.be/xEeFrLSkMm8', 'image': 'https://i.ytimg.com/vi/xEeFrLSkMm8/hqdefault.jpg'},
    {'mood': '설렘', 'genre': 'EDM', 'title': 'Magnetic', 'artist': 'ILLIT', 'youtube': 'https://youtu.be/Vk5-c_v4gMU', 'image': 'https://i.ytimg.com/vi/Vk5-c_v4gMU/hqdefault.jpg'},
    {'mood': '설렘', 'genre': '시티팝', 'title': 'Feel Special', 'artist': 'TWICE', 'youtube': 'https://youtu.be/3ymwOvzhwHs', 'image': 'https://i.ytimg.com/vi/3ymwOvzhwHs/hqdefault.jpg'},
    {'mood': '설렘', 'genre': '어쿠스틱', 'title': 'Red Flavor', 'artist': 'Red Velvet', 'youtube': 'https://youtu.be/WyiIGEHQP8o', 'image': 'https://i.ytimg.com/vi/WyiIGEHQP8o/hqdefault.jpg'},
    {'mood': '설렘', 'genre': '라틴팝', 'title': 'Love Shot', 'artist': 'EXO', 'youtube': 'https://youtu.be/pSudEWBAYRE', 'image': 'https://i.ytimg.com/vi/pSudEWBAYRE/hqdefault.jpg'},
    {'mood': '설렘', 'genre': '팝', 'title': 'Love Dive', 'artist': 'IVE', 'youtube': 'https://youtu.be/Y8JFxS1HlDo', 'image': 'https://i.ytimg.com/vi/Y8JFxS1HlDo/hqdefault.jpg'},
    {'mood': '쓸쓸함', 'genre': '댄스', 'title': 'Cupid', 'artist': 'FIFTY FIFTY', 'youtube': 'https://youtu.be/6uvUTz0uP3k', 'image': 'https://i.ytimg.com/vi/6uvUTz0uP3k/hqdefault.jpg'},
    {'mood': '쓸쓸함', 'genre': '인디팝', 'title': 'Red Flavor', 'artist': 'Red Velvet', 'youtube': 'https://youtu.be/WyiIGEHQP8o', 'image': 'https://i.ytimg.com/vi/WyiIGEHQP8o/hqdefault.jpg'},
    {'mood': '쓸쓸함', 'genre': '발라드', 'title': 'Magnetic', 'artist': 'ILLIT', 'youtube': 'https://youtu.be/Vk5-c_v4gMU', 'image': 'https://i.ytimg.com/vi/Vk5-c_v4gMU/hqdefault.jpg'},
    {'mood': '쓸쓸함', 'genre': '록', 'title': 'Cupid', 'artist': 'FIFTY FIFTY', 'youtube': 'https://youtu.be/6uvUTz0uP3k', 'image': 'https://i.ytimg.com/vi/6uvUTz0uP3k/hqdefault.jpg'},
    {'mood': '쓸쓸함', 'genre': '힙합', 'title': 'Magnetic', 'artist': 'ILLIT', 'youtube': 'https://youtu.be/Vk5-c_v4gMU', 'image': 'https://i.ytimg.com/vi/Vk5-c_v4gMU/hqdefault.jpg'},
    {'mood': '쓸쓸함', 'genre': 'R&B', 'title': 'Hype Boy', 'artist': 'NewJeans', 'youtube': 'https://youtu.be/js1CtxSY38I', 'image': 'https://i.ytimg.com/vi/js1CtxSY38I/hqdefault.jpg'},
    {'mood': '쓸쓸함', 'genre': 'EDM', 'title': 'Blue Hour', 'artist': 'TXT', 'youtube': 'https://youtu.be/Vd9QkWsd5p4', 'image': 'https://i.ytimg.com/vi/Vd9QkWsd5p4/hqdefault.jpg'},
    {'mood': '쓸쓸함', 'genre': '시티팝', 'title': 'Love Shot', 'artist': 'EXO', 'youtube': 'https://youtu.be/pSudEWBAYRE', 'image': 'https://i.ytimg.com/vi/pSudEWBAYRE/hqdefault.jpg'},
    {'mood': '쓸쓸함', 'genre': '어쿠스틱', 'title': 'Blue Hour', 'artist': 'TXT', 'youtube': 'https://youtu.be/Vd9QkWsd5p4', 'image': 'https://i.ytimg.com/vi/Vd9QkWsd5p4/hqdefault.jpg'},
    {'mood': '쓸쓸함', 'genre': '라틴팝', 'title': 'Polaroid Love', 'artist': 'ENHYPEN', 'youtube': 'https://youtu.be/HGt-I6_hDk4', 'image': 'https://i.ytimg.com/vi/HGt-I6_hDk4/hqdefault.jpg'},
    {'mood': '쓸쓸함', 'genre': '팝', 'title': 'Polaroid Love', 'artist': 'ENHYPEN', 'youtube': 'https://youtu.be/HGt-I6_hDk4', 'image': 'https://i.ytimg.com/vi/HGt-I6_hDk4/hqdefault.jpg'},
    {'mood': '자신감', 'genre': '댄스', 'title': 'Spring Day', 'artist': 'BTS', 'youtube': 'https://youtu.be/xEeFrLSkMm8', 'image': 'https://i.ytimg.com/vi/xEeFrLSkMm8/hqdefault.jpg'},
    {'mood': '자신감', 'genre': '인디팝', 'title': 'Red Flavor', 'artist': 'Red Velvet', 'youtube': 'https://youtu.be/WyiIGEHQP8o', 'image': 'https://i.ytimg.com/vi/WyiIGEHQP8o/hqdefault.jpg'},
    {'mood': '자신감', 'genre': '발라드', 'title': 'Feel Special', 'artist': 'TWICE', 'youtube': 'https://youtu.be/3ymwOvzhwHs', 'image': 'https://i.ytimg.com/vi/3ymwOvzhwHs/hqdefault.jpg'},
    {'mood': '자신감', 'genre': '록', 'title': 'Love Shot', 'artist': 'EXO', 'youtube': 'https://youtu.be/pSudEWBAYRE', 'image': 'https://i.ytimg.com/vi/pSudEWBAYRE/hqdefault.jpg'},
    {'mood': '자신감', 'genre': '힙합', 'title': 'Blue Hour', 'artist': 'TXT', 'youtube': 'https://youtu.be/Vd9QkWsd5p4', 'image': 'https://i.ytimg.com/vi/Vd9QkWsd5p4/hqdefault.jpg'},
    {'mood': '자신감', 'genre': 'R&B', 'title': 'Red Flavor', 'artist': 'Red Velvet', 'youtube': 'https://youtu.be/WyiIGEHQP8o', 'image': 'https://i.ytimg.com/vi/WyiIGEHQP8o/hqdefault.jpg'},
    {'mood': '자신감', 'genre': 'EDM', 'title': 'Spring Day', 'artist': 'BTS', 'youtube': 'https://youtu.be/xEeFrLSkMm8', 'image': 'https://i.ytimg.com/vi/xEeFrLSkMm8/hqdefault.jpg'},
    {'mood': '자신감', 'genre': '시티팝', 'title': 'Spring Day', 'artist': 'BTS', 'youtube': 'https://youtu.be/xEeFrLSkMm8', 'image': 'https://i.ytimg.com/vi/xEeFrLSkMm8/hqdefault.jpg'},
    {'mood': '자신감', 'genre': '어쿠스틱', 'title': 'Cupid', 'artist': 'FIFTY FIFTY', 'youtube': 'https://youtu.be/6uvUTz0uP3k', 'image': 'https://i.ytimg.com/vi/6uvUTz0uP3k/hqdefault.jpg'},
    {'mood': '자신감', 'genre': '라틴팝', 'title': 'Hype Boy', 'artist': 'NewJeans', 'youtube': 'https://youtu.be/js1CtxSY38I', 'image': 'https://i.ytimg.com/vi/js1CtxSY38I/hqdefault.jpg'},
    {'mood': '자신감', 'genre': '팝', 'title': 'LOVE SCENARIO', 'artist': 'iKON', 'youtube': 'https://youtu.be/vecSVX1QYbQ', 'image': 'https://i.ytimg.com/vi/vecSVX1QYbQ/hqdefault.jpg'},
    {'mood': '기분전환', 'genre': '댄스', 'title': 'Feel Special', 'artist': 'TWICE', 'youtube': 'https://youtu.be/3ymwOvzhwHs', 'image': 'https://i.ytimg.com/vi/3ymwOvzhwHs/hqdefault.jpg'},
    {'mood': '기분전환', 'genre': '인디팝', 'title': 'Feel Special', 'artist': 'TWICE', 'youtube': 'https://youtu.be/3ymwOvzhwHs', 'image': 'https://i.ytimg.com/vi/3ymwOvzhwHs/hqdefault.jpg'},
    {'mood': '기분전환', 'genre': '발라드', 'title': 'Red Flavor', 'artist': 'Red Velvet', 'youtube': 'https://youtu.be/WyiIGEHQP8o', 'image': 'https://i.ytimg.com/vi/WyiIGEHQP8o/hqdefault.jpg'},
    {'mood': '기분전환', 'genre': '록', 'title': 'Feel Special', 'artist': 'TWICE', 'youtube': 'https://youtu.be/3ymwOvzhwHs', 'image': 'https://i.ytimg.com/vi/3ymwOvzhwHs/hqdefault.jpg'},
    {'mood': '기분전환', 'genre': '힙합', 'title': 'Polaroid Love', 'artist': 'ENHYPEN', 'youtube': 'https://youtu.be/HGt-I6_hDk4', 'image': 'https://i.ytimg.com/vi/HGt-I6_hDk4/hqdefault.jpg'},
    {'mood': '기분전환', 'genre': 'R&B', 'title': 'Feel Special', 'artist': 'TWICE', 'youtube': 'https://youtu.be/3ymwOvzhwHs', 'image': 'https://i.ytimg.com/vi/3ymwOvzhwHs/hqdefault.jpg'},
    {'mood': '기분전환', 'genre': 'EDM', 'title': 'Cupid', 'artist': 'FIFTY FIFTY', 'youtube': 'https://youtu.be/6uvUTz0uP3k', 'image': 'https://i.ytimg.com/vi/6uvUTz0uP3k/hqdefault.jpg'},
    {'mood': '기분전환', 'genre': '시티팝', 'title': 'LOVE SCENARIO', 'artist': 'iKON', 'youtube': 'https://youtu.be/vecSVX1QYbQ', 'image': 'https://i.ytimg.com/vi/vecSVX1QYbQ/hqdefault.jpg'},
    {'mood': '기분전환', 'genre': '어쿠스틱', 'title': 'Spring Day', 'artist': 'BTS', 'youtube': 'https://youtu.be/xEeFrLSkMm8', 'image': 'https://i.ytimg.com/vi/xEeFrLSkMm8/hqdefault.jpg'},
    {'mood': '기분전환', 'genre': '라틴팝', 'title': 'Cupid', 'artist': 'FIFTY FIFTY', 'youtube': 'https://youtu.be/6uvUTz0uP3k', 'image': 'https://i.ytimg.com/vi/6uvUTz0uP3k/hqdefault.jpg'},
    {'mood': '기분전환', 'genre': '팝', 'title': 'Hype Boy', 'artist': 'NewJeans', 'youtube': 'https://youtu.be/js1CtxSY38I', 'image': 'https://i.ytimg.com/vi/js1CtxSY38I/hqdefault.jpg'},
    {'mood': '우울함', 'genre': '댄스', 'title': 'Feel Special', 'artist': 'TWICE', 'youtube': 'https://youtu.be/3ymwOvzhwHs', 'image': 'https://i.ytimg.com/vi/3ymwOvzhwHs/hqdefault.jpg'},
    {'mood': '우울함', 'genre': '인디팝', 'title': 'Magnetic', 'artist': 'ILLIT', 'youtube': 'https://youtu.be/Vk5-c_v4gMU', 'image': 'https://i.ytimg.com/vi/Vk5-c_v4gMU/hqdefault.jpg'},
    {'mood': '우울함', 'genre': '발라드', 'title': 'Love Dive', 'artist': 'IVE', 'youtube': 'https://youtu.be/Y8JFxS1HlDo', 'image': 'https://i.ytimg.com/vi/Y8JFxS1HlDo/hqdefault.jpg'},
    {'mood': '우울함', 'genre': '록', 'title': 'Love Shot', 'artist': 'EXO', 'youtube': 'https://youtu.be/pSudEWBAYRE', 'image': 'https://i.ytimg.com/vi/pSudEWBAYRE/hqdefault.jpg'},
    {'mood': '우울함', 'genre': '힙합', 'title': 'Red Flavor', 'artist': 'Red Velvet', 'youtube': 'https://youtu.be/WyiIGEHQP8o', 'image': 'https://i.ytimg.com/vi/WyiIGEHQP8o/hqdefault.jpg'},
    {'mood': '우울함', 'genre': 'R&B', 'title': 'Red Flavor', 'artist': 'Red Velvet', 'youtube': 'https://youtu.be/WyiIGEHQP8o', 'image': 'https://i.ytimg.com/vi/WyiIGEHQP8o/hqdefault.jpg'},
    {'mood': '우울함', 'genre': 'EDM', 'title': 'Feel Special', 'artist': 'TWICE', 'youtube': 'https://youtu.be/3ymwOvzhwHs', 'image': 'https://i.ytimg.com/vi/3ymwOvzhwHs/hqdefault.jpg'},
    {'mood': '우울함', 'genre': '시티팝', 'title': 'Magnetic', 'artist': 'ILLIT', 'youtube': 'https://youtu.be/Vk5-c_v4gMU', 'image': 'https://i.ytimg.com/vi/Vk5-c_v4gMU/hqdefault.jpg'},
    {'mood': '우울함', 'genre': '어쿠스틱', 'title': 'Blue Hour', 'artist': 'TXT', 'youtube': 'https://youtu.be/Vd9QkWsd5p4', 'image': 'https://i.ytimg.com/vi/Vd9QkWsd5p4/hqdefault.jpg'},
    {'mood': '우울함', 'genre': '라틴팝', 'title': 'Love Shot', 'artist': 'EXO', 'youtube': 'https://youtu.be/pSudEWBAYRE', 'image': 'https://i.ytimg.com/vi/pSudEWBAYRE/hqdefault.jpg'},
    {'mood': '우울함', 'genre': '팝', 'title': 'Red Flavor', 'artist': 'Red Velvet', 'youtube': 'https://youtu.be/WyiIGEHQP8o', 'image': 'https://i.ytimg.com/vi/WyiIGEHQP8o/hqdefault.jpg'},
    {'mood': '신남', 'genre': '댄스', 'title': 'Cupid', 'artist': 'FIFTY FIFTY', 'youtube': 'https://youtu.be/6uvUTz0uP3k', 'image': 'https://i.ytimg.com/vi/6uvUTz0uP3k/hqdefault.jpg'},
    {'mood': '신남', 'genre': '인디팝', 'title': 'Blue Hour', 'artist': 'TXT', 'youtube': 'https://youtu.be/Vd9QkWsd5p4', 'image': 'https://i.ytimg.com/vi/Vd9QkWsd5p4/hqdefault.jpg'},
    {'mood': '신남', 'genre': '발라드', 'title': 'Love Dive', 'artist': 'IVE', 'youtube': 'https://youtu.be/Y8JFxS1HlDo', 'image': 'https://i.ytimg.com/vi/Y8JFxS1HlDo/hqdefault.jpg'},
    {'mood': '신남', 'genre': '록', 'title': 'Magnetic', 'artist': 'ILLIT', 'youtube': 'https://youtu.be/Vk5-c_v4gMU', 'image': 'https://i.ytimg.com/vi/Vk5-c_v4gMU/hqdefault.jpg'},
    {'mood': '신남', 'genre': '힙합', 'title': 'Cupid', 'artist': 'FIFTY FIFTY', 'youtube': 'https://youtu.be/6uvUTz0uP3k', 'image': 'https://i.ytimg.com/vi/6uvUTz0uP3k/hqdefault.jpg'},
    {'mood': '신남', 'genre': 'R&B', 'title': 'Hype Boy', 'artist': 'NewJeans', 'youtube': 'https://youtu.be/js1CtxSY38I', 'image': 'https://i.ytimg.com/vi/js1CtxSY38I/hqdefault.jpg'},
    {'mood': '신남', 'genre': 'EDM', 'title': 'LOVE SCENARIO', 'artist': 'iKON', 'youtube': 'https://youtu.be/vecSVX1QYbQ', 'image': 'https://i.ytimg.com/vi/vecSVX1QYbQ/hqdefault.jpg'},
    {'mood': '신남', 'genre': '시티팝', 'title': 'Hype Boy', 'artist': 'NewJeans', 'youtube': 'https://youtu.be/js1CtxSY38I', 'image': 'https://i.ytimg.com/vi/js1CtxSY38I/hqdefault.jpg'},
    {'mood': '신남', 'genre': '어쿠스틱', 'title': 'Red Flavor', 'artist': 'Red Velvet', 'youtube': 'https://youtu.be/WyiIGEHQP8o', 'image': 'https://i.ytimg.com/vi/WyiIGEHQP8o/hqdefault.jpg'},
    {'mood': '신남', 'genre': '라틴팝', 'title': 'Love Dive', 'artist': 'IVE', 'youtube': 'https://youtu.be/Y8JFxS1HlDo', 'image': 'https://i.ytimg.com/vi/Y8JFxS1HlDo/hqdefault.jpg'},
    {'mood': '신남', 'genre': '팝', 'title': 'LOVE SCENARIO', 'artist': 'iKON', 'youtube': 'https://youtu.be/vecSVX1QYbQ', 'image': 'https://i.ytimg.com/vi/vecSVX1QYbQ/hqdefault.jpg'},
    {'mood': '힐링', 'genre': '댄스', 'title': 'LOVE SCENARIO', 'artist': 'iKON', 'youtube': 'https://youtu.be/vecSVX1QYbQ', 'image': 'https://i.ytimg.com/vi/vecSVX1QYbQ/hqdefault.jpg'},
    {'mood': '힐링', 'genre': '인디팝', 'title': 'Love Dive', 'artist': 'IVE', 'youtube': 'https://youtu.be/Y8JFxS1HlDo', 'image': 'https://i.ytimg.com/vi/Y8JFxS1HlDo/hqdefault.jpg'},
    {'mood': '힐링', 'genre': '발라드', 'title': 'Cupid', 'artist': 'FIFTY FIFTY', 'youtube': 'https://youtu.be/6uvUTz0uP3k', 'image': 'https://i.ytimg.com/vi/6uvUTz0uP3k/hqdefault.jpg'},
    {'mood': '힐링', 'genre': '록', 'title': 'Feel Special', 'artist': 'TWICE', 'youtube': 'https://youtu.be/3ymwOvzhwHs', 'image': 'https://i.ytimg.com/vi/3ymwOvzhwHs/hqdefault.jpg'},
    {'mood': '힐링', 'genre': '힙합', 'title': 'Feel Special', 'artist': 'TWICE', 'youtube': 'https://youtu.be/3ymwOvzhwHs', 'image': 'https://i.ytimg.com/vi/3ymwOvzhwHs/hqdefault.jpg'},
    {'mood': '힐링', 'genre': 'R&B', 'title': 'Love Shot', 'artist': 'EXO', 'youtube': 'https://youtu.be/pSudEWBAYRE', 'image': 'https://i.ytimg.com/vi/pSudEWBAYRE/hqdefault.jpg'},
    {'mood': '힐링', 'genre': 'EDM', 'title': 'Love Shot', 'artist': 'EXO', 'youtube': 'https://youtu.be/pSudEWBAYRE', 'image': 'https://i.ytimg.com/vi/pSudEWBAYRE/hqdefault.jpg'},
    {'mood': '힐링', 'genre': '시티팝', 'title': 'Blue Hour', 'artist': 'TXT', 'youtube': 'https://youtu.be/Vd9QkWsd5p4', 'image': 'https://i.ytimg.com/vi/Vd9QkWsd5p4/hqdefault.jpg'},
    {'mood': '힐링', 'genre': '어쿠스틱', 'title': 'Magnetic', 'artist': 'ILLIT', 'youtube': 'https://youtu.be/Vk5-c_v4gMU', 'image': 'https://i.ytimg.com/vi/Vk5-c_v4gMU/hqdefault.jpg'},
    {'mood': '힐링', 'genre': '라틴팝', 'title': 'Love Dive', 'artist': 'IVE', 'youtube': 'https://youtu.be/Y8JFxS1HlDo', 'image': 'https://i.ytimg.com/vi/Y8JFxS1HlDo/hqdefault.jpg'},
    {'mood': '힐링', 'genre': '팝', 'title': 'Feel Special', 'artist': 'TWICE', 'youtube': 'https://youtu.be/3ymwOvzhwHs', 'image': 'https://i.ytimg.com/vi/3ymwOvzhwHs/hqdefault.jpg'},
    {'mood': '위로받고 싶음', 'genre': '댄스', 'title': 'Love Dive', 'artist': 'IVE', 'youtube': 'https://youtu.be/Y8JFxS1HlDo', 'image': 'https://i.ytimg.com/vi/Y8JFxS1HlDo/hqdefault.jpg'},
    {'mood': '위로받고 싶음', 'genre': '인디팝', 'title': 'Cupid', 'artist': 'FIFTY FIFTY', 'youtube': 'https://youtu.be/6uvUTz0uP3k', 'image': 'https://i.ytimg.com/vi/6uvUTz0uP3k/hqdefault.jpg'},
    {'mood': '위로받고 싶음', 'genre': '발라드', 'title': 'LOVE SCENARIO', 'artist': 'iKON', 'youtube': 'https://youtu.be/vecSVX1QYbQ', 'image': 'https://i.ytimg.com/vi/vecSVX1QYbQ/hqdefault.jpg'},
    {'mood': '위로받고 싶음', 'genre': '록', 'title': 'LOVE SCENARIO', 'artist': 'iKON', 'youtube': 'https://youtu.be/vecSVX1QYbQ', 'image': 'https://i.ytimg.com/vi/vecSVX1QYbQ/hqdefault.jpg'},
    {'mood': '위로받고 싶음', 'genre': '힙합', 'title': 'Blue Hour', 'artist': 'TXT', 'youtube': 'https://youtu.be/Vd9QkWsd5p4', 'image': 'https://i.ytimg.com/vi/Vd9QkWsd5p4/hqdefault.jpg'},
    {'mood': '위로받고 싶음', 'genre': 'R&B', 'title': 'LOVE SCENARIO', 'artist': 'iKON', 'youtube': 'https://youtu.be/vecSVX1QYbQ', 'image': 'https://i.ytimg.com/vi/vecSVX1QYbQ/hqdefault.jpg'},
    {'mood': '위로받고 싶음', 'genre': 'EDM', 'title': 'Love Dive', 'artist': 'IVE', 'youtube': 'https://youtu.be/Y8JFxS1HlDo', 'image': 'https://i.ytimg.com/vi/Y8JFxS1HlDo/hqdefault.jpg'},
    {'mood': '위로받고 싶음', 'genre': '시티팝', 'title': 'Love Shot', 'artist': 'EXO', 'youtube': 'https://youtu.be/pSudEWBAYRE', 'image': 'https://i.ytimg.com/vi/pSudEWBAYRE/hqdefault.jpg'},
    {'mood': '위로받고 싶음', 'genre': '어쿠스틱', 'title': 'Red Flavor', 'artist': 'Red Velvet', 'youtube': 'https://youtu.be/WyiIGEHQP8o', 'image': 'https://i.ytimg.com/vi/WyiIGEHQP8o/hqdefault.jpg'},
    {'mood': '위로받고 싶음', 'genre': '라틴팝', 'title': 'Polaroid Love', 'artist': 'ENHYPEN', 'youtube': 'https://youtu.be/HGt-I6_hDk4', 'image': 'https://i.ytimg.com/vi/HGt-I6_hDk4/hqdefault.jpg'},
    {'mood': '위로받고 싶음', 'genre': '팝', 'title': 'Blue Hour', 'artist': 'TXT', 'youtube': 'https://youtu.be/Vd9QkWsd5p4', 'image': 'https://i.ytimg.com/vi/Vd9QkWsd5p4/hqdefault.jpg'},
    {'mood': '비 오는 날', 'genre': '댄스', 'title': 'Love Dive', 'artist': 'IVE', 'youtube': 'https://youtu.be/Y8JFxS1HlDo', 'image': 'https://i.ytimg.com/vi/Y8JFxS1HlDo/hqdefault.jpg'},
    {'mood': '비 오는 날', 'genre': '인디팝', 'title': 'Polaroid Love', 'artist': 'ENHYPEN', 'youtube': 'https://youtu.be/HGt-I6_hDk4', 'image': 'https://i.ytimg.com/vi/HGt-I6_hDk4/hqdefault.jpg'},
    {'mood': '비 오는 날', 'genre': '발라드', 'title': 'Red Flavor', 'artist': 'Red Velvet', 'youtube': 'https://youtu.be/WyiIGEHQP8o', 'image': 'https://i.ytimg.com/vi/WyiIGEHQP8o/hqdefault.jpg'},
    {'mood': '비 오는 날', 'genre': '록', 'title': 'Love Dive', 'artist': 'IVE', 'youtube': 'https://youtu.be/Y8JFxS1HlDo', 'image': 'https://i.ytimg.com/vi/Y8JFxS1HlDo/hqdefault.jpg'},
    {'mood': '비 오는 날', 'genre': '힙합', 'title': 'Love Shot', 'artist': 'EXO', 'youtube': 'https://youtu.be/pSudEWBAYRE', 'image': 'https://i.ytimg.com/vi/pSudEWBAYRE/hqdefault.jpg'},
    {'mood': '비 오는 날', 'genre': 'R&B', 'title': 'Hype Boy', 'artist': 'NewJeans', 'youtube': 'https://youtu.be/js1CtxSY38I', 'image': 'https://i.ytimg.com/vi/js1CtxSY38I/hqdefault.jpg'},
    {'mood': '비 오는 날', 'genre': 'EDM', 'title': 'Magnetic', 'artist': 'ILLIT', 'youtube': 'https://youtu.be/Vk5-c_v4gMU', 'image': 'https://i.ytimg.com/vi/Vk5-c_v4gMU/hqdefault.jpg'},
    {'mood': '비 오는 날', 'genre': '시티팝', 'title': 'Red Flavor', 'artist': 'Red Velvet', 'youtube': 'https://youtu.be/WyiIGEHQP8o', 'image': 'https://i.ytimg.com/vi/WyiIGEHQP8o/hqdefault.jpg'},
    {'mood': '비 오는 날', 'genre': '어쿠스틱', 'title': 'Spring Day', 'artist': 'BTS', 'youtube': 'https://youtu.be/xEeFrLSkMm8', 'image': 'https://i.ytimg.com/vi/xEeFrLSkMm8/hqdefault.jpg'},
    {'mood': '비 오는 날', 'genre': '라틴팝', 'title': 'Cupid', 'artist': 'FIFTY FIFTY', 'youtube': 'https://youtu.be/6uvUTz0uP3k', 'image': 'https://i.ytimg.com/vi/6uvUTz0uP3k/hqdefault.jpg'},
    {'mood': '비 오는 날', 'genre': '팝', 'title': 'Red Flavor', 'artist': 'Red Velvet', 'youtube': 'https://youtu.be/WyiIGEHQP8o', 'image': 'https://i.ytimg.com/vi/WyiIGEHQP8o/hqdefault.jpg'},
    {'mood': '친구들과 함께', 'genre': '댄스', 'title': 'Feel Special', 'artist': 'TWICE', 'youtube': 'https://youtu.be/3ymwOvzhwHs', 'image': 'https://i.ytimg.com/vi/3ymwOvzhwHs/hqdefault.jpg'},
    {'mood': '친구들과 함께', 'genre': '인디팝', 'title': 'Feel Special', 'artist': 'TWICE', 'youtube': 'https://youtu.be/3ymwOvzhwHs', 'image': 'https://i.ytimg.com/vi/3ymwOvzhwHs/hqdefault.jpg'},
    {'mood': '친구들과 함께', 'genre': '발라드', 'title': 'Polaroid Love', 'artist': 'ENHYPEN', 'youtube': 'https://youtu.be/HGt-I6_hDk4', 'image': 'https://i.ytimg.com/vi/HGt-I6_hDk4/hqdefault.jpg'},
    {'mood': '친구들과 함께', 'genre': '록', 'title': 'Love Dive', 'artist': 'IVE', 'youtube': 'https://youtu.be/Y8JFxS1HlDo', 'image': 'https://i.ytimg.com/vi/Y8JFxS1HlDo/hqdefault.jpg'},
    {'mood': '친구들과 함께', 'genre': '힙합', 'title': 'Blue Hour', 'artist': 'TXT', 'youtube': 'https://youtu.be/Vd9QkWsd5p4', 'image': 'https://i.ytimg.com/vi/Vd9QkWsd5p4/hqdefault.jpg'},
    {'mood': '친구들과 함께', 'genre': 'R&B', 'title': 'Red Flavor', 'artist': 'Red Velvet', 'youtube': 'https://youtu.be/WyiIGEHQP8o', 'image': 'https://i.ytimg.com/vi/WyiIGEHQP8o/hqdefault.jpg'},
    {'mood': '친구들과 함께', 'genre': 'EDM', 'title': 'Cupid', 'artist': 'FIFTY FIFTY', 'youtube': 'https://youtu.be/6uvUTz0uP3k', 'image': 'https://i.ytimg.com/vi/6uvUTz0uP3k/hqdefault.jpg'},
    {'mood': '친구들과 함께', 'genre': '시티팝', 'title': 'Hype Boy', 'artist': 'NewJeans', 'youtube': 'https://youtu.be/js1CtxSY38I', 'image': 'https://i.ytimg.com/vi/js1CtxSY38I/hqdefault.jpg'},
    {'mood': '친구들과 함께', 'genre': '어쿠스틱', 'title': 'Magnetic', 'artist': 'ILLIT', 'youtube': 'https://youtu.be/Vk5-c_v4gMU', 'image': 'https://i.ytimg.com/vi/Vk5-c_v4gMU/hqdefault.jpg'},
    {'mood': '친구들과 함께', 'genre': '라틴팝', 'title': 'Magnetic', 'artist': 'ILLIT', 'youtube': 'https://youtu.be/Vk5-c_v4gMU', 'image': 'https://i.ytimg.com/vi/Vk5-c_v4gMU/hqdefault.jpg'},
    {'mood': '친구들과 함께', 'genre': '팝', 'title': 'Magnetic', 'artist': 'ILLIT', 'youtube': 'https://youtu.be/Vk5-c_v4gMU', 'image': 'https://i.ytimg.com/vi/Vk5-c_v4gMU/hqdefault.jpg'},
    {'mood': '추억에 잠기고 싶을 때', 'genre': '댄스', 'title': 'Blue Hour', 'artist': 'TXT', 'youtube': 'https://youtu.be/Vd9QkWsd5p4', 'image': 'https://i.ytimg.com/vi/Vd9QkWsd5p4/hqdefault.jpg'},
    {'mood': '추억에 잠기고 싶을 때', 'genre': '인디팝', 'title': 'Red Flavor', 'artist': 'Red Velvet', 'youtube': 'https://youtu.be/WyiIGEHQP8o', 'image': 'https://i.ytimg.com/vi/WyiIGEHQP8o/hqdefault.jpg'},
    {'mood': '추억에 잠기고 싶을 때', 'genre': '발라드', 'title': 'Love Dive', 'artist': 'IVE', 'youtube': 'https://youtu.be/Y8JFxS1HlDo', 'image': 'https://i.ytimg.com/vi/Y8JFxS1HlDo/hqdefault.jpg'},
    {'mood': '추억에 잠기고 싶을 때', 'genre': '록', 'title': 'Love Shot', 'artist': 'EXO', 'youtube': 'https://youtu.be/pSudEWBAYRE', 'image': 'https://i.ytimg.com/vi/pSudEWBAYRE/hqdefault.jpg'},
    {'mood': '추억에 잠기고 싶을 때', 'genre': '힙합', 'title': 'Blue Hour', 'artist': 'TXT', 'youtube': 'https://youtu.be/Vd9QkWsd5p4', 'image': 'https://i.ytimg.com/vi/Vd9QkWsd5p4/hqdefault.jpg'},
    {'mood': '추억에 잠기고 싶을 때', 'genre': 'R&B', 'title': 'Cupid', 'artist': 'FIFTY FIFTY', 'youtube': 'https://youtu.be/6uvUTz0uP3k', 'image': 'https://i.ytimg.com/vi/6uvUTz0uP3k/hqdefault.jpg'},
    {'mood': '추억에 잠기고 싶을 때', 'genre': 'EDM', 'title': 'Cupid', 'artist': 'FIFTY FIFTY', 'youtube': 'https://youtu.be/6uvUTz0uP3k', 'image': 'https://i.ytimg.com/vi/6uvUTz0uP3k/hqdefault.jpg'},
    {'mood': '추억에 잠기고 싶을 때', 'genre': '시티팝', 'title': 'Red Flavor', 'artist': 'Red Velvet', 'youtube': 'https://youtu.be/WyiIGEHQP8o', 'image': 'https://i.ytimg.com/vi/WyiIGEHQP8o/hqdefault.jpg'},
    {'mood': '추억에 잠기고 싶을 때', 'genre': '어쿠스틱', 'title': 'Feel Special', 'artist': 'TWICE', 'youtube': 'https://youtu.be/3ymwOvzhwHs', 'image': 'https://i.ytimg.com/vi/3ymwOvzhwHs/hqdefault.jpg'},
    {'mood': '추억에 잠기고 싶을 때', 'genre': '라틴팝', 'title': 'Spring Day', 'artist': 'BTS', 'youtube': 'https://youtu.be/xEeFrLSkMm8', 'image': 'https://i.ytimg.com/vi/xEeFrLSkMm8/hqdefault.jpg'},
    {'mood': '추억에 잠기고 싶을 때', 'genre': '팝', 'title': 'Cupid', 'artist': 'FIFTY FIFTY', 'youtube': 'https://youtu.be/6uvUTz0uP3k', 'image': 'https://i.ytimg.com/vi/6uvUTz0uP3k/hqdefault.jpg'},
] 

# ... 이어지는 전체 곡 리스트는 필요에 따라 계속 추가 가능
]
