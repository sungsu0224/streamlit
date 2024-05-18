import streamlit as st
import pandas as pd
from st_aggrid import AgGrid

# 데이터 파일을 적절한 인코딩으로 읽기
# CSV 파일 예시
# df = pd.read_csv('your_data_file.csv', encoding='cp949')

# Excel 파일 예시
# df = pd.read_excel('your_data_file.xlsx')

# 여기서는 예시로 DataFrame을 생성합니다.
data = {
    'column1': [1, 2, 3, 4],
    'column2': ['A', 'B', 'C', 'D']
}
df = pd.DataFrame(data)

# Streamlit 앱으로 DataFrame 표시
st.title('AgGrid Example')
AgGrid(df)