import streamlit as st

# --- 샘플 K-POP 데이터 (앱 내에 직접 작성) ---
songs = [
    {"title": "Magnetic", "artist": "ILLIT", "mood": "설렘", "genre": "댄스"},
    {"title": "Ditto", "artist": "NewJeans", "mood": "쓸쓸함", "genre": "인디팝"},
    {"title": "UNFORGIVEN", "artist": "LE SSERAFIM", "mood": "자신감", "genre": "댄스"},
    {"title": "Love Dive", "artist": "IVE", "mood": "설렘", "genre": "댄스"},
    {"title": "Event Horizon", "artist": "YOUNHA", "mood": "감성", "genre": "록"},
    {"title": "Antifragile", "artist": "LE SSERAFIM", "mood": "자신감", "genre": "라틴팝"}
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
            st.markdown(f"- **🎶 {song['title']}** by *{song['artist']}*")
    else:
        st.warning("앗! 해당 조건에 맞는 노래가 없어요. 조건을 바꿔보세요 😢")

