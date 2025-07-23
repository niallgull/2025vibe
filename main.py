import streamlit as st

# 샘플 데이터
songs = [
    {
        "title": "Magnetic",
        "artist": "ILLIT",
        "mood": "설렘",
        "genre": "댄스",
    },
    {
        "title": "Ditto",
        "artist": "NewJeans",
        "mood": "쓸쓸함",
        "genre": "인디팝",
    },
    {
        "title": "UNFORGIVEN",
        "artist": "LE SSERAFIM",
        "mood": "자신감",
        "genre": "댄스",
    },
    {
        "title": "Love Dive",
        "artist": "IVE",
        "mood": "설렘",
        "genre": "댄스",
    }
]

# 앱 제목
st.title("🎧 K-POP 노래 추천기")

# 선택 박스
moods = sorted(set(song["mood"] for song in songs))
genres = sorted(set(song["genre"] for song in songs))

selected_mood = st.selectbox("기분을 골라주세요", moods)
selected_genre = st.selectbox("장르를 골라주세요", genres)

# 추천 버튼
if st.button("노래 추천받기"):
    results = [s for s in songs if s["mood"] == selected_mood and s["genre"] == selected_genre]
    if results:
        st.success("추천 결과:")
        for s in results:
            st.write(f"- 🎵 {s['title']} - {s['artist']}")
    else:
        st.warning("해당 조건에 맞는 노래가 없어요 😢")
st.markdown("""
    <style>
    @import url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2104@1.0/NanumSquareRound.css');

    html, body, [class*="css"] {
        font-family: 'NanumSquareRound', sans-serif !important;
    }
    </style>
""", unsafe_allow_html=True)

