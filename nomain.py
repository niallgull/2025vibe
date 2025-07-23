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

# ✅ 전체 노래 리스트 (일부 생략 가능)
songs = [
    # 🎵 예시: 기존 곡들 + 너가 추가한 아티스트들 포함
    {
        "title": "Youth",
        "artist": "TOURS (투어스)",
        "mood": "추억에 잠기고 싶을 때",
        "genre": "어쿠스틱",
        "youtube": "https://www.youtube.com/watch?v=VKjG5n0Q2rU",
        "image": "https://i.ytimg.com/vi/VKjG5n0Q2rU/hqdefault.jpg"
    },
    {
        "title": "Dive",
        "artist": "TOURS (투어스)",
        "mood": "힐링",
        "genre": "인디팝",
        "youtube": "https://www.youtube.com/watch?v=25VmR3cSPv4",
        "image": "https://i.ytimg.com/vi/25VmR3cSPv4/hqdefault.jpg"
    },
    {
        "title": "Runaway",
        "artist": "TOURS (투어스)",
        "mood": "우울함",
        "genre": "R&B",
        "youtube": "https://www.youtube.com/watch?v=ZBpne6SL1Xg",
        "image": "https://i.ytimg.com/vi/ZBpne6SL1Xg/hqdefault.jpg"
    },
    {
        "title": "REALLY REALLY",
        "artist": "WINNER",
        "mood": "기분전환",
        "genre": "시티팝",
        "youtube": "https://www.youtube.com/watch?v=4tBnF46ybZk",
        "image": "https://i.ytimg.com/vi/4tBnF46ybZk/hqdefault.jpg"
    },
    {
        "title": "ISLAND",
        "artist": "WINNER",
        "mood": "기분전환",
        "genre": "EDM",
        "youtube": "https://www.youtube.com/watch?v=AV5vZpJ_HV8",
        "image": "https://i.ytimg.com/vi/AV5vZpJ_HV8/hqdefault.jpg"
    },
    {
        "title": "MILLIONS",
        "artist": "WINNER",
        "mood": "설렘",
        "genre": "팝",
        "youtube": "https://www.youtube.com/watch?v=nQ6wLuYvGd4",
        "image": "https://i.ytimg.com/vi/nQ6wLuYvGd4/hqdefault.jpg"
    },
    # 🎵 이전에 넣은 곡들도 여기에 같이 포함하면 돼요!
    # 🎵 생략: BTS, ILLIT, IVE, NewJeans, EXO, FIFTY FIFTY 등
]

# ✅ 고정된 기분/장르 선택지
moods = [
    "설렘", "쓸쓸함", "자신감", "기분전환", "우울함", "신남",
    "힐링", "위로받고 싶음", "비 오는 날", "친구들과 함께", "추억에 잠기고 싶을 때"
]
genres = [
    "댄스", "인디팝", "발라드", "록", "힙합", "R&B",
    "EDM", "시티팝", "어쿠스틱", "라틴팝", "팝"
]

# ✅ UI
st.title("🎧 K-POP 아이돌 노래 추천기")

selected_mood = st.selectbox("기분을 골라주세요", moods)
selected_genre = st.selectbox("장르를 골라주세요", genres)

if st.button("🔍 추천받기"):
    filtered = [s for s in songs if s["mood"] == selected_mood and s["genre"] == selected_genre]
    if filtered:
        song = random.choice(filtered)
    else:
        song = random.choice(songs)
        st.info("조건에 맞는 곡이 없어 랜덤으로 추천할게요! 💡")

    st.success("✨ 추천 노래 ✨")
    st.image(song["image"], width=300, caption=f"{song['title']} - {song['artist']}")
    st.markdown(f"[유튜브에서 보기 🎬]({song['youtube']})", unsafe_allow_html=True)

st.markdown("## 🎲 아무거나 추천받기")
if st.button("🎲 아무거나 추천해줘!"):
    s = random.choice(songs)
    st.balloons()
    st.image(s["image"], width=300, caption=f"{s['title']} - {s['artist']}")
    st.markdown(f"**🎶 {s['title']}** by *{s['artist']}*")
    st.markdown(f"[유튜브에서 보기 🎬]({s['youtube']})", unsafe_allow_html=True)

