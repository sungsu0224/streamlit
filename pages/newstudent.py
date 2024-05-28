import streamlit as st
import pandas as pd
from annotated_text import annotated_text
from Dao import pymongo_users
from datetime import datetime



st.title('리아영어 상담카드')


with st.expander("상담카드 작성"):
    annotated_text("학생 상담을 위한 양식입니다😘 ",("최대한 자세히 작성","","") , "해주시면 상담에 큰 도움이 됩니다!")
    
    academy = st.text_input("학원")
    name = st.text_input("이름")
    age = st.number_input("나이", value=10,format="%d", step=1)
    phone = st.text_input("전화번호")
    parentPhone = st.text_input("학부모 연락처")
    link = st.text_area("선생님에게 하고 싶으신 말씀")
    classes = st.number_input("수업",value=0,format="%d", step=1)

    if st.button("저장하기"):
        pymongo_users.setUsers(academy,classes, name, phone, age, parentPhone, link)


with st.expander("학원 소개"):
    st.write("## :Reading")
    st.write(" 1. 예습 (모르는 단어 찾기 + 해석해보기)")
    st.write(" 2. 직접 읽고 해석해보기")
    st.write(" 3. 해석 첨삭")
    st.write(" 4. 주제 잡기")

    st.write("homework")
    st.write("1. 그날 배운것 공책에 해석하기/ 고재 문제 풀기")
    st.write("2. 다음주 리딩 예습하기")

    st.divider()
    st.write("## Grammer")
    st.write("1. 문법의 큰 틀을 잡는 수업")
    st.write("2. 전에 배운 내용들 복습")
    st.write("3. 질문이 많은 수업")

    st.write("homework")
    st.write("1. 본책+ WorkBook 문제 풀기")
    st.divider()

    st.write("## Listening")
    st.write("수업x")
    st.write("1. 문제풀기")
    st.write("2. 낭독하기")

    st.divider()
    st.write("## Voca")
    st.write("60-120개 (반마다다름)")

    st.write("1. 그 외")
    st.write("2. 매주 배운 내용 Weekly Test (미통과시 일요일 보충!)")
    st.write("3. 그 주 숙제 완료 못할시 주말 보충")
    st.write("4. 매달 Monthly Test를 통한 총 복습")
    st.write("5. 한달에 주 8회 수업, 교재비 별도 (달 1회 보충 가능)")
    st.write("")

st.divider()
if st.button("학생관리",use_container_width=True):
    st.switch_page("home.py")

if st.button("피드백 작성",use_container_width=True):
    st.switch_page("home.py")