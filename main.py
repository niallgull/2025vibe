import streamlit as st
import random

# 🍭 폰트 및 배경색 스타일
FONT_URL = "https://fonts.googleapis.com/css2?family=Jua&display=swap"
st.markdown(
    f"""
    <style>
    @import url('{FONT_URL}');

    html, body, [class*="css"] {{
        font-family: 'Jua', sans-serif;
        background-color: #FFF8DC;  /* 아이보리 배경 */
    }}

    .center-text {{
        text-align: center;
        margin-top: 30px;
        font-size: 42px;
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

# 🍱 음식 종류별 점심 메뉴
category_menus = {
    "한식": ["🍚 비빔밥", "🥩 불고기", "🥣 김치찌개", "🌶️ 제육볶음", "🥓 삼겹살", "🍜 칼국수", "🐔 삼계탕"],
    "중식": ["🍜 짜장면", "🌶️ 짬뽕", "🍖 탕수육", "🥟 군만두", "🍲 마파두부", "🍢 훠궈"],
    "일식": ["🍣 초밥", "🍲 우동", "🥩 규동", "🐽 돈까스", "🍜 라멘", "🍛 일본식 카레"],
    "양식": ["🍝 파스타", "🥩 스테이크", "🍔 햄버거", "🍕 피자", "🧀 그라탱", "🥗 샐러드"]
}

# 🍮 음식 종류별 디저트
category_desserts = {
    "한식": ["🍵 식혜", "🍯 꿀약과", "🧊 팥빙수", "🍠 군고구마", "🍡 인절미"],
    "중식": ["🍊 오렌지 젤리", "🥛 두유 푸딩", "🥭 망고 찹쌀떡", "🍘 중국 꽈배기"],
    "일식": ["🍵 말차 아이스크림", "🍮 푸딩", "🍡 다이후쿠", "🍘 단팥모나카"],
    "양식": ["🍰 티라미수", "🍮 크렘브륄레", "🍫 초코 케이크", "🍦 젤라또"]
}

# 🌤️ 계절별 메뉴
seasonal_menus = {
    "봄": ["🥬 봄동겉절이", "🍲 달래된장국", "🥗 냉이무침", "🥚 계란비빔밥"],
    "여름": ["❄️ 냉면", "🍉 수박화채", "🍜 비빔국수", "🥢 냉모밀"],
    "가을": ["🍂 버섯전골", "🍁 단호박죽", "🍲 고등어조림", "🥘 장어덮밥"],
    "겨울": ["🔥 갈비탕", "🍲 순대국", "🍜 우동", "🍢 어묵탕"]
}

# 🍨 계절별 디저트
seasonal_desserts = {
    "봄": ["🍓 딸기 케이크", "🍈 멜론 젤리"],
    "여름": ["🍧 팥빙수", "🍉 수박화채", "🥭 망고빙수", "🍮 냉 푸딩"],
    "가을": ["🍠 군고구마", "🍪 밤타르트", "🍎 사과파이"],
    "겨울": ["🥯 호떡", "🐟 붕어빵", "☕ 시나몬롤", "🍫 핫초코"]
}

# 🎀 앱 제목
st.title("🍱 오늘의 점메추!!")
st.markdown("음식 종류 또는 계절을 선택하면, 어울리는 점심과 디저트를 추천해드릴게요! 🍽️🍰")

# 🧭 추천 방식 선택
mode = st.radio("추천 기준을 선택하세요:", ["🍱 음식 종류", "🗓️ 계절"])

# 🍱 음식 종류 추천
if mode == "🍱 음식 종류":
    category = st.selectbox("🍴 어떤 음식이 땡기나요?", list(category_menus.keys()))
    if st.button("🎁 메뉴 + 디저트 추천 받기", key="category"):
        menu = random.choice(category_menus[category])
        dessert = random.choice(category_desserts[category])

        st.markdown(
            f"""
            <div class="center-text">
                🍽️ 오늘의 점심은 <span class="highlight">{menu}</span><br>
                🍰 어울리는 디저트는 <span class="highlight">{dessert}</span>
            </div>
            """,
            unsafe_allow_html=True
        )

# 🗓️ 계절 추천
elif mode == "🗓️ 계절":
    season = st.selectbox("📅 현재 계절은?", list(seasonal_menus.keys()))
    if st.button("🎁 메뉴 + 디저트 추천 받기", key="season"):
        menu = random.choice(seasonal_menus[season])
        dessert = random.choice(seasonal_desserts[season])

        st.markdown(
            f"""
            <div class="center-text">
                🍽️ 오늘의 계절 메뉴는 <span class="highlight">{menu}</span><br>
                🍰 어울리는 디저트는 <span class="highlight">{dessert}</span>
            </div>
            """,
            unsafe_allow_html=True
        )
