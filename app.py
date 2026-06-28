import streamlit as st
from agent import ask_agent
st.set_page_config(page_title="Web Search Agent", page_icon="🔍")
st.title(" Web Search Agent")
if "messages" not in st.session_state:
    st.session_state.messages = []
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
user_input = st.chat_input("Ask me anything...")
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)
    with st.chat_message("assistant"):
        response = ask_agent(user_input)
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})