import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv() 

st.title("Roast Me Ai")

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

lookup = st.text_input("Find age")

if st.button("Find"):
    if lookup in st.session_state.people:
        st.write(lookup, "is", st.session_state.people[lookup], "years old")
    else:
        st.write("No record for", lookup)




client = OpenAI()

response = client.responses.create(
    model="gpt-4o",
    input=f"Write a good insult about a {name} and {age}.",
)

st.write(response.output_text)
