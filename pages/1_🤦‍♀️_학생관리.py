import streamlit as st
import pandas as pd
from Dao import pymongo_users

# 페이지 제목 및 설명
st.title("학생관리 페이지")
st.write("이 페이지를 사용하여 학생을 등록, 수정, 삭제 할 수 있습니다")

with st.expander("신규 원생 등록") :
    name = st.text_input("학생이름")
    phone = st.text_input("전화번호")
    age = st.number_input("나이")
    parentPhone = st.text_input("학부모 연락처")
    link = "student?name="+name
    if st.button("등록하기"):
        pymongo_users.setUsers(name, phone, age , parentPhone,link)
        
st.divider()
studentDf = pd.DataFrame(pymongo_users.getUsers())
with st.expander("기존 원생 조회",expanded=True) :
    st.dataframe(studentDf,
                 column_config = {
                     "link" : st.column_config.LinkColumn("link",display_text="바로가기")
                 }
    )

# Sample data
data = {
    'Name': ['John Doe', 'Jane Smith', 'Alice Johnson', 'Bob Brown'],
    'Phone Number': ['123-456-7890', '234-567-8901', '345-678-9012', '456-789-0123'],
    'Age': [16, 17, 15, 16],
    'Parent Contact': ['987-654-3210', '876-543-2109', '765-432-1098', '654-321-0987']
}


# Option to view details of a specific student
student_name = st.selectbox('Select a student', studentDf['name'])

if student_name:
    student_details = studentDf[studentDf['name'] == student_name]
    st.write(f"### Details of {student_name}")
    st.write(student_details)
