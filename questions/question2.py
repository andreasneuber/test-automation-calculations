# page2.py
import math
import streamlit as st
import plotly.graph_objs as go
import numpy as np

def show():
    st.subheader('How many test runs are needed to counter-balance the initial time investment for automating a test suite?')

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
