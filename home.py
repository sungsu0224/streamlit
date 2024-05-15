import streamlit as st

# 제목
st.title("Hello, Streamlitaa!")

# 텍스트
st.write("This is a simple Streamlit app.")

# 사용자 입력
user_input = st.text_input("Enter some text:")

st.text("her")
# 입력된 텍스트 출력
if user_input:
    st.write(f"You entered: {user_input}")
