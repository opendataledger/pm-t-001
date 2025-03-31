import streamlit as st
from time import sleep
from navigation import make_sidebar, check_user_inactivity  # Import necessary functions

# Check for inactivity and logout if necessary
check_user_inactivity()

# Add sidebar
make_sidebar()

st.title("Welcome to PM Beta Test")

# Inject JavaScript to focus the input field on the page load globally
st.components.v1.html("""
    <script>
        // Check if the element with id 'user_input' exists and set focus
        const userInput = document.getElementById('user_input');
        if (userInput) {
            userInput.focus();
        }
    </script>
""", height=0)

st.write("🔒 Please log in to continue.")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Log in", type="primary"):
    if username == "uiltest" and password == "cheathamtest":
        st.session_state.logged_in = True
        st.success("✔️Logged in successfully!")
        sleep(0.5)
        st.switch_page("app.py")
    else:
        st.error("❌Incorrect username or password")
