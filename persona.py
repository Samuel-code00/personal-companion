import streamlit as st
from model import model

st.markdown("# Personal AI Companion")

st.write("I am Gemini, I am here to help you and be your personal companion.")

# Create chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history when app is rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input for chat
if prompt := st.chat_input("Start chatting ..."):

    # Add user input to chat history
    st.session_state.messages.append({'role': 'user', 'content': prompt})

    # Display user message in chat container
    with st.chat_message('user'):
        st.markdown(prompt)

    # Display summarizer response in chat container
    with st.chat_message('assistant'):
        message_placeholder = st.markdown("...")
        full_response = " "
        # Get summary from Summarizer
        try:
            result = model.generate_content(prompt)
            full_response += result.text
            message_placeholder.markdown(full_response)
        except:
            full_response = "Error while generating answer Try checking your connection or reload browser."
            message_placeholder.markdown(full_response)

    # Add summarizer reply to chat history
    st.session_state.messages.append(
        {'role': 'assistant', 'content': full_response})