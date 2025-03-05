import streamlit as st
import google.generativeai as genai
import os

# API Key Securely Load Karein
api_key = "AIzaSyBn5CZqnelyoreQzLhy5XRdxSflqYR8KSY"  # Apni API key yahan paste karein
genai.configure(api_key=api_key)

# Custom CSS for better UI styling
st.markdown(
    """
    <style>
        .stTextInput>div>div {
            margin-top: -20px;
        }
        .stChatInput>div {
            margin-top: -20px;
        }
        .stTitle {
            text-align: center;
            font-size: 32px;
            font-weight: bold;
            color: #4A90E2;
        }
        .chat-container {
            max-width: 700px;
            margin: auto;
            padding: 10px;
            border-radius: 10px;
            background: #f9f9f9;
        }
        .stChatMessageUser {
            background-color: #DCF8C6;
            padding: 8px;
            border-radius: 10px;
            margin-bottom: 5px;
        }
        .stChatMessageAssistant {
            background-color: #E6E6E6;
            padding: 8px;
            border-radius: 10px;
            margin-bottom: 5px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("<h1 class='stTitle'>Gemini AI Chatbot</h1>", unsafe_allow_html=True)

# Multi-turn chat ka system banayein
if "messages" not in st.session_state:
    st.session_state.messages = []

# Purani messages ko display karein
st.markdown("<div class='chat-container'>", unsafe_allow_html=True)
for message in st.session_state.messages:
    role_class = "stChatMessageUser" if message["role"] == "user" else "stChatMessageAssistant"
    st.markdown(f"<div class='{role_class}'>{message['content']}</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

user_input = st.chat_input("Aap ka sawal likhein:")

if user_input:
    # User ka message save karein
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    try:
        # AI Response Generate karein
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(user_input)
        ai_message = response.text

        # AI ka response save karein
        st.session_state.messages.append({"role": "assistant", "content": ai_message})
        with st.chat_message("assistant"):
            st.markdown(ai_message)

    except Exception as e:
        st.error(f"Error: {str(e)}")