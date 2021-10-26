import streamlit as st
from util.file_manager import save_file
from util.unit_test_manager import call_unit_test
from test.test_assignment_0 import TestAssignment0


def app():

    st.title("Assignment 0")
    
    st.write("Assignment 0 result checker")

    uploaded_file = st.file_uploader("upload your code here", type= ['py'])
    if uploaded_file is not None:
        file_details = {"FileName": uploaded_file.name, "FileType": uploaded_file.type, "FileSize": uploaded_file.size}
        save_file(uploaded_file, 'tmp/assignment_0.py')
        st.success(f"Successfully uploaded {file_details['FileName']}. Type: {file_details['FileType']}. Size: {file_details['FileSize']}.")

    if st.button("Check your assignment"):
        test_run, errors, failures, test_output = call_unit_test(TestAssignment0)
        if errors or failures:
            st.error(f"The assignment has {len(errors)} errors and {len(failures)} failures.")
            if errors:
                st.subheader('Errors')
                for e in errors:
                    st.write(e[0])
                    st.code(e[1])
                    st.markdown("***")
            if failures:
                st.subheader("Failures")
                for f in failures:
                    st.write(f[0])
                    st.code(f[1])
        else:
            st.success('The assignment pass the unittest')
