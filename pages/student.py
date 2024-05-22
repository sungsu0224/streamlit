import streamlit as st
import pandas as pd
from annotated_text import annotated_text
from Dao import pymongo_users
import pandas as pd
from bson.objectid import ObjectId
from datetime import datetime

params = st.query_params
name = ""


if len(params) == 0 :
    st.error("잘못된 접근입니다.")
    all_feedback = pd.DataFrame(pymongo_users.getAllFeedback())
    st.dataframe(all_feedback)

else :
    name = params["name"]

name = ObjectId (name)
users = pd.DataFrame(pymongo_users.getUserById(name))
allFeedback = pd.DataFrame(pymongo_users.getFeedback(name))

student_name = users['name'][0]


st.title("["+student_name+"] 학생 피드백")

st.write("이 페이지에서 학부모님들이 학생들의 피드백 결과를 볼 수 있습니다.")


flag = 1
for feedback in allFeedback.iterrows():
    time = feedback[1][3]
    time = datetime.strptime(feedback[1][3],'%Y-%m-%d %H:%M:%S.%f').strftime('%Y년 %m월 %d일')
    content = feedback[1][2]
    
    with st.expander(time+" 작성 피드백",expanded=flag):
         st.write(content)
    flag = 0

if st.button("aa"):
    st.switch_page("home.py")
# st.link_button("home","/")