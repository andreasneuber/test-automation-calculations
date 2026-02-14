# page3.py
import streamlit as st
import matplotlib.pyplot as plt
from utils.date_utils import generate_next_6_months
from utils.translations import get_text

def show(language='en'):
    st.subheader(get_text(language, 'question3', 'title'))

    # Input fields
    TH = st.number_input(get_text(language, 'question3', 'input_th'), min_value=0)
    MT = st.number_input(get_text(language, 'question3', 'input_mt'), min_value=0)
    N = st.number_input(get_text(language, 'question3', 'input_n'), min_value=0)
    A = st.number_input(get_text(language, 'question3', 'input_a'), min_value=0)

    # Calculate the potential to add more tests (P)
    potential_tests_array = []

    if N > 0:

        P = []
        MAINTENANCE_HOURS_NEW = MT
        for i in range(1, 7):
            MAINTENANCE_HOURS_NEW += (MT / N) * A
            P.append(TH - MAINTENANCE_HOURS_NEW)

        for i, p in enumerate(P, 1):
            potential_tests_array.append(p)

        # Interpretation
        st.text("")
        st.text("")

        if isinstance(potential_tests_array[0], (int, float)) and potential_tests_array[0] <= 0:
            st.warning(get_text(language, 'question3', 'warning_message'))
        elif isinstance(potential_tests_array[0], (int, float)) and potential_tests_array[0] > 0:
            st.success(get_text(language, 'question3', 'success_message').format(count=int(A)))

        # Plot the trend
        fig, ax = plt.subplots()
        months = generate_next_6_months(language)
        ax.plot(months, potential_tests_array, marker='o')
        ax.axhline(0, color='red', linestyle='--', linewidth=0.5)
        ax.set_xlabel(get_text(language, 'question3', 'chart_xaxis'))
        ax.set_ylabel(get_text(language, 'question3', 'chart_yaxis'))
        ax.grid(True)

        # Display the chart
        st.text("")
        st.text("")
        st.text("")
        st.pyplot(fig)

    else:
        st.text("")
