# from dotenv import load_dotenv
# load_dotenv()

import streamlit as st
from langchain_openai import ChatOpenAI

chat_model = ChatOpenAI()

st.title("삼행시 놀이")

# content = st.write("시의 주제는", title)
content = st.text_input('삼행시 주제를 제시해주세요.')

if st.button("시 작성 요청하기"):
    with st.spinner('생각중...'):
        result = chat_model.predict(content+"에 대한 삼행시를 지어줘 (50자 이내)")
        st.write(result)
# print(result)


# title = st.text_input("사의 주제를 정해주세요")
