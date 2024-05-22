import streamlit as st
import pandas as pd
from datetime import datetime
from Dao import pymongo_users
from annotated_text import annotated_text
from streamlit_option_menu import option_menu

import time

# 5. Add on_change callback
def on_change(key):
    selection = st.session_state[key]
    st.write(f"Selection changed to {selection}")
    

# MongoDB에서 데이터 읽기
studentDf = pd.DataFrame(pymongo_users.getUsers())
studentDf['academy'] = studentDf['academy'].fillna(2).astype(int)
studentDf['classes'] = studentDf['classes'].fillna(2).astype(int)



@st.experimental_dialog("수정하기")
def studentInfoChg(id):
    chg_df = studentDf[studentDf['_id'] == id].iloc[0]
    classes = st.number_input("수업",value=chg_df['classes'],format="%d", step=1)
    name = st.text_input("이름", value = chg_df['name'])
    phone = st.text_input("전화", value = chg_df['phone'])
    age = st.text_input("학생나이", value = chg_df['age'])
    parentPhone = st.text_input("학부모연락처", value=chg_df['parentPhone'])
    if st.button("수정완료"):
        with st.status("수정중.. 잠시만 기다려주세요..") as status:
            pymongo_users.updateUsers(id,classes,name,phone,age,parentPhone)
            status.update(label="수정완료! 잠시후 창을 닫습니다",state="complete")
        time.sleep(1)
        st.experimental_rerun()  # 새로고침
        
    #st.button("삭제하기",type="primary"):




# 페이지 제목 및 설명
st.title("For _선생님_")
annotated_text("학생 ", ("등록을 위한", "", ""), "과정들")
st.divider()

with st.expander("등록 상담"):
    academy = st.text_input("학원")
    classes = st.number_input("수업",value=1,format="%d", step=1)
    name = st.text_input("이름")
    phone = st.text_input("전화번호")
    age = st.number_input("나이", value=10,format="%d", step=1)
    parentPhone = st.text_input("학부모 연락처")
    link = "student?name=" + name
    if st.button("등록하기"):
        pymongo_users.setUsers(academy,classes, name, phone, age, parentPhone, link)

with st.expander("학원 설명"):
    st.write("## Reading")
    st.write("1. 예습 (모르는 단어 찾기 + 해석해보기)")
    st.write("2. 직접 읽고 해석해보기")
    st.write("3. 해석 첨삭")
    st.write("4. 주제 잡기")

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
with st.expander("반 배정"):
    st.write("이곳에선 미배정된 아이들의 반을 배정할 수 있습니다.")

st.divider()
annotated_text("각 반별 학생들의 ", ("정보 조회/수정 및 피드백 작성", "", ""), "을 할 수 있습니다.")
col = st.columns([1,1])


for num in studentDf.sort_values(by="classes")['classes'].unique():
    with st.container(border=True):
        filtered_df = studentDf[studentDf['classes'] == num]
        st.write(str(num)+"반")
        for index, row in filtered_df.iterrows():
            with st.expander(row['name']):
                st.write(f"Age: {row['age']}")
                st.write(f"parentPhone: {row['parentPhone']}")
                st.write(f"phone: {row['phone']}")
                st.write(f"academy: {row['academy']}")
                st.write(f"classes: {row['classes']}")
                col = st.columns([1,1])
                if col[0].button("수정하기",use_container_width=True,key="수정하기"+str(row['_id'])):
                    studentInfoChg(row['_id'])
                col[1].link_button("피드백 보기","student/?name="+str(row['_id']),use_container_width=True,type="primary")
                         

                with st.container(border=True):
                    content = st.text_input(label = "피드백 작성",key="피드백작성"+str(row['_id']))
                    timestamp = st.text("작성일 " + datetime.now().strftime('%Y 년 %m월 %d일'))
                    st.write(content)
                    if st.button("피드백 작성완료",key="제출"+str(row['_id'])) :
                        pymongo_users.setFeedback(str(row['_id']),str(content), str(datetime.now()))
                        st.write("finished")
                        
                    st.divider()
                
        
        

st.divider()