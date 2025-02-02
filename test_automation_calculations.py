import streamlit as st
from questions import home
from questions import question1
from questions import question2
from questions import question3

# Set the layout to wide
# st.set_page_config(layout="wide")

# Title of the app
st.title('Test Automation Calculations')

page_dict = {
    "Home": "home",
    "How many work hours can be saved by automating the test suite?": "question1",
    "How many test runs are needed to counter-balance the initial investment for automating a test suite?": "question2",
    "Can the team 'afford' the maintenance of [n] more automated tests?": "question3",
}

st.sidebar.title("Navigation")
selected_label = st.sidebar.radio("Go to", list(page_dict.keys()))

if page_dict[selected_label] == "home":
    home.show()
elif page_dict[selected_label] == "question1":
    question1.show()
elif page_dict[selected_label] == "question2":
    question2.show()
elif page_dict[selected_label] == "question3":
    question3.show()
