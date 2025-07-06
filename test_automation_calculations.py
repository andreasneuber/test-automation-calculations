import streamlit as st
from questions import home, question1, question2, question3


# Set the layout to wide
# st.set_page_config(layout="wide")

# Title of the app
st.title('Test Automation Calculations')

page_dict = {
    "HOME": "home",
    "1\\) How many work hours can be saved by automating the test suite?": "question1",
    "2\\) How many test runs are needed to counter-balance the initial time investment for automating a test suite?": "question2",
    "3\\) Can the team 'afford' the maintenance of [n] more automated tests?": "question3",
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
