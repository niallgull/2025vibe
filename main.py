import streamlit as st
import random
from streamlit_option_menu import option_menu

songs = [
    {
        "title": "Magnetic",
        "artist": "ILLIT",
        "mood": "설렘",
        "genre": "댄스",
        "youtube_url": "https://www.youtube.com/watch?v=6eOmygLzLZ0",
        "image_url": "https://i.ytimg.com/vi/6eOmygLzLZ0/hqdefault.jpg"
    },
    {
        "title": "Ditto",
        "artist": "NewJeans",
        "mood": "쓸쓸함",
        "genre": "인디팝",
        "youtube_url": "https://www.youtube.com/watch?v=pSUydWEqKwE",
        "image_url": "https://i.ytimg.com/vi/pSUydWEqKwE/hqdefault.jpg"
    },
    {
        "title": "UNFORGIVEN",
        "artist": "LE SSERAFIM",
        "mood": "자신감",
        "genre": "댄스",
        "youtube_url": "https://www.youtube.com/watch?v=UBURTj20HXI",
        "image_url": "https://i.ytimg.com/vi/UBURTj20HXI/hqdefault.jpg"
    },
    {
        "title": "Love Dive",
        "artist": "IVE",
        "mood": "설렘",
        "genre": "댄스",
        "youtube_url": "https://www.youtube.com/watch?v=Y8JFxS1HlDo",
        "image_url": "https://i.ytimg.com/vi/Y8JFxS1HlDo/hqdefault.jpg"
    }
]

st.set_page_config(page_title="K-POP 추천기", page_icon="🎧", layout="centered")
st.markdown("""
    <style>
    .stApp { background-color: #fff5f8; font-family: 'Arial', sans-serif; }
    .stButton>button {
        background-color: #ff85a2; color: white; border-radius: 8px;
        height: 3em; width: 100%; border: none; font-size: 16px;
    }
    .stButton>button:hover { background-color: #ff678e; transition: 0.3s; }
    </style>
""", unsafe_allow_html=True)

selected = option_menu(
    menu_title=None,
    options=["🎧 추천받기", "🎲 랜덤추천", "ℹ️ 정보"],
    icons=["music-note-beamed", "dice-5", "info-circle"],
    orientation="horizontal"
)

if selected == "🎧 추천받기":
    st.title("🎧 K-POP 아이돌 노래 추천기")
    st.write("기분/장르 골라서 어울리는 곡 추천해드려요!")
    mood_options = sorted(set(s["mood"] for s in songs))
    genre_options = sorted(set(s["genre"] for s in songs))
    sel_mood = st.selectbox("기분을 골라주세요 😊", mood_options)
    sel_genre = st.selectbox("장르를 골라주세요 🎵", genre_options)
    if st.button("🎵 추천받기"):
        res = [s for s in songs if s["mood"]==sel_mood and s["genre"]==sel_genre]
        if res:
            st.success(f"'{sel_mood}' 기분엔 '{sel_genre}' 장르 추천!")
            for s in res:
                st.image(s["image_url"], width=300, caption=f"{s['title']} - {s['artist']}")
                st.markdown(f"[🔗 유튜브에서 보기]({s['youtube_url']})", unsafe_allow_html=True)
                st.markdown("---")
        else:
            st.warning("아직 데이터가 없어요 😢")

elif selected == "🎲 랜덤추천":
    st.title("🎲 랜덤 추천")
    if st.button("✨ 아무거나!"):
        s = random.choice(songs)
        st.balloons()
        st.image(s["image_url"], width=300, caption=f"{s['title']} - {s['artist']}")
        st.markdown(f"**🎶 {s['title']}** by *{s['artist']}*")
        st.markdown(f"[🔗 유튜브]( {s['youtube_url']})", unsafe_allow_html=True)

elif selected == "ℹ️ 정보":
    st.title("ℹ️ 앱 정보")
    st.markdown("""
    - 만든 사람: 너 💖  
    - 기능: 기분/장르 추천, 랜덤 추천, 유튜브 연결  
    - 기술: Streamlit, streamlit-option-menu  
    - 다음 목표:
      - 입덕 테스트, 유저 추가 데이터 등!
    """)
