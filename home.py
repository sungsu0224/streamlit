import streamlit as st
from Dao import pymongo_users
from annotated_text import annotated_text
# 제목
st.title("피드백")

# 텍스트
annotated_text(
    "This ",
    ("is", "verb"),
    " some ",
    ("annotated", "adj"),
    ("text", "noun"),
    " for those of ",
    ("you", "pronoun"),
    " who ",
    ("like", "verb"),
    " this sort of ",
    ("thing", "noun"),
    "."
)


