import streamlit as st
import random

# ✅ 폰트 스타일 적용
st.markdown("""
    <style>
    @import url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2104@1.0/NanumSquareRound.css');
    html, body, [class*="css"] {
        font-family: 'NanumSquareRound', sans-serif !important;
    }
    </style>
""", unsafe_allow_html=True)

# ✅ 121개 조합에 맞춘 노래 리스트
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

moods = [
    "설렘", "쓸쓸함", "자신감", "기분전환", "우울함", "신남",
    "힐링", "위로받고 싶음", "비 오는 날", "친구들과 함께", "추억에 잠기고 싶을 때"
]

genres = [
    "댄스", "인디팝", "발라드", "록", "힙합", "R&B",
    "EDM", "시티팝", "어쿠스틱", "라틴팝", "팝"
]

st.title("🎵 K-POP 아이돌 노래 추천기")

# 추천 기록 저장용 세션 상태 초기화
if "history" not in st.session_state:
    st.session_state.history = []

selected_mood = st.selectbox("기분을 골래주세요", moods)
selected_genre = st.selectbox("장르를 골래주세요", genres)

if st.button("🔍 추천받기"):
    filtered = [s for s in songs if s["mood"] == selected_mood and s["genre"] == selected_genre]
    if filtered:
        song = random.choice(filtered)
        st.success("✨ 추천 노래 ✨")
        st.image(song["image"], width=300, caption=f"{song['title']} - {song['artist']}")
        st.markdown(f"[유튜브에서 보기 🎬]({song['youtube']})", unsafe_allow_html=True)
        st.session_state.history.append(song)
    else:
        st.warning("해당 조건에 맞는 곡이 없어요. 😢")

st.markdown("## 🎲 아무것이나 추천받기")
if st.button("🎲 아무것이나 추천해줘!"):
    s = random.choice(songs)
    st.balloons()
    st.image(s["image"], width=300, caption=f"{s['title']} - {s['artist']}")
    st.markdown(f"**🎶 {s['title']}** by *{s['artist']}*")
    st.markdown(f"[유튜브에서 보기 🎬]({s['youtube']})", unsafe_allow_html=True)
    st.session_state.history.append(s)

# 추천 기록 표시
st.markdown("---")
st.markdown("### 📜 지금까지 추천받은 노래")
if st.session_state.history:
    for idx, h in enumerate(st.session_state.history[::-1], 1):
        st.markdown(f"{idx}. **{h['title']}** by *{h['artist']}*")
else:
    st.markdown("아직 추천받은 노래가 없어요!")
