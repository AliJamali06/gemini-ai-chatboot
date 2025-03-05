# import streamlit as st
# import google.generativeai as genai
# import os

# # ✅ API Key Securely Load Karein
# api_key = "AIzaSyBn5CZqnelyoreQzLhy5XRdxSflqYR8KSY"  # Apni API key yahan paste karein
# genai.configure(api_key=api_key)

# st.title("Gemini AI Chatbot")

# user_input = st.text_input("Aap ka sawal likhein:")

# if st.button("Send"):
#     try:
#         # ✅ Sahi model ka naam use karein
#         model = genai.GenerativeModel("gemini-1.5-flash")  # Faster model
#         response = model.generate_content(user_input)
#         st.write("Gemini AI:", response.text)
#     except Exception as e:
#         st.error(f"Error: {str(e)}")

import streamlit as st
import google.generativeai as genai
import os

# ✅ API Key Securely Load Karein
api_key = "AIzaSyBn5CZqnelyoreQzLhy5XRdxSflqYR8KSY" # Apni API key yahan paste karein
genai.configure(api_key=api_key)

st.title("Gemini AI Chatbot")

# ✅ Multi-turn chat ka system banayein
if "messages" not in st.session_state:
    st.session_state.messages = []

# ✅ Purani messages ko display karein
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.chat_input("Aap ka sawal likhein:")

if user_input:
    # ✅ User ka message save karein
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    try:
        # ✅ AI Response Generate karein
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(user_input)

        ai_message = response.text

        # ✅ AI ka response save karein
        st.session_state.messages.append({"role": "assistant", "content": ai_message})
        with st.chat_message("assistant"):
            st.markdown(ai_message)

    except Exception as e:
        st.error(f"Error: {str(e)}")
