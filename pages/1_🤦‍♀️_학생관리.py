import streamlit as st
import pandas as pd
from datetime import datetime
from Dao import pymongo_users
from annotated_text import annotated_text
import time

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
st.title("학생관리 페이지")
st.write("선생님이 학생들의 정보 등록 /수정/삭제 할 수 있고, 각 학생에 대한 피드백을 작성할 수 있음")

st.divider()

annotated_text("신규 원생 ", ("등록", "", ""), "을 할 수 있습니다.")

with st.expander("신규 원생 등록"):
    academy = st.text_input("학원")
    classes = st.number_input("수업",value=10,format="%d", step=1)
    name = st.text_input("이름")
    phone = st.text_input("전화번호")
    age = st.number_input("나이", value=10,format="%d", step=1)
    parentPhone = st.text_input("학부모 연락처")
    link = "student?name=" + name
    if st.button("등록하기"):
        pymongo_users.setUsers(academy,classes, name, phone, age, parentPhone, link)

st.divider()

annotated_text("각 반별 학생들의 ", ("정보 조회/수정 및 피드백 작성", "", ""), "을 할 수 있습니다.")
col = st.columns([1,1])


for num in studentDf.sort_values(by="classes")['classes'].unique():
    with st.container(border=True):
        filtered_df = studentDf[studentDf['classes'] == num]
        st.write(str(num)+"반 학생들의 정보입니다.")
        for index, row in filtered_df.iterrows():
            with st.expander(row['name']):
                st.write(f"Age: {row['age']}")
                st.write(f"parentPhone: {row['parentPhone']}")
                st.write(f"phone: {row['phone']}")
                st.write(f"link: {row['link']}")
                st.write(f"academy: {row['academy']}")
                st.write(f"classes: {row['classes']}")
                if st.button("수정하기",use_container_width=True,key="수정하기"+str(row['_id'])):
                    studentInfoChg(row['_id'])
                if st.button("피드백 작성",type="primary",use_container_width=True,key="피드백"+str(row['_id'])):
                    st.text_input(label = "피드백 작성",key="피드백작성"+str(row['_id']))
                    st.text("작성일 " + datetime.now().strftime('%Y 년 %m월 %d일'))
                    st.button("피드백 제출하기",key="제출"+str(row['_id']))
        st.dataframe(filtered_df)
                
        
        

st.divider()

annotated_text(("모든 학생들의 정보", "", ""), "를 확인할 수 있습니다")


st.dataframe(studentDf)