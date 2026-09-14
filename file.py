import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv() 

import random

def matrix_bg(columns: int = 45):
    streaks = "".join(
        f'<span style="left:{i * (100 / columns):.2f}%;'
        f'animation-duration:{random.uniform(1.8, 5.5):.2f}s;'
        f'animation-delay:-{random.uniform(0, 6):.2f}s;'
        f'height:{random.randint(25, 60)}vh;'
        f'opacity:{random.uniform(0.35, 1):.2f};"></span>'
        for i in range(columns)
    )

    st.markdown(
        f"""
        <style>
          html, body {{ background: #000 !important; }}
          .stApp {{ background: transparent !important; }}
          [data-testid="stHeader"] {{ background: transparent !important; }}

          #rain {{
              position: fixed;
              inset: 0;
              overflow: hidden;
              pointer-events: none;
              z-index: 0;
          }}
          #rain span {{
              position: absolute;
              top: 0;
              width: 2px;
              background: linear-gradient(to bottom,
                          rgba(0,255,70,0) 0%,
                          rgba(0,255,70,0.55) 60%,
                          rgba(180,255,200,0.95) 100%);
              animation-name: fall;
              animation-timing-function: linear;
              animation-iteration-count: infinite;
              filter: drop-shadow(0 0 6px rgba(0,255,70,0.8));
          }}
          @keyframes fall {{
              0%   {{ transform: translateY(-100%); }}
              100% {{ transform: translateY(100vh); }}
          }}

          /* lift all Streamlit content above the rain */
          [data-testid="stAppViewContainer"] > .main,
          .stMain, .block-container {{
              position: relative;
              z-index: 1;
          }}
          .stApp, .stApp p, .stApp label, .stApp h1, .stApp h2, .stApp h3 {{
              color: #7CFFB2 !important;
              font-family: "Courier New", monospace !important;
          }}
          .stTextInput input, .stNumberInput input {{
              background: #020d05 !important;
              color: #7CFFB2 !important;
              border: 1px solid #0f0 !important;
              font-family: "Courier New", monospace !important;
          }}
          .stButton button {{
              background: #020d05 !important;
              color: #7CFFB2 !important;
              border: 1px solid #0f0 !important;
              font-family: "Courier New", monospace !important;
          }}
        </style>
        <div id="rain">{streaks}</div>
        """,
        unsafe_allow_html=True,
    )

matrix_bg()

st.title("LAWS90286")

if "people" not in st.session_state:
    st.session_state.people = {}

X = st.text_input("What is your name?")
name = X

age = st.number_input("How old are you?", min_value=0, max_value=120, step=1)

if st.button("Hi"):
    st.session_state.people[name] = age
    st.write("Welcome", name)
    st.write(name, "is", age,"years old")

    if age <= 26:
        st.write("You were born this millennium")
    else:
        st.write("Haha you're old lol blehhhhhhhhh")




client = OpenAI()

response = client.responses.create(
    model="gpt-4o",
    input=f"Write a very brutal and creative roast about a {name} and {age}, give the output in both English and Chinese.",
)

if st.button("Start"):
    response = client.responses.create(
        model="gpt-4o",
        input=f"Write a very brutal and creative roast about a {name} and {age}, give the output in both English and Chinese.",
    )
    with st.container(border=True):
        st.markdown("-----------------")
        st.write(response.output_text)
        st.markdown("-----------------")


lookup = st.text_input("Find age")

if st.button("Find"):
    if lookup in st.session_state.people:
        st.write(lookup, "is", st.session_state.people[lookup], "years old")
    else:
        st.write("No record for", lookup)


