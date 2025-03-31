import os
import streamlit as st


st.title("Github Action Test")
st.write("This is a text")

with open(os.getenv("SECRET_NAME_FILE")) as f:
    st.markdown(f.read())


st.write("Okay wow now on the other vps")


st.info(f"This comes straight from github secret: {os.getenv("GITHUB_SECRET")}")