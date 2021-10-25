import streamlit as st
from multiapp import MultiApp
from apps import app_assignment_0, app_assignment_1, app_assignment_2, app_about

app = MultiApp()

st.markdown("""
# Python Bootcamp Grading Mockup

This is application to check you python coding
            """)

app.add_app("Assignment 0", app_assignment_0.app)
app.add_app("Assignment 1", app_assignment_1.app)
app.add_app("Assignment 2", app_assignment_2.app)
app.add_app("About", app_about.app)

app.run()