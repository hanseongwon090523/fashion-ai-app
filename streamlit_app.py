# streamlit_app.py
import streamlit as st

def classify_style(text):
    text = text.lower()
    if "크롭" in text or "여자" in text:
        return "미니멀", "심플하고 세련된 미니멀 스타일이에요."
    elif "스트릿" in text or "오버핏" in text:
        return "스트릿", "자유롭고 개성 있는 스트릿 감성이에요."
    elif "자켓" in text or "정장" in text or "블랙" in text:
        return "포멀", "깔끔하고 단정한 포멀 스타일이에요."
    elif "빈티지" in text or "데님" in text:
        return "빈티지", "유니크하고 멋스러운 빈티지 무드에요."
    else:
        return "캐주얼", "편안하고 데일리한 캐주얼 스타일이에요."

st.title("👕 옷 스타일 분석기")
user_input = st.text_input("입고 싶은 옷 이름이나 스타일을 입력해주세요:")
if user_input:
    style, comment = classify_style(user_input)
    st.success(f"📌 스타일 분류: {style}")
    st.info(f"🧠 코멘트: {comment}")