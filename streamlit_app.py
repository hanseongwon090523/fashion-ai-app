import streamlit as st
import random

st.set_page_config(page_title="옷 스타일 분석기", page_icon="🧥")

st.title("👕 옷 스타일 분석기")
st.caption("입고 싶은 옷 이름이나 스타일 키워드를 입력하면, AI가 스타일을 분석해 드려요!")

# ✅ 사용자 입력 받기
user_input = st.text_input("📝 예: 오버핏 반팔티, 크롭 자켓, 셋업 정장 등")

# ✅ 스타일별 멘트 함수들
def get_minimal_comment():
    return f"{random.choice(['세련되고 단정한', '깔끔하게 떨어지는', '미니멀 감성이 묻어나는'])} 스타일이에요. {random.choice(['심플한 매력이 있어요.', '군더더기 없는 멋이 돋보여요.', '누구에게나 잘 어울리는 느낌이에요.'])}"

def get_street_comment():
    return f"{random.choice(['힙한 분위기의', '자유로운 느낌의', '강렬한 인상의'])} 스트릿룩이에요. {random.choice(['개성이 확실해요!', '트렌디함이 느껴져요.', '에너지가 넘치는 조합이에요.'])}"

def get_formal_comment():
    return f"{random.choice(['포멀하고 클래식한', '단정한 분위기의', '프로페셔널한 느낌의'])} 스타일이에요. {random.choice(['면접이나 발표에 딱이에요.', '신뢰감을 주는 룩이에요.', '고급스러움이 느껴져요.'])}"

def get_vintage_comment():
    return f"{random.choice(['레트로 감성의', '개성 강한', '유니크한 무드의'])} 빈티지 스타일이에요. {random.choice(['시간을 거슬러 올라간 듯한 느낌이에요.', '남들과는 다른 감각이 돋보여요.', '추억을 소환하는 멋이 있어요.'])}"

def get_casual_comment():
    return f"{random.choice(['편안하고 자연스러운', '데일리하게 입기 좋은', '무심한 듯 멋스러운'])} 캐주얼룩이에요. {random.choice(['활동하기 좋아 보여요.', '누구에게나 잘 어울리는 스타일이에요.', '기본에 충실한 멋이 있어요.'])}"

# ✅ 스타일 분류 함수
def classify_style(text):
    text = text.lower()

    if "크롭" in text or "여자" in text or "셔츠" in text:
        return "미니멀", get_minimal_comment()
    elif "스트릿" in text or "오버핏" in text or "후드" in text:
        return "스트릿", get_street_comment()
    elif "자켓" in text or "정장" in text or "블랙" in text:
        return "포멀", get_formal_comment()
    elif "빈티지" in text or "데님" in text or "청" in text:
        return "빈티지", get_vintage_comment()
    else:
        return "캐주얼", get_casual_comment()

# ✅ 결과 출력
if user_input:
    if len(user_input.strip()) < 2:
        st.warning("❗ 두 글자 이상 입력해주세요.")
    else:
        style, comment = classify_style(user_input)
        st.markdown(f"🎯 **스타일 분류:** `{style}`")
        st.success(f"💬 {comment}")
else:
    st.info("👆 위에 입력창에 옷 스타일을 입력해 보세요!")