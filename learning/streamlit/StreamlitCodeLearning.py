import pandas as pd
import streamlit as st

st.title("Title of screen - QA UKP")
st.header("Welcome to Streamlit  - Header")
st.subheader("Streamlit  - Sub-Header")
st.write("Hello world, this is my first Streamlit code...!")
st.text("This is text values")

# Button
if st.button("Click here...!"):
    st.write("Button clicked , please wait")

agree = st.checkbox("I Agree.")
if agree:
    st.write("You agreed")


level = st.slider("Enter Level",1,10)
st.write(f"Selected Value of level is : {level}")

uploaded_file = st.file_uploader("Upload a file",type=["csv","txt","pdf"])


# st.help("Help")