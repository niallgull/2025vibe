import streamlit as st
import json

# Load song data
def load_songs():
    with open("data/songs.json", "r", encoding="utf-8") as f:
        return json.load(f)

# 추천 필터링 함수
def recommend_songs(mood, genre, songs):
    return [s for s in songs if s["mood"] == mood and s["genre"] == genre]

# 앱 제목
st.title("🎧 K-POP 아이돌 노래 추천기")
st.write("기분과 장르를 선택하면 어울리는 K-POP 노래를 추천해줄게요!")

# 데이터 불러오기
songs = load_songs()

# 유니크 mood/genre 목록 추출
moods = sorted(set(song["mood"] for song in songs))
genres = sorted(set(song["genre"] for song in songs))

# 사용자 입력
selected_mood = st.selectbox("기분을 골라주세요 😊", moods)
selected_genre = st.selectbox("장르를 골라주세요 🎵", genres)

# 추천 결과
if st.button("노래 추천받기"):
    results = recommend_songs(selected_mood, selected_genre, songs)
    if results:
        st.success("이런 노래들을 추천해요!")
        for song in results:
            st.write(f"**🎶 {song['title']}** - *{song['artist']}*")
    else:
        st.warning("해당 조건에 맞는 노래가 없어요. 조건을 바꿔보세요!")
