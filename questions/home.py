# home.py
import streamlit as st
from utils.translations import get_text

def show(language='en'):
    st.write(get_text(language, 'home', 'instructions'))