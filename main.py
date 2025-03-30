import os
import streamlit as st


st.title("Github Action Test")
st.write("This is a text")

st.markdown(os.getenv("SECRET_NAME"))
