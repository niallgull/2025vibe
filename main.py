import streamlit as st
import random

# 💡 귀엽고 둥근 느낌의 구글 웹폰트 사용 (나눔스퀘어라운드 대체 느낌)
FONT_URL = "https://fonts.googleapis.com/css2?family=Jua&display=swap"

# 📌 스타일 커스텀 추가
st.markdown(
    f"""
    <style>
    @import url('{FONT_URL}');

    html, body, [class*="css"] {{
        font-family: 'Jua', sans-serif;
    }}

    .center-text {{
        text-align: center;
        margin-top: 30px;
        font-size: 48px;
        color: #333333;
        text-shadow: 1px 1px 2px #cccccc;
    }}

    .highlight {{
        color: #1E90FF;
        font-weight: bold;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# 🍱 메뉴 목록
menus = {
    "한식": ["🍚 비빔밥", "🥩 불고기", "🥣 김치찌개", "🥬 된장찌개", "🌶️ 제육볶음", "🥓 삼겹살", "❄️ 냉면", "🍜 칼국수"],
    "중식": ["🍜 짜장면", "🌶️ 짬뽕", "🍖 탕수육", "🌶️ 마라탕", "🍗 깐풍기", "🥗 양장피", "🍤 유산슬", "🍳 볶음밥"],
    "일식": ["🍣 초밥", "🍲 우동", "🥩 규동", "🐽 돈까스", "🍜 라멘", "🍱 가츠동", "🦐 텐동", "🥞 오코노미야끼"],
    "양식": ["🍝 파스타", "🥩 스테이크", "🍔 햄버거", "🍕 피자", "🧀 그라탱", "🥄 리조또", "🥗 샐러드", "🍗 치킨"]
}

# 🎀 앱 제목
st.title("🍽️ 오늘의 점심 메뉴 추천기")

st.markdown("한식, 중식, 일식, 양식 중에서 하나를 골라봐요! 메뉴를 귀엽게 추천해드릴게요 ✨")

# 선택
category = st.selectbox("👉 먹고 싶은 음식 종류를 골라주세요!", list(menus.keys()))

# 추천 버튼
if st.button("🎁 메뉴 추천 받기"):
    menu = random.choice(menus[category])

    st.markdown(
        f"""
        <div class="center-text">
            ✨ 오늘의 추천 메뉴는 <span class="highlight">{menu}</span> 입니다!
        </div>
        """,
        unsafe_allow_html=True
    )
