import streamlit as st
from time import sleep
from navigation import make_sidebar, check_user_inactivity  # Import necessary functions

# Check for inactivity and logout if necessary
check_user_inactivity()

# Add sidebar
make_sidebar()

st.title("Welcome to PM-001 β wip 6S")

# Inject JavaScript to focus the input field on the page load globally
st.components.v1.html("""<script>
    const userInput = document.getElementById('user_input');
    if (userInput) {
        userInput.focus();
    }
</script>""", height=0)

st.write("🔒 Please log in to continue.")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Log in", type="primary"):
    if username == "uiltest" and password == "curtistest":
        st.session_state.logged_in = True
        st.success("✔️Logged in successfully!")
        sleep(0.5)
        
        # Instead of using st.switch_page(), use st.experimental_rerun() to reload the page.
        st.switch_page("pages/aws_quiz_st.py") # Store the next page in session state
        # st.experimental_rerun()  # Trigger a rerun to go to the new page
    else:
        st.error("❌Incorrect username or password")
