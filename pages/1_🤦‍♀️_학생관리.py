import streamlit as st
import pandas as pd

# 페이지 제목 및 설명
st.title("학생관리 페이지")
st.write("이 페이지를 사용하여 학생을 등록, 수정, 삭제 할 수 있습니다")


with st.expander("신규 원생 등록") :
    st.text_input("학생이름")
    st.text_input("전화번호")
    st.text_input("나이")
    st.text_input("학부모 연락처")
    

with st.expander("기존 원생 수정") :
    st.write("여기에 기존 원생들 리스트업")

