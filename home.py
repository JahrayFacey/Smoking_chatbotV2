import streamlit as st
import requests
from streamlit_lottie import st_lottie
import json

st.set_page_config(page_title="Over the Mountain", page_icon=":tada:", layout="wide")
# def load_lottieurl(url):
#     r = requests.get(url)
#     if r.status_code != 200:
#         return None
#     return r.json
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

lottie_coding = load_lottiefile("assets\No_smoking.json")

with st.container():
    left_column, middle, right_column = st.columns(3, gap="large")
    st.markdown("<h1 style='text-align: center;'> Over The Mountain</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'>A quit smoking AI platform</h2>", unsafe_allow_html=True)
    # with middle:
    #     st.subheader("Over the Mountain")
    #     st.title("A quit smoking platform")
    #     st.title("My name is Paul and my job is to help people quit smoking and enjoy a healthier life")
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2, gap="large")
    with left_column:
        st.header("Our mission")
        st.write("##")
        st.write(
            """
            
            I am here to assit users using the power of AI and methods backed by research to be free from the puff.
            Our mission is to motivate people to live healthier lives and contribute to a society where people feel more freedom.
            We understand the challenges and shame that smoking addiciton can bring. People often feel stuck, tired or hesitant to reach out for help.
            That's why this platform was created. So users can have a 24/7 supportive chatbot that can be used to vent, express feelings
            track their smoking and perform activities. Some things may seem impossible to get done alone, but with our help, we can get you
            over the mountain.

            """
        )
    with right_column:

        st_lottie(
            lottie_coding,
            speed = 1,
            reverse=False,
            loop=True,
            quality="low",
            key=None,
            height=450,
            width=400,
        )


with st.container():
    st.write("---")
    left_column, middle, right = st.columns(3)
    with middle:
        st.markdown(
            """
    <h1 style="text-align: center; margin_top: 0;">
    Try us out now!    <span style='font_size:200px;'>&#8595;</span>
    </h1>
 
            """,
            unsafe_allow_html=True
        )
        # st.header("Try us out now :arrow_down:")
        st.link_button(label="Chat", url=r"/messaging_app.py", type="primary", icon=None, use_container_width=True)
        st.write("##")
    st.markdown("<p style='text-align: center;'>Website and chatbot under development</p>", unsafe_allow_html=True)

    
