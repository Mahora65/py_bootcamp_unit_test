import streamlit as st
from apps import app_assignment_0, app_assignment_1, app_assignment_2, app_about
from multiapp import MultiApp

multi_app = MultiApp()

st.markdown("""
# Python Bootcamp Grading Mockup

This is application to check you python coding
            """)

multi_app.add_app("Assignment 0", app_assignment_0.app)
multi_app.add_app("Assignment 1", app_assignment_1.app)
multi_app.add_app("Assignment 2", app_assignment_2.app)
multi_app.add_app("About", app_about.app)

multi_app.run()
