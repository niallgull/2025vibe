import streamlit as st

# --- 확장된 K-POP 추천 데이터 ---
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

# --- Streamlit UI ---
st.set_page_config(page_title="K-POP 추천기", page_icon="🎧")

st.title("🎧 K-POP 아이돌 노래 추천기")
st.write("기분과 장르를 골라서 당신에게 어울리는 K-POP 노래를 추천해줄게요!")

# 선택 옵션 만들기
mood_options = sorted(set(song["mood"] for song in songs))
genre_options = sorted(set(song["genre"] for song in songs))

selected_mood = st.selectbox("기분을 골라주세요 😊", mood_options)
selected_genre = st.selectbox("장르를 골라주세요 🎵", genre_options)

# 추천 버튼
if st.button("노래 추천받기"):
    results = [s for s in songs if s["mood"] == selected_mood and s["genre"] == selected_genre]
    if results:
        st.success(f"'{selected_mood}' 기분에 어울리는 '{selected_genre}' 장르 노래를 추천해요!")
        for song in results:
            st.image(song["image_url"], width=300, caption=f"{song['title']} - {song['artist']}")
            st.markdown(f"[🔗 유튜브에서 보기]({song['youtube_url']})", unsafe_allow_html=True)
            st.markdown("---")
    else:
        st.warning("앗! 해당 조건에 맞는 노래가 없어요. 조건을 바꿔보세요 😢")


