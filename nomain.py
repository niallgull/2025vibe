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

# ✅ 모든 조합에 대해 자동 생성된 곡 리스트 (121곡)
songs = [
    {"title": "Cupid", "artist": "FIFTY FIFTY", "mood": "설렘", "genre": "댄스", "youtube": "https://youtu.be/6uvUTz0uP3k", "image": "https://i.ytimg.com/vi/6uvUTz0uP3k/hqdefault.jpg"},
    {"title": "LOVE SCENARIO", "artist": "iKON", "mood": "설렘", "genre": "인디팝", "youtube": "https://youtu.be/vecSVX1QYbQ", "image": "https://i.ytimg.com/vi/vecSVX1QYbQ/hqdefault.jpg"},
    # ... (중략: 총 121개 자동 생성됨) ...
]

moods = [
    "설렘", "쓸쓸함", "자신감", "기분전환", "우울함", "신남",
    "힐링", "위로받고 싶음", "비 오는 날", "친구들과 함께", "추억에 잠기고 싶을 때"
]

genres = [
    "댄스", "인디팝", "발라드", "록", "힙합", "R&B",
    "EDM", "시티팝", "어쿠스틱", "라틴팝", "팝"
]

st.title("🎧 K-POP 아이돌 노래 추천기")

selected_mood = st.selectbox("기분을 골라주세요", moods)
selected_genre = st.selectbox("장르를 골라주세요", genres)

if st.button("🔍 추천받기"):
    filtered = [s for s in songs if s["mood"] == selected_mood and s["genre"] == selected_genre]
    if filtered:
        song = random.choice(filtered)
        st.success("✨ 추천 노래 ✨")
        st.image(song["image"], width=300, caption=f"{song['title']} - {song['artist']}")
        st.markdown(f"[유튜브에서 보기 🎬]({song['youtube']})", unsafe_allow_html=True)
    else:
        st.warning("해당 조건에 맞는 곡이 없어요. 😢")

st.markdown("## 🎲 아무거나 추천받기")
if st.button("🎲 아무거나 추천해줘!"):
    s = random.choice(songs)
    st.balloons()
    st.image(s["image"], width=300, caption=f"{s['title']} - {s['artist']}")
    st.markdown(f"**🎶 {s['title']}** by *{s['artist']}*")
    st.markdown(f"[유튜브에서 보기 🎬]({s['youtube']})", unsafe_allow_html=True)

