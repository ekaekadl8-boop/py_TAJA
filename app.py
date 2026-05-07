import streamlit as st
import random
import time

# -----------------------------
# 페이지 설정
# -----------------------------
st.set_page_config(
    page_title="Python 명령어 타자 연습",
    page_icon="⌨️",
    layout="wide"
)

st.title("⌨️ Python 명령어 타자 연습")
st.write("Python 코드를 그대로 입력해보세요!")

# -----------------------------
# 난이도별 문제
# -----------------------------
LEVELS = {
    "초급": [
        'print("Hello World")',
        "x = 10",
        "name = input('이름 입력: ')",
        "for i in range(5):\n    print(i)",
        "numbers = [1, 2, 3, 4]",
    ],

    "중급": [
        "def add(a, b):\n    return a + b",
        "for i in range(1, 10):\n    print(i * 2)",
        "with open('test.txt', 'r') as file:\n    data = file.read()",
        "my_dict = {'a':1, 'b':2}\nfor key, value in my_dict.items():\n    print(key, value)",
        "squares = [x*x for x in range(10)]",
    ],

    "고급": [
        "class Person:\n    def __init__(self, name):\n        self.name = name\n\n    def greet(self):\n        print(f'Hello {self.name}')",
        
        "try:\n    result = 10 / 0\nexcept ZeroDivisionError:\n    print('에러 발생')",

        "import asyncio\n\nasync def main():\n    await asyncio.sleep(1)\n    print('Done')",

        "lambda_func = lambda x: x**2\nprint(lambda_func(5))",

        "@decorator\ndef hello():\n    print('Hello')",
    ]
}

# -----------------------------
# 난이도 선택
# -----------------------------
difficulty = st.selectbox(
    "난이도를 선택하세요",
    ["초급", "중급", "고급"]
)

# -----------------------------
# 세션 상태
# -----------------------------
if "target_code" not in st.session_state:
    st.session_state.target_code = random.choice(LEVELS[difficulty])

if "start_time" not in st.session_state:
    st.session_state.start_time = None

if "finished" not in st.session_state:
    st.session_state.finished = False

if "current_level" not in st.session_state:
    st.session_state.current_level = difficulty

# 난이도 바뀌면 새 문제
if st.session_state.current_level != difficulty:
    st.session_state.target_code = random.choice(LEVELS[difficulty])
    st.session_state.current_level = difficulty
    st.session_state.start_time = None
    st.session_state.finished = False

# -----------------------------
# 새 문제 버튼
# -----------------------------
if st.button("🎲 새 문제"):
    st.session_state.target_code = random.choice(LEVELS[difficulty])
    st.session_state.start_time = None
    st.session_state.finished = False

# -----------------------------
# 문제 표시
# -----------------------------
st.subheader("📌 아래 Python 코드를 입력하세요")

st.code(st.session_state.target_code, language="python")

# -----------------------------
# 코드 입력창
# -----------------------------
user_input = st.text_area(
    "💻 코드 입력",
    height=300,
    placeholder="여기에 Python 코드를 입력하세요...",
)

# -----------------------------
# 입력 시작 시간
# -----------------------------
if user_input and st.session_state.start_time is None:
    st.session_state.start_time = time.time()

# -----------------------------
# 정확도 계산
# -----------------------------
if user_input:

    target = st.session_state.target_code

    correct_chars = sum(
        1 for a, b in zip(user_input, target)
        if a == b
    )

    accuracy = (correct_chars / len(target)) * 100

    st.progress(min(int(accuracy), 100))

    col1, col2 = st.columns(2)

    with col1:
        st.metric("정확도", f"{accuracy:.1f}%")

    with col2:
        st.metric("입력 길이", f"{len(user_input)} / {len(target)}")

    # -----------------------------
    # 완료 체크
    # -----------------------------
    if user_input == target and not st.session_state.finished:

        elapsed = time.time() - st.session_state.start_time

        # 코드 기준 타수 계산
        cpm = (len(target) / elapsed) * 60

        st.session_state.finished = True

        st.success("🎉 정답입니다!")

        result_col1, result_col2 = st.columns(2)

        with result_col1:
            st.metric("걸린 시간", f"{elapsed:.2f}초")

        with result_col2:
            st.metric("타수(CPM)", f"{cpm:.0f}")

# -----------------------------
# 하단 설명
# -----------------------------
st.markdown("---")

st.info("""
✅ 기능
- Python 코드 타자 연습
- 난이도 선택
- 코드 입력창 제공
- 정확도 계산
- CPM(분당 타수) 측정
""")
