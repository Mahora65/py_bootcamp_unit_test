import streamlit as st


class MultiApp:
    """Framework for create multi-pages applications.add()
    Usage:
        def foo():
            st.title("Hello Foo")
        def bar():
            st.title("Hello Bar")
        
        app = MultiApp()
        app.add_app("Foo", foo)
        app.add_app("Bar", bar)
        app.run()
    """

    def __init__(self):
        self.apps = []

    def add_app(self, title, app):
        """Adds new app page 

        Args:
            title (str): title of the page
            app (func): the python function to render the page
        """

        self.apps.append({
            "title": title,
            "function": app
        })

    def run(self):
        """Run the application
        """
        app = st.selectbox(
            'Assignment',
            self.apps,
            format_func=lambda app: app['title']
            # format_func=lambda app: app['title']
        )
        print(app)
        app['function']()
