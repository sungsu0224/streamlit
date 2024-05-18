import streamlit as st
import pandas as pd
from annotated_text import annotated_text


name = st.query_params["name"]


# 페이지 제목 및 설명

st.title("학생 피드백 페이지")

st.write("이 페이지에서 학부모님들이 학생들의 피드백 결과를 볼 수 있습니다.")

with st.expander("2024년 05월",expanded=True) :
    st.write("이름 :"+ name)
    st.write("성적표")
    st.write("피드백 내용")

with st.expander("2024년 04월") :
    st.write("이름 :"+ name)
    st.write("성적표")
    st.write("피드백 내용")
with st.expander("2024년 03월") :
    st.write("이름 :"+ name)
    st.write("성적표")
    st.write("피드백 내용")