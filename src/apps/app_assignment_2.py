import streamlit as st
import os


def app():
    st.title("Assignment 2")

    st.write("Assignment 2 result checker")

    uploaded_file = st.file_uploader("Upload your assignment.py file here", type=['py'])
    if uploaded_file is not None:
        file_details = {"FileName": uploaded_file.name, "FileType": uploaded_file.type, "FileSize": uploaded_file.size}
        st.write(file_details)
