import streamlit as st
import time
from time import sleep
from streamlit.runtime.scriptrunner import get_script_run_ctx
from streamlit.source_util import get_pages


def get_current_page_name():
    ctx = get_script_run_ctx()
    if ctx is None:
        raise RuntimeError("Couldn't get script context")

    pages = get_pages("")

    return pages[ctx.page_script_hash]["page_name"]


def make_sidebar():
    with st.sidebar:
        st.title("⚡ PM β")
        st.write("")
        st.write("")

        if st.session_state.get("logged_in", False):
            st.page_link("pages/page1.py", label="5th-6th Grade - 📝List of Words", icon="🔹")
            st.page_link("pages/page2.py", label="5th-6th Grade - 👍Selected Spelling Game", icon="🔸")
            st.page_link("pages/page3.py", label="3rd-4th Grade - 📝List of Words", icon="🔹")
            st.page_link("pages/page4.py", label="5th-6th Grade - 👍Full Spelling Game", icon="🔸")
            

            st.write("")
            st.write("")

            if st.button("Log out"):
                logout()

        elif get_current_page_name() != "streamlit_app":
            # If anyone tries to access a secret page without being logged in,
            # redirect them to the login page
            st.switch_page("streamlit_app.py")

# BELOW ADD

# Function to check user inactivity and automatically log out after 15 minutes
def check_user_inactivity():
    inactivity_limit = 15 * 60  # 15 minutes in seconds
    current_time = time.time()

    # Track last activity time
    if 'last_activity_time' not in st.session_state:
        st.session_state.last_activity_time = current_time

    # Calculate inactivity time
    inactivity_time = current_time - st.session_state.last_activity_time

    # If the user is inactive for too long, log them out
    if inactivity_time > inactivity_limit:
        st.session_state.clear()  # Clear session state to log the user out
        st.write("You have been logged out due to inactivity.")
        st.experimental_rerun()  # Rerun the app to reset the session

    # Update the last activity time
    st.session_state.last_activity_time = current_time   

# ABOVE ADD

def logout():
    st.session_state.logged_in = False
    st.info("✔️Logged out successfully!")
    sleep(0.5)
    st.switch_page("streamlit_app.py")
