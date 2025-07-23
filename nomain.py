# ✅ 필요한 라이브러리 임포트
import streamlit as st
import random

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
st.markdown('<h1 class="title-animated">🎧 K-POP 아이돌 노래 추천기</h1>', unsafe_allow_html=True)

# ✅ 기분과 장르 선택
moods = ["설렘", "쓸쓸함", "자신감", "기분전환", "우울함", "신남", "힐링", "위로받고 싶음", "비 오는 날", "친구들과 함께", "추억에 잠기고 싶을 때"]
genres = ["댄스", "인디팝", "발라드", "록", "힙합", "R&B", "EDM", "시티팝", "어쿠스틱", "라틴팝", "팝"]

selected_mood = st.selectbox("기분을 골라주세요", moods)
selected_genre = st.selectbox("장르를 골라주세요", genres)

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

# ✅ 조건 기반 추천
if st.button("🔍 추천받기"):
    filtered = [s for s in songs if s["mood"] == selected_mood and s["genre"] == selected_genre]
    if filtered:
        song = random.choice(filtered)
        st.session_state.history.append(song)
        st.success("✨ 추천 노래 ✨")
        st.image(song["image"], width=300, caption=f"{song['title']} - {song['artist']}")
        st.markdown(f"[유튜브에서 보기 🎬]({song['youtube']})", unsafe_allow_html=True)
    else:
        st.warning("해당 조건에 맞는 곡이 없어요. 😢")

# ✅ 아무거나 추천하기
st.markdown("## 🎲 아무거나 추천받기")
if st.button("🎲 아무거나 추천해줘!"):
    remaining = [s for s in songs if s not in st.session_state.history]
    if not remaining:
        st.warning("모든 곡을 추천했어요! 기록을 초기화할게요.")
        st.session_state.history = []
        remaining = songs[:]
    s = random.choice(remaining)
    st.session_state.history.append(s)
    st.toast("✨ 새로운 노래를 추천할게요!", icon="🎧")
    st.image(s["image"], width=300, caption=f"{s['title']} - {s['artist']}")
    st.markdown(f"**🎶 {s['title']}** by *{s['artist']}*")
    st.markdown(f"[유튜브에서 보기 🎬]({s['youtube']})", unsafe_allow_html=True)

# ✅ 기록 초기화 버튼과 함께 추천 내역 보여주기
col1, col2 = st.columns([1, 5])
with col1:
    if st.button("🧹 기록 초기화"):
        st.session_state.history = []
        st.success("추천 기록이 초기화되었어요!")

with col2:
    st.markdown("### 📜 지금까지 추천받은 노래")
    if st.session_state.history:
        for idx, h in enumerate(st.session_state.history[::-1], 1):
            st.markdown(f"{idx}. **{h['title']}** by *{h['artist']}*")
    else:
        st.markdown("아직 추천받은 노래가 없어요!")

# ✅ 모든 곡 보기
with st.expander("📚 모든 추천 곡 목록 보기 (전체 121곡)"):
    for idx, s in enumerate(songs, 1):
        st.markdown(f"**{idx}. {s['title']}** by *{s['artist']}*")
        st.image(s["image"], width=200)
        st.markdown(f"[유튜브에서 보기 🎬]({s['youtube']})", unsafe_allow_html=True)
        st.markdown("---")

# 모든 가능한 조합
all_moods = ["설렘", "쓸쓸함", "자신감", "기분전환", "우울함", "신남", "힐링", "위로받고 싶음", "비 오는 날", "친구들과 함께", "추억에 잠기고 싶을 때"]
all_genres = ["댄스", "인디팝", "발라드", "록", "힙합", "R&B", "EDM", "시티팝", "어쿠스틱", "라틴팝", "팝"]

# 현재 존재하는 조합
existing_combinations = set((s['mood'], s['genre']) for s in songs)

# 빠진 조합 찾기
missing_combinations = []
for mood in all_moods:
    for genre in all_genres:
        if (mood, genre) not in existing_combinations:
            missing_combinations.append((mood, genre))

# 출력
st.markdown("### ❗ 빠진 기분 + 장르 조합")
if missing_combinations:
    for mood, genre in missing_combinations:
        st.markdown(f"- {mood} + {genre}")
    st.warning(f"총 {len(missing_combinations)}개의 조합이 누락되어 있어요.")
else:
    st.success("모든 기분 + 장르 조합이 완벽하게 채워져 있어요!")

