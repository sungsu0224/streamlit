import streamlit as st
from Dao import pymongo_users
# 제목
st.title("Hello, This is Lia English")

# 텍스트
st.write("Coming Soon")
st.write("💁🏻 학생 별 정보 페이지")


# 사용자 입력
user_input = st.text_input("Enter some text:")

if st.button("readDatas"):
    users = pymongo_users.connectTest()

if st.button("readUserInfo"):
    users = pymongo_users.getUsers()
    st.dataframe(users)

if st.button("writeUserInfo"):    
    pymongo_users.setUsers("kim","24")
    

st.text("her")
# 입력된 텍스트 출력
if user_input:
    st.write(f"You entered: {user_input}")
