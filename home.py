import streamlit as st
import pandas as pd
from Dao import pymongo_users
from annotated_text import annotated_text
from streamlit_option_menu import option_menu

import time

# 5. Add on_change callback
def on_change(key):
    selection = st.session_state[key]
    st.write(f"Selection changed to {selection}")

if '_id' not in st.session_state:
    st.session_state['_id'] = 'default'

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
st.title("리아영어")
st.divider()

if st.button("등록상담",use_container_width=True,type="primary"):
    st.switch_page("pages/newstudent.py")

st.write("## 학생 관리")
annotated_text("각 반별 학생들의 ", ("정보 조회/수정 및 피드백 작성", "", ""), "을 할 수 있습니다.")
col = st.columns([1,1])


for num in studentDf.sort_values(by="classes")['classes'].unique():
    with st.container(border=True):
        filtered_df = studentDf[studentDf['classes'] == num]
        st.write(str(num)+"반")

        classCol = st.columns([2,1,1])
        for index, row in filtered_df.iterrows():
            with classCol[0].expander("[ "+row['name'] +" ] 학생 정보"):
                st.write(f"Age: {row['age']}")
                st.write(f"parentPhone: {row['parentPhone']}")
                st.write(f"phone: {row['phone']}")
                st.write(f"academy: {row['academy']}")
                st.write(f"classes: {row['classes']}")
                col = st.columns([1,1])
                if col[0].button("수정하기",use_container_width=True,key="수정하기"+str(row['_id'])):
                    studentInfoChg(row['_id'])
                        
            if classCol[1].button("지난 피드백",key = "지난피드백"+str(row['_id']),use_container_width=True):
                    st.session_state['_id'] = str(row['_id'])
                    st.switch_page("pages/student")
            if classCol[2].button("피드백 작성",key ="피드백"+str(row['_id']),use_container_width=True):
                    st.session_state['_id'] = str(row['_id'])
                    st.switch_page("pages/writefeedback.py")
            
                
        
        

st.divider()