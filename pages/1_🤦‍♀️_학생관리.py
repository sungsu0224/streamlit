import streamlit as st
import pandas as pd
from Dao import pymongo_users
from annotated_text import annotated_text


# 페이지 제목 및 설명
st.title("학생관리 페이지")
st.write("선생님이 학생들의 정보 등록 /수정/삭제 할 수 있고, 각 학생에 대한 피드백을 작성할 수 있음")

st.divider()
with st.expander("신규 원생 등록"):
    classes = st.number_input("수업", step=1)
    name = st.text_input("학생이름")
    phone = st.text_input("전화번호")
    age = st.number_input("나이", step=1)
    parentPhone = st.text_input("학부모 연락처")
    link = "student?name=" + name
    if st.button("등록하기"):
        pymongo_users.setUsers(classes, name, phone, age, parentPhone, link)

st.divider()

annotated_text("각 ", ("반별 학생의 정보", "", ""), "를 확인할 수 있습니다.")

# MongoDB에서 데이터 읽기
studentDf = pd.DataFrame(pymongo_users.getUsers())

for index, row in studentDf.iterrows():
    with st.expander(row['name']):
        st.write(f"Age: {row['age']}")
        st.write(f"parentPhone: {row['parentPhone']}")
st.divider()

annotated_text(("모든 학생들의 정보", "", ""), "를 확인할 수 있습니다")


student_name = st.selectbox('학생을 선택하세요', studentDf['name'])

student_details = studentDf[studentDf['name'] == student_name]
st.write(f"### Details of {student_name}")
st.write(student_details)
