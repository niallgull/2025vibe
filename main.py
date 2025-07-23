import streamlit as st
import random
from streamlit_option_menu import option_menu

# -------------------------------
# 🎵 데이터셋
# -------------------------------
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

# -------------------------------
# 🎨 페이지 스타일 설정
# -------------------------------
st.set_page_config(page_title="K-POP 노래 추천기", page_icon="🎧", layout="centered")

st.markdown(
    """
    <style>
    .stApp {
        background-color: #fff7f9;
        font-family: 'Pretendard', sans-serif;
    }
    .recommend-box {
        padding: 10px;
        background-color: #ffffff;
        border-radius: 10px;
        box-shadow: 0px 2px 10px rgba(0,0,0,0.05);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -------------------------------
# 📂 메뉴 구성
# -------------------------------
selected = option_menu(
    menu_title=None,
    options=["🎧 추천받기", "🎲 랜덤추천", "ℹ️ 정보"],
    icons=["music-note-beamed", "dice-5", "info-circle"],
    orientation="horizontal"
)

# -------------------------------
# 📌 추천받기 페이지
# -------------------------------
if selected == "🎧 추천받기":
    st.title("🎧 K-POP 아이돌 노래 추천기")
    st.write("기분과 장르를 선택하면 어울리는 K-POP 노래를 추천해줄게요!")

    mood_options = sorted(set(song["mood"] for song in songs))
    genre_options = sorted(set(song["genre"] for song in songs))

    selected_mood = st.selectbox("기분을 골라주세요 😊", mood_options)
    selected_genre = st.selectbox("장르를 골라주세요 🎵", genre_options)

    if st.button("🎵 노래 추천받기"):
        results = [s for s in songs if s["mood"] == selected_mood and s["genre"] == selected_genre]
        if results:
            st.success("✨ 아래 노래를 추천해요!")
            for song in results:
                with st.container():
                    st.image(song["image_url"], width=300, caption=f"{song['title']} - {song['artist']}")
                    st.markdown(f"[🔗 유튜브에서 보기]({song['youtube_url']})", unsafe_allow_html=True)
                    st.markdown("---")
        else:
            st.warning("조건에 맞는 노래가 없어요 😢")

# -------------------------------
# 🎲 랜덤 추천 페이지
# -------------------------------
elif selected == "🎲 랜덤추천":
    st.title("🎲 랜덤 K-POP 추천")
    if st.button("✨ 랜덤으로 추천해줘!"):
        song = random.choice(songs)
        st.balloons()
        st.image(song["image_url"], width=300, caption=f"{song['title']} - {song['artist']}")
        st.markdown(f"**🎶 {song['title']}** by *{song['artist']}*")
        st.markdown(f"[🔗 유튜브에서 보기]({song['youtube_url']})", unsafe_allow_html=True)

# -------------------------------
# ℹ️ 정보 페이지
# -------------------------------
elif selected == "ℹ️ 정보":
    st.title("ℹ️ 앱 정보")
    st.markdown("""
    - 만든 사람: 당신 😎  
    - 사용 기술: Python + Streamlit  
    - 기능: K-POP 노래 추천, 랜덤 추천, 유튜브 연결  
    - 다음에 만들 기능: 입덕 테스트, 팬픽 연동, 댓글 모음 등등!

    궁금한 점은 GPT에게 물어보세요 💬
    """)

