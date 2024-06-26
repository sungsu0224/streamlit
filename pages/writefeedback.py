import streamlit as st
import pandas as pd
from Dao import pymongo_users
from bson.objectid import ObjectId

if '_id' in st.session_state:
    _id = st.session_state['_id']
else:
    _id = 'default'

users = pd.DataFrame(pymongo_users.getUserById(ObjectId(_id)))
student_name = users['name'][0]

# 페이지 제목 및 설명
st.title("피드백 작성 페이지"+student_name)
st.write("이 페이지를 사용하여 학생의 학습 피드백을 작성할 수 있습니다.")

inputCols = st.columns([1,1,1])


content = st.text_input(label = "피드백 작성",key="피드백작성"+str(users['_id']))
timestamp = st.text("작성일 " + datetime.now().strftime('%Y 년 %m월 %d일'))
st.write(content)
if st.button("피드백 작성완료",key="제출"+str(row['_id'])) :
    pymongo_users.setFeedback(str(users['_id']),str(content), str(datetime.now()))
    st.write("finished")
# 학생 정보 입력
st.header("학생 정보")
student_name = inputCols[0].text_input("학생 이름")
phone_number = inputCols[1].text_input("전화번호")

# 데이터프레임 생성
data = {
    "수업": ["문법", "단어", "출석"],
    "1회차" : [0] * 3,
    "2회차" : [0] * 3,
    "3회차" : [0] * 3,
    "4회차" : [0] * 3,
    "5회차" : [0] * 3,
    "6회차" : [0] * 3,
    "7회차" : [0] * 3,
    "8회차" : [0] * 3,
}
df = pd.DataFrame(data)
updated_df = st.data_editor(df,hide_index=True)

# 피드백 내용 입력
st.header("피드백 내용")
feedback_content = st.text_area("피드백 내용을 입력하세요")

# 피드백 제출 버튼
if st.button("피드백 제출"):
    # 제출된 피드백을 테이블 형식으로 표시
    st.write("### 제출된 피드백")
    st.write(f"**학생 이름:** {student_name}")
    st.write(f"**전화번호:** {phone_number}")
    st.dataframe(updated_df)
    st.write("**피드백 내용:**")
    st.write(feedback_content)
