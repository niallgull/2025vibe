import streamlit as st
import random

# ✅ 귀엽고 모던한 폰트 적용 (NanumSquareRound)
st.markdown("""
    <style>
    @import url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2104@1.0/NanumSquareRound.css');
    html, body, [class*="css"] {
        font-family: 'NanumSquareRound', sans-serif !important;
    }
    </style>
""", unsafe_allow_html=True)

# ✅ 샘플 데이터
songs = [
    {
        "title": "Magnetic",
        "artist": "ILLIT",
        "mood": "설렘",
        "genre": "댄스",
        "youtube": "https://www.youtube.com/watch?v=6eOmygLzLZ0",
        "image": "https://i.ytimg.com/vi/6eOmygLzLZ0/hqdefault.jpg"
    },
    {
        "title": "Ditto",
        "artist": "NewJeans",
        "mood": "쓸쓸함",
        "genre": "인디팝",
        "youtube": "https://www.youtube.com/watch?v=pSUydWEqKwE",
        "image": "https://i.ytimg.com/vi/pSUydWEqKwE/hqdefault.jpg"
    },
    {
        "title": "UNFORGIVEN",
        "artist": "LE SSERAFIM",
        "mood": "자신감",
        "genre": "댄스",
        "youtube": "https://www.youtube.com/watch?v=UBURTj20HXI",
        "image": "https://i.ytimg.com/vi/UBURTj20HXI/hqdefault.jpg"
    },
    {
        "title": "Love Dive",
        "artist": "IVE",
        "mood": "설렘",
        "genre": "댄스",
        "youtube": "https://www.youtube.com/watch?v=Y8JFxS1HlDo",
        "image": "https://i.ytimg.com/vi/Y8JFxS1HlDo/hqdefault.jpg"
    }
]

st.title("🎧 K-POP 노래 추천기")

# ✅ 기본 추천
moods = sorted(set(s["mood"] for s in songs))
genres = sorted(set(s["genre"] for s in songs))

selected_mood = st.selectbox("기분을 골라주세요", moods)
selected_genre = st.selectbox("장르를 골라주세요", genres)

if st.button("🔍 추천받기"):
    results = [s for s in songs if s["mood"] == selected_mood and s["genre"] == selected_genre]
    if results:
        for song in results:
            st.image(song["image"], width=300, caption=f"{song['title']} - {song['artist']}")
            st.markdown(f"[유튜브에서 보기 🎬]({song['youtube']})", unsafe_allow_html=True)
            st.markdown("---")
    else:
        st.warning("조건에 맞는 노래가 없어요 😢")

# ✅ 랜덤 추천
st.markdown("## 또는 🎲 랜덤으로 추천받기")
if st.button("🎲 아무 노래나 추천해줘!"):
    random_song = random.choice(songs)
    st.success("랜덤 추천이에요!")
    st.image(random_song["image"], width=300, caption=f"{random_song['title']} - {random_song['artist']}")
    st.markdown(f"[유튜브에서 보기 🎬]({random_song['youtube']})", unsafe_allow_html=True)
