import math
import streamlit as st
import matplotlib.pyplot as plt
import plotly.graph_objs as go
import plotly.express as px
import numpy as np
from utils.date_utils import generate_next_6_months

# Set the layout to wide
# st.set_page_config(layout="wide")

# Title of the app
st.title('Test Automation Calculations')

st.subheader('How many work hours can be saved by automating the test suite?')

# Input fields
manual_test_execution_time = st.number_input('Manual Test Run Time of Test Suite (in hours):', min_value=0)
automated_test_execution_time_min = st.number_input('Automated Test Run Time of Test Suite (in minutes):', min_value=0)

# Calculate the hours saved
automated_test_execution_time = automated_test_execution_time_min / 60
time_savings_per_run = manual_test_execution_time - automated_test_execution_time

# Display the result
if manual_test_execution_time > 0 and automated_test_execution_time > 0:
    st.success(f'Each automated test run will save you about {time_savings_per_run:.2f} hours.')

    # Data for the bar chart
    data = {
        'Type': ['Manual', 'Automated', 'Time Saved'],
        'Time (hours)': [manual_test_execution_time, automated_test_execution_time, time_savings_per_run]
    }

    # Create the bar chart with different colors for each bar
    fig = px.bar(data, x='Type', y='Time (hours)', title='Time Comparison: Manual vs Automated Test Suite',
                 labels={'Time (hours)': 'Time (hours)'},
                 color='Type', color_discrete_map={
            'Manual': 'blue',
            'Automated': 'green',
            'Time Saved': 'orange'
        })

    # Display the bar chart in Streamlit
    st.plotly_chart(fig)

st.markdown("---")

#################################################################################################
st.subheader('How many test runs are needed to counter-balance the initial investment for automating a test suite?')

# Input variables
initial_investment = st.number_input('Initial investment for automation (in hours)', min_value=0)
time_savings_per_run = st.number_input('Time savings per run (in hours)', min_value=0)

# Calculate the number of runs to break even
if time_savings_per_run != 0:
    runs_to_break_even = math.ceil(initial_investment / time_savings_per_run)
    st.success(f'Number of test runs needed to counter-balance the initial investment: {runs_to_break_even}')
else:
    runs_to_break_even = float('inf')

if initial_investment > 0 and time_savings_per_run > 0:
    # Create the data for the graph
    runs = np.arange(0, int(runs_to_break_even) + 10, 1)
    cumulative_savings = runs * time_savings_per_run

    # Create the Plotly figure
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=runs, y=cumulative_savings,
        mode='lines+markers',
        name='Cumulative Time Savings',
        hovertemplate='Number of Runs: %{x}<br>Time Savings: %{y:.2f} hours<extra></extra>',
    ))

    fig.add_hline(y=initial_investment, line_dash="dash", line_color="red", annotation_text="Initial Investment",
                  annotation_position="top right")

    fig.update_layout(
        title='Reaching Break-even Point for Automated Test Suite',
        xaxis_title='Number of Test Runs',
        yaxis_title='Cumulative Time Savings (hours)',
        legend=dict(yanchor="top", y=0.99, xanchor="right", x=0.99)
    )

    # Display the Plotly figure in Streamlit
    st.plotly_chart(fig)

st.markdown("---")

#################################################################################################
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

    # Optionally, display the array
    st.write(f'Array data used for plot: {potential_tests_array}')
else:
    st.text("")
