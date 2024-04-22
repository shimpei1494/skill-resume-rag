import streamlit as st
from service.gemini_answer import gemini_answer

st.title("RAG test")

## オプションを定義
model_options = ['gemini-1.5pro', 'GPT-4-turbo']

## セレクトボックスをサイドバーに作成
selected_option = st.sidebar.selectbox('モデルを選択してください:', model_options)
# 選択したモデルを基にインスタンスを作成（classも後で作成）→それを実行することでモデルやベクトルDBを可変にできるようにしたい

prompt = st.chat_input("What is up?")

if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = gemini_answer(prompt)
        # response = selected_option
        st.markdown(response)