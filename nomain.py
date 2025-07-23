import streamlit as st
import random

# ✅ 귀엽고 모던한 폰트 적용
st.markdown("""
    <style>
    @import url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2104@1.0/NanumSquareRound.css');
    html, body, [class*="css"] {
        font-family: 'NanumSquareRound', sans-serif !important;
    }
    </style>
""", unsafe_allow_html=True)

# ✅ K-POP 추천 데이터 (일부만 보여줄게)
songs = [
    {
        "title": "Magnetic",
        "artist": "ILLIT",
        "mood": "설렘",
        "genre": "댄스",
        "youtube": "https://www.youtube.com/watch?v=Vk5-c_v4gMU",
        "image": "https://i.ytimg.com/vi/Vk5-c_v4gMU/hqdefault.jpg"
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
        "title": "Love Dive",
        "artist": "IVE",
        "mood": "기분전환",
        "genre": "EDM",
        "youtube": "https://www.youtube.com/watch?v=Y8JFxS1HlDo",
        "image": "https://i.ytimg.com/vi/Y8JFxS1HlDo/hqdefault.jpg"
    },
    {
        "title": "Eight",
        "artist": "IU",
        "mood": "추억에 잠기고 싶을 때",
        "genre": "어쿠스틱",
        "youtube": "https://www.youtube.com/watch?v=TgOu00Mf3kI",
        "image": "https://i.ytimg.com/vi/TgOu00Mf3kI/hqdefault.jpg"
    }
]

# ✅ 전체 선택지 고정 추가
moods = [
    "설렘", "쓸쓸함", "자신감", "기분전환", "우울함", "신남",
    "힐링", "위로받고 싶음", "비 오는 날", "친구들과 함께", "추억에 잠기고 싶을 때"
]
genres = [
    "댄스", "인디팝", "발라드", "록", "힙합", "R&B",
    "EDM", "시티팝", "어쿠스틱", "라틴팝"
]

# ✅ UI
st.title("🎧 K-POP 아이돌 노래 추천기")

selected_mood = st.selectbox("기분을 골라주세요", moods)
selected_genre = st.selectbox("장르를 골라주세요", genres)

if st.button("🔍 추천받기"):
    results = [s for s in songs if s["mood"] == selected_mood and s["genre"] == selected_genre]
    if results:
        st.success(f"🎵 '{selected_mood}' 기분에 어울리는 '{selected_genre}' 장르 노래!")
        for s in results:
            st.image(s["image"], width=300, caption=f"{s['title']} - {s['artist']}")
            st.markdown(f"[유튜브에서 보기 🎬]({s['youtube']})", unsafe_allow_html=True)
            st.markdown("---")
    else:
        st.warning("해당 조건에 맞는 노래가 없어요 😢")

st.markdown("## 🎲 랜덤으로 추천받기")
if st.button("🎲 아무거나 추천해줘!"):
    s = random.choice(songs)
    st.balloons()
    st.image(s["image"], width=300, caption=f"{s['title']} - {s['artist']}")
    st.markdown(f"**🎶 {s['title']}** by *{s['artist']}*")
    st.markdown(f"[유튜브에서 보기 🎬]({s['youtube']})", unsafe_allow_html=True)
