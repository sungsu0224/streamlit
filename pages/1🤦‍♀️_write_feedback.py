import streamlit as st
import pandas as pd

# 페이지 제목 및 설명
st.title("리아영어 학생 피드백 작성 페이지")
st.write("이 페이지를 사용하여 학생의 학습 피드백을 작성할 수 있습니다. 작성된 피드백은 학부모님께 전달됩니다.")

# 학생 정보 입력
st.header("학생 정보")
student_name = st.text_input("학생 이름")
phone_number = st.text_input("전화번호")

# 데이터프레임 생성
data = {
    "회차": [f"수업 {i+1}" for i in range(9)],
    "문법 점수": [0] * 9,
    "단어 점수": [0] * 9,
    "출석 점수": [0] * 9
}
df = pd.DataFrame(data)
st.data_editor(df)

# 피드백 내용 입력
st.header("피드백 내용")
feedback_content = st.text_area("피드백 내용을 입력하세요")

# 피드백 제출 버튼
if st.button("피드백 제출"):


    # 제출된 피드백을 테이블 형식으로 표시
    st.write("### 제출된 피드백")
    st.write(f"**학생 이름:** {student_name}")
    st.write(f"**전화번호:** {phone_number}")
    st.dataframe(df)
    st.write("**피드백 내용:**")
    st.write(feedback_content)
