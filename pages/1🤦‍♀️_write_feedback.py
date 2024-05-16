import streamlit as st
import pandas as pd
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

# 페이지 제목 및 설명
st.title("리아영어 학생 피드백 작성 페이지")
st.write("이 페이지를 사용하여 학생의 학습 피드백을 작성할 수 있습니다. 작성된 피드백은 학부모님께 전달됩니다.")

# 학생 정보 입력
st.header("학생 정보")
student_name = st.text_input("학생 이름")
phone_number = st.text_input("전화번호")

# 데이터프레임 생성
data = {
    "회차": [f"수업 {i+1}" for i in range(9)],
    "문법 점수": [0] * 9,
    "단어 점수": [0] * 9,
    "출석 점수": [0] * 9
}
df = pd.DataFrame(data)

# 피드백 내용 입력
st.header("피드백 내용")
feedback_content = st.text_area("피드백 내용을 입력하세요")

# 피드백 제출 버튼
if st.button("피드백 제출"):
    # 제출된 데이터를 데이터프레임으로 변환
    submitted_df = pd.DataFrame({
        "회차": [f"수업 {i+1}" for i in range(9)],
        "문법 점수": [st.session_state.get(f"문법 점수_{i}", 0) for i in range(9)],
        "단어 점수": [st.session_state.get(f"단어 점수_{i}", 0) for i in range(9)],
        "출석 점수": [st.session_state.get(f"출석 점수_{i}", 0) for i in range(9)]
    })
    
    # 이미지 생성 함수
    def create_feedback_image(df, feedback_content, student_name, phone_number):
        # 이미지 크기 설정
        width, height = 800, 1000
        image = Image.new('RGB', (width, height), 'white')
        draw = ImageDraw.Draw(image)

        # 폰트 설정 (시스템 기본 폰트 사용)
        font = ImageFont.load_default()

        # 배경 그리기
        draw.rectangle([0, 0, width, height], fill="#d1ecf1")

        # 타이틀 그리기
        draw.rectangle([50, 20, 750, 100], fill="#ffffff")
        draw.text((100, 40), "리아영어 학생 피드백", fill="#008080", font=font)
        draw.text((600, 40), f"[{student_name}]", fill="#008080", font=font)

        # 학생 정보 그리기
        draw.rectangle([50, 120, 750, 160], fill="#ffffff")
        draw.text((60, 130), f"학생 이름: {student_name}", fill="black", font=font)
        draw.text((300, 130), f"전화번호: {phone_number}", fill="black", font=font)

        # 테이블 그리기
        table_top = 180
        row_height = 30
        col_width = 180

        headers = ["회차", "문법 점수", "단어 점수", "출석 점수"]
        for col_num, header in enumerate(headers):
            draw.text((60 + col_num * col_width, table_top), header, fill="black", font=font)

        for row_num, row in enumerate(df.values):
            for col_num, cell in enumerate(row):
                draw.text((60 + col_num * col_width, table_top + (row_num + 1) * row_height), str(cell), fill="black", font=font)

        # 피드백 내용 그리기
        draw.rectangle([50, table_top + 10 * row_height + 20, 750, table_top + 10 * row_height + 220], fill="#ffffff")
        draw.text((60, table_top + 10 * row_height + 40), "피드백 내용:", fill="black", font=font)
        draw.text((60, table_top + 10 * row_height + 70), feedback_content, fill="black", font=font)

        # 이미지 버퍼에 저장
        buf = BytesIO()
        image.save(buf, format="PNG")
        buf.seek(0)
        return buf

    # 이미지 생성
    img_buffer = create_feedback_image(submitted_df, feedback_content, student_name, phone_number)

    # 이미지 다운로드 링크 생성
    st.download_button(
        label="피드백 이미지 다운로드",
        data=img_buffer,
        file_name="feedback.png",
        mime="image/png"
    )

    # 제출된 피드백을 테이블 형식으로 표시
    st.write("### 제출된 피드백")
    st.write(f"**학생 이름:** {student_name}")
    st.write(f"**전화번호:** {phone_number}")
    st.write(submitted_df)
    st.write("**피드백 내용:**")
    st.write(feedback_content)
