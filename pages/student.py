import streamlit as st
import pandas as pd
from annotated_text import annotated_text


params = st.query_params
name = ""


if len(params) == 0 :
    st.error("잘못된 접근입니다.")
else :
    name = params["name"]

st.title("["+name+" 학생] 피드백")

st.write("이 페이지에서 학부모님들이 학생들의 피드백 결과를 볼 수 있습니다.")

# 각달의 피드백 내용을 보여주고싶음.
# 우선 DB가 없음.. db에 학생별 피드백 내용이 저장되어야함.. 이는 관리자 페이지에서 만들고 여기선 보여지기만 할꺼임
# 매달에 대한 반복문이 진행될 예정.

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