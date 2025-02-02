# page3.py
import streamlit as st
import matplotlib.pyplot as plt
from utils.date_utils import generate_next_6_months

def show():
    st.subheader('Can the team "afford" the maintenance of [n] more automated tests?')

    # Input fields
    TH = st.number_input('Monthly hours available for maintenance tasks (TH):', min_value=0)
    MT = st.number_input('Monthly hours currently used to maintain existing automated tests (MT):', min_value=0)
    N = st.number_input('Total count of all current automated tests (N):', min_value=0)
    A = st.number_input('Count of new automated tests to be added next month (A):', min_value=0)

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
            st.warning('Adding more tests will lead to decay of the automation test suite.')
        elif isinstance(potential_tests_array[0], (int, float)) and potential_tests_array[0] > 0:
            st.success(f'You can afford to add and maintain {A} more automated tests next month.')

        # Plot the trend
        fig, ax = plt.subplots()
        months = generate_next_6_months()
        ax.plot(months, potential_tests_array, marker='o')
        ax.axhline(0, color='red', linestyle='--', linewidth=0.5)
        ax.set_xlabel('Months')
        ax.set_ylabel('Potential to add more tests (P)')
        ax.grid(True)

        # Display the chart
        st.text("")
        st.text("")
        st.text("")
        st.markdown(f"##### 6-Month Prediction of Potential (P) for Adding {A} More Tests Each Month")
        st.pyplot(fig)

    else:
        st.text("")
