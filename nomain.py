import streamlit as st
import random
from songs_list import songs  # songs_list.py 파일에서 songs 리스트 불러오기

# 앱 기본 설정
st.set_page_config(page_title="K-POP 추천기", layout="wide")
st.markdown("<h1 style='text-align:center; color:#5D3A00;'>K-POP 노래 추천기 🎵</h1>", unsafe_allow_html=True)

# 세션 상태 초기화
if "history" not in st.session_state:
    st.session_state.history = []
if "used_indexes" not in st.session_state:
    st.session_state.used_indexes = set()

# 분위기 & 장르 선택
col1, col2 = st.columns(2)
with col1:
    selected_mood = st.selectbox("기분을 골라보세요 🎭", sorted(set(song["mood"] for song in songs)))
with col2:
    selected_genre = st.selectbox("듣고 싶은 장르를 골라보세요 🎶", sorted(set(song["genre"] for song in songs)))

# 노래 추천 로직
def recommend_song():
    filtered = [i for i, song in enumerate(songs) if song["mood"] == selected_mood and song["genre"] == selected_genre]
    candidates = [i for i in filtered if i not in st.session_state.used_indexes]
    if not candidates:
        st.session_state.used_indexes.clear()  # 다 나왔으면 초기화
        candidates = filtered
    if candidates:
        index = random.choice(candidates)
        st.session_state.used_indexes.add(index)
        return songs[index]
    return None

# 추천 버튼
if st.button("🎲 아무거나 추천해줘!"):
    result = recommend_song()
    if result:
        st.session_state.history.append(result)
        st.image(result["image"], width=300)
        st.markdown(f"### 🎧 {result['title']} - {result['artist']}")
        st.markdown(f"[🔗 유튜브에서 보기]({result['youtube']})")
    else:
        st.warning("조건에 맞는 노래가 없어요!")

# 추천 기록
st.markdown("---")
st.markdown("### 📜 지금까지 추천받은 노래")
if st.session_state.history:
    for h in st.session_state.history[::-1]:
        st.markdown(f"- **{h['title']}** - {h['artist']}")
else:
    st.write("추천받은 노래가 아직 없어요.")

# 초기화 버튼
if st.button("초기화 🔄"):
    st.session_state.history.clear()
    st.session_state.used_indexes.clear()
    st.experimental_rerun()
