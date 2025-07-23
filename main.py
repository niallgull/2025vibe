import streamlit as st
import random

# 귀여운 폰트 & 스타일 적용
FONT_URL = "https://fonts.googleapis.com/css2?family=Jua&display=swap"
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
        color: #333;
        text-shadow: 1px 1px 2px #ccc;
    }}

    .highlight {{
        color: #1E90FF;
        font-weight: bold;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# 음식 분류별 메뉴
category_menus = {
    "한식": [
        "🍚 비빔밥", "🥩 불고기", "🥣 김치찌개", "🥬 된장찌개", "🌶️ 제육볶음", "🥓 삼겹살", "❄️ 냉면", "🍜 칼국수",
        "🍲 갈비탕", "🐔 삼계탕", "🥘 순두부찌개", "🍢 어묵탕", "🍗 닭갈비", "🍖 보쌈", "🍳 계란말이 정식"
    ],
    "중식": [
        "🍜 짜장면", "🌶️ 짬뽕", "🍖 탕수육", "🌶️ 마라탕", "🍗 깐풍기", "🥗 양장피", "🍤 유산슬", "🍳 볶음밥",
        "🥟 군만두", "🍲 마파두부", "🍢 훠궈", "🍚 중식덮밥"
    ],
    "일식": [
        "🍣 초밥", "🍲 우동", "🥩 규동", "🐽 돈까스", "🍜 라멘", "🍱 가츠동", "🦐 텐동", "🥞 오코노미야끼",
        "🍛 일본식 카레", "🍢 오뎅", "🍥 나베", "🍡 미소시루 정식"
    ],
    "양식": [
        "🍝 파스타", "🥩 스테이크", "🍔 햄버거", "🍕 피자", "🧀 그라탱", "🥄 리조또", "🥗 샐러드", "🍗 치킨",
        "🍞 파니니", "🥪 클럽 샌드위치", "🥣 수프와 바게트", "🍳 오믈렛", "🧈 에그베네딕트"
    ]
}

# 계절별 메뉴
seasonal_menus = {
    "봄": [
        "🥬 봄동겉절이", "🍲 달래된장국", "🥗 냉이무침", "🥚 계란비빔밥", "🍙 유부초밥"
    ],
    "여름": [
        "❄️ 냉면", "🥗 콩국수", "🍉 수박화채", "🍱 초밥", "🍜 비빔국수", "🥢 냉모밀", "🥒 오이냉국"
    ],
    "가을": [
        "🍂 버섯전골", "🍁 단호박죽", "🍲 고등어조림", "🥘 장어덮밥", "🍜 들깨칼국수", "🐟 꽁치구이"
    ],
    "겨울": [
        "🔥 갈비탕", "🍲 순대국", "🐔 삼계탕", "🍜 우동", "🍢 어묵탕", "🍲 부대찌개", "🥘 곰탕"
    ]
}

# 타이틀
st.title("🍽️ 오늘 뭐 먹지? 점심 메뉴 추천기")

st.markdown("아래에서 **방식**을 선택하고 메뉴를 추천받아보세요! 😊")

# 방식 선택
mode = st.radio("추천 방식 선택:", ["🍱 음식 종류로 추천", "🗓️ 계절별 추천"])

if mode == "🍱 음식 종류로 추천":
    category = st.selectbox("🍴 먹고 싶은 음식 종류를 골라주세요!", list(category_menus.keys()))
    if st.button("🎁 메뉴 추천 받기", key="category"):
        menu = random.choice(category_menus[category])
        st.markdown(
            f"""
            <div class="center-text">
                ✨ 오늘의 추천 메뉴는 <span class="highlight">{menu}</span>
            </div>
            """,
            unsafe_allow_html=True
        )

elif mode == "🗓️ 계절별 추천":
    season = st.selectbox("📅 지금은 어떤 계절인가요?", list(seasonal_menus.keys()))
    if st.button("🎁 메뉴 추천 받기", key="season"):
        menu = random.choice(seasonal_menus[season])
        st.markdown(
            f"""
            <div class="center-text">
                ✨ 오늘의 추천 메뉴는 <span class="highlight">{menu}</span>
            </div>
            """,
            unsafe_allow_html=True
        )

