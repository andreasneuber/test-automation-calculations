import streamlit as st
from questions import home, question1, question2, question3
from utils.translations import get_text


# Set the layout to wide
# st.set_page_config(layout="wide")

# Initialize language in session state
if 'language' not in st.session_state:
    st.session_state.language = 'en'

# Language selector in sidebar
language_options = {'English': 'en', 'Deutsch': 'de', 'Français': 'fr', 'Lëtzebuergesch': 'lb'}
selected_language_label = st.sidebar.selectbox(
    get_text(st.session_state.language, 'main', 'language_label'),
    options=list(language_options.keys()),
    index=list(language_options.values()).index(st.session_state.language)
)
st.session_state.language = language_options[selected_language_label]

# Get current language
lang = st.session_state.language

# Title of the app
st.title(get_text(lang, 'main', 'app_title'))

# Page dictionary with stable keys mapped to translated labels
page_dict = {
    get_text(lang, 'main', 'nav_home'): "home",
    get_text(lang, 'main', 'nav_q1'): "question1",
    get_text(lang, 'main', 'nav_q2'): "question2",
    get_text(lang, 'main', 'nav_q3'): "question3",
}

st.sidebar.title(get_text(lang, 'main', 'sidebar_title'))
selected_label = st.sidebar.radio(get_text(lang, 'main', 'nav_label'), list(page_dict.keys()))

if page_dict[selected_label] == "home":
    home.show(lang)
elif page_dict[selected_label] == "question1":
    question1.show(lang)
elif page_dict[selected_label] == "question2":
    question2.show(lang)
elif page_dict[selected_label] == "question3":
    question3.show(lang)
