import streamlit as st
import requests

st.set_page_config(page_title="Ziad's Chatbot")


st.markdown("""
    <h1 style='text-align: center;'>Ziad's AI Chatbot</h1>
    <p style='text-align: center;'>تقدر تكتب أي سؤال والروبوت هيرد عليك</p>
""", unsafe_allow_html=True)


API_URL = "http://127.0.0.1:8000/chat"

if "messages" not in st.session_state:
    st.session_state.messages = []  

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("اكتب سؤالك هنا...")

if st.button("مسح المحادثة"):
    st.session_state.messages = []
    st.rerun()

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("الرد بيجهز..."):
            try:
                response = requests.post(API_URL, json={"user_input": user_input})
                if response.status_code == 200:
                    reply = response.json().get("response", "مش عارف افيدك اوي")
                else:
                    reply = f"خطأ في الاتصال: {response.status_code}"
            except Exception as e:
                reply = f"فشل الاتصال بالسيرفر: {str(e)}"

        st.markdown(reply)
        st.session_state.messages.append({"role": "assistant", "content": reply})
