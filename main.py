import streamlit as st
import random

# 이모티콘과 함께한 각 분야별 점심 메뉴 리스트
menus = {
    "한식": ["🍚 비빔밥", "🥩 불고기", "🥣 김치찌개", "🥬 된장찌개", "🌶️ 제육볶음", "🥓 삼겹살", "❄️ 냉면", "🍜 칼국수"],
    "중식": ["🍜 짜장면", "🌶️ 짬뽕", "🍖 탕수육", "🌶️ 마라탕", "🍗 깐풍기", "🥗 양장피", "🍤 유산슬", "🍳 볶음밥"],
    "일식": ["🍣 초밥", "🍲 우동", "🥩 규동", "🐽 돈까스", "🍜 라멘", "🍱 가츠동", "🦐 텐동", "🥞 오코노미야끼"],
    "양식": ["🍝 파스타", "🥩 스테이크", "🍔 햄버거", "🍕 피자", "🧀 그라탱", "🥄 리조또", "🥗 샐러드", "🍗 치킨"]
}

# 앱 제목
st.title("🍽️ 오늘의 점심 메뉴 추천기")

# 설명
st.markdown("한식, 중식, 일식, 양식 중에서 하나를 선택하면, 이모티콘과 함께한 추천 메뉴를 보여드려요!")

# 선택 박스
category = st.selectbox("🍱 먹고 싶은 음식 종류를 선택하세요:", list(menus.keys()))

# 버튼 클릭 시 추천
if st.button("메뉴 추천 받기"):
    recommended = random.choice(menus[category])
    
    # 한 줄 출력 + 파란색 텍스트 적용
    st.markdown(
        f"""
        <h1 style='text-align: center; font-size: 48px; margin-top: 30px; color: #1E90FF;'>
            ✨ 오늘의 추천 메뉴는 {recommended} 입니다!
        </h1>
        """,
        unsafe_allow_html=True
    )
