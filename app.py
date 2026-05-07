import streamlit as st
import random
import time

# -----------------------------
# 타자 연습 문장 리스트
# -----------------------------
SENTENCES = [
    "Python is fun and powerful.",
    "Streamlit makes web apps easy.",
    "Practice typing every day.",
    "Fast typing improves productivity.",
    "GitHub is useful for version control.",
    "Coding skills grow with practice.",
    "Artificial intelligence is transforming the world.",
    "Consistency is the key to improvement."
]

# -----------------------------
# 페이지 설정
# -----------------------------
st.set_page_config(
    page_title="타자 연습 앱",
    page_icon="⌨️",
    layout="centered"
)

st.title("⌨️ Python 타자 연습 앱")
st.write("문장을 빠르게 입력해보세요!")

# -----------------------------
# 세션 상태 초기화
# -----------------------------
if "target_sentence" not in st.session_state:
    st.session_state.target_sentence = random.choice(SENTENCES)

if "start_time" not in st.session_state:
    st.session_state.start_time = None

if "finished" not in st.session_state:
    st.session_state.finished = False

# -----------------------------
# 새 문장 버튼
# -----------------------------
if st.button("새 문장 시작"):
    st.session_state.target_sentence = random.choice(SENTENCES)
    st.session_state.start_time = None
    st.session_state.finished = False

# -----------------------------
# 목표 문장 표시
# -----------------------------
st.subheader("📌 따라 입력할 문장")
st.info(st.session_state.target_sentence)

# -----------------------------
# 사용자 입력
# -----------------------------
user_input = st.text_input("⌨️ 문장을 입력하세요")

# 입력 시작 시간 기록
if user_input and st.session_state.start_time is None:
    st.session_state.start_time = time.time()

# -----------------------------
# 결과 계산
# -----------------------------
if user_input:
    target = st.session_state.target_sentence

    # 정확도 계산
    correct_chars = sum(
        1 for a, b in zip(user_input, target) if a == b
    )

    accuracy = (correct_chars / len(target)) * 100

    st.write(f"정확도: {accuracy:.1f}%")

    # 완료 여부
    if user_input == target and not st.session_state.finished:
        end_time = time.time()
        elapsed = end_time - st.session_state.start_time

        # WPM 계산
        words = len(target.split())
        wpm = (words / elapsed) * 60

        st.session_state.finished = True

        st.success("🎉 완료했습니다!")
        st.write(f"⏱️ 걸린 시간: {elapsed:.2f}초")
        st.write(f"🚀 타자 속도: {wpm:.2f} WPM")

# -----------------------------
# 하단 안내
# -----------------------------
st.markdown("---")
st.caption("Python + Streamlit으로 만든 타자 연습 웹앱")
