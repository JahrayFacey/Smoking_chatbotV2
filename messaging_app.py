import streamlit as st
import requests

rasa_url = "http://localhost:5055/webhook"

st.set_page_config(page_title="Over The Mountain", layout="centered")
st.title("Over The Mountain(paul)")
st.write("My name is Paul, your supportive chatbot ready to help in anyway to conquer your smoking")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Type your message here...")
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

response = requests.post(
    rasa_url,
    json={"sender": "user", "message": user_input}
)

if response.status == 200:
    rasa_reply = response.json()
    for reply in rasa_reply:
        bot_message = reply.get("text", "")
        st.session_state.messages.append({"role": "assistant", "content": bot_message})

        with st.chat_message("assistant"):
            st.markdown(bot_message)

        if "box_breathing" in bot_message.lower():
            st.audio("audio/box_breathing.mp3", format="audio/mp3")
        elif  "4-7-8 breathing" in bot_message.lower():
            st.audio("audio/4-7-8_breathing/mp3", format="audio/mp3")
        elif "abdominal breathing" in bot_message.lower():
            st.audio("audio/abdominal_breathing.mp3", format="audip/mp3")
        if "focused meditation" in bot_message.lower():
            st.audio("audio/focused_meditation.mp3", format="audio/mp3")
        elif "progressive relaxation" in bot_message.lower():
            st.audio("audio/progressive_relaxation.mp3", format="audio/mp3")
        elif "mindfulness meditation" in bot_message.lower():
            st.audio("audio/mindfulness_meditation.mp3", format="audio/mp3")