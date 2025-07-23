import streamlit as st
import random

# ✅ 폰트 적용
st.markdown("""
    <style>
    @import url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2104@1.0/NanumSquareRound.css');
    html, body, [class*="css"] {
        font-family: 'NanumSquareRound', sans-serif !important;
    }
    </style>
""", unsafe_allow_html=True)

# ✅ 곡 데이터
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
    },
    {
        "title": "134340",
        "artist": "BTS (방탄소년단)",
        "mood": "쓸쓸함",
        "genre": "어쿠스틱",
        "youtube": "https://www.youtube.com/watch?v=U8H-5cZ6zv8",
        "image": "https://i.ytimg.com/vi/U8H-5cZ6zv8/hqdefault.jpg"
    },
    {
        "title": "슈퍼소닉 (Super Sonic)",
        "artist": "fromis_9",
        "mood": "신남",
        "genre": "EDM",
        "youtube": "https://www.youtube.com/watch?v=Kj2XN0qZ-GQ",
        "image": "https://i.ytimg.com/vi/Kj2XN0qZ-GQ/hqdefault.jpg"
    },
    {
        "title": "빌려온 고양이",
        "artist": "ILLIT",
        "mood": "힐링",
        "genre": "시티팝",
        "youtube": "https://www.youtube.com/watch?v=0aZr9VA93zY",
        "image": "https://i.ytimg.com/vi/0aZr9VA93zY/hqdefault.jpg"
    },
    {
        "title": "I AM",
        "artist": "IVE",
        "mood": "자신감",
        "genre": "댄스",
        "youtube": "https://www.youtube.com/watch?v=6ZUIwj3FgUY",
        "image": "https://i.ytimg.com/vi/6ZUIwj3FgUY/hqdefault.jpg"
    },
    {
        "title": "Polaroid Love",
        "artist": "ENHYPEN",
        "mood": "설렘",
        "genre": "인디팝",
        "youtube": "https://www.youtube.com/watch?v=HGt-I6_hDk4",
        "image": "https://i.ytimg.com/vi/HGt-I6_hDk4/hqdefault.jpg"
    },
    {
        "title": "PANORAMA",
        "artist": "iKON",
        "mood": "기분전환",
        "genre": "록",
        "youtube": "https://www.youtube.com/watch?v=3KoKE9nCGBY",
        "image": "https://i.ytimg.com/vi/3KoKE9nCGBY/hqdefault.jpg"
    },
    {
        "title": "사랑을 했다",
        "artist": "iKON",
        "mood": "추억에 잠기고 싶을 때",
        "genre": "발라드",
        "youtube": "https://www.youtube.com/watch?v=vecSVX1QYbQ",
        "image": "https://i.ytimg.com/vi/vecSVX1QYbQ/hqdefault.jpg"
    }
]

# ✅ 선택지
moods = [
    "설렘", "쓸쓸함", "자신감", "기분전환", "우울함", "신남",
    "힐링", "위로받고 싶음", "비 오는 날", "친구들과 함께", "추억에 잠기고 싶을 때"
]
genres = [
    "댄스", "인디팝", "발라드", "록", "힙합", "R&B",
    "EDM", "시티팝", "어쿠스틱", "라틴팝"
]

# ✅ 앱 제목
st.title("🎧 K-POP 아이돌 노래 추천기")

selected_mood = st.selectbox("기분을 골라주세요", moods)
selected_genre = st.selectbox("장르를 골라주세요", genres)

# ✅ 조건 기반 추천 (랜덤 1곡)
if st.button("🔍 추천받기"):
    filtered = [s for s in songs if s["mood"] == selected_mood and s["genre"] == selected_genre]
    if filtered:
        song = random.choice(filtered)
    else:
        song = random.choice(songs)
        st.info("해당 조건에 맞는 곡이 없어 랜덤으로 추천해드릴게요! 💡")

    st.success("추천 노래 🎶")
    st.image(song["image"], width=300, caption=f"{song['title']} - {song['artist']}")
    st.markdown(f"[유튜브에서 보기 🎬]({song['youtube']})", unsafe_allow_html=True)

# ✅ 아무 노래 추천
st.markdown("## 🎲 아무거나 추천받기")
if st.button("🎲 아무거나 추천해줘!"):
    s = random.choice(songs)
    st.balloons()
    st.image(s["image"], width=300, caption=f"{s['title']} - {s['artist']}")
    st.markdown(f"**🎶 {s['title']}** by *{s['artist']}*")
    st.markdown(f"[유튜브에서 보기 🎬]({s['youtube']})", unsafe_allow_html=True)
