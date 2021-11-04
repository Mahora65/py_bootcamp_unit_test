import streamlit as st
from util.file_manager import save_file
from util.unit_test_manager import call_unit_test
from importlib import import_module
from shutil import copyfile


class BaseApp():
    def __init__(self, assignment_number, database=None) -> None:
        self.assignment_number = assignment_number
        self.title = f"Assignment {self.assignment_number}"
        self.test_name = f"test.test_assignment_{assignment_number}"
        self.test_class_name = f"TestAssignment{self.assignment_number}"
        self.database= database

    def write_headers(self):
        st.title(self.title)
        st.write(f"{self.title} results checker")

    @staticmethod
    def write_file_uploader(assignment_number):
        uploaded_file = st.file_uploader("upload your code here", type=['py'])
        if uploaded_file is not None:
            file_details = {"FileName": uploaded_file.name, "FileType": uploaded_file.type,
                            "FileSize": uploaded_file.size}
            save_file(uploaded_file, f'tmp/assignment_{assignment_number}.py')
            st.success(
                f"Successfully uploaded {file_details['FileName']}. Type: {file_details['FileType']}"
                f". Size: {file_details['FileSize']}.")

    def import_test(self):
        """ 
        Import a named object from a module in the context of this function.
        """
        try:
            self.test_class = getattr(import_module(self.test_name), self.test_class_name)
        except ImportError:
            return None

    def check_assignment(self):
        if st.button("Check your assignment"):
            test_run, errors, failures, test_output = call_unit_test(self.test_class)
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

    def load_databases(self):
        copyfile(f"db/{self.database}", self.database)

    def run_app(self):
        if self.database: self.load_databases()
        self.import_test()
        self.write_headers()
        self.write_file_uploader(self.assignment_number)
        self.check_assignment()
