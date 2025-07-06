# page1.py
import streamlit as st
import plotly.express as px
import pandas as pd


def show():
    st.subheader('How many work hours can be saved by automating the test suite?')

    # Input fields
    manual_test_execution_time = st.number_input('Manual Test Run Time of Test Suite (in hours):', min_value=0)
    automated_test_execution_time_min = st.number_input('Automated Test Run Time of Test Suite (in minutes):',
                                                        min_value=0)

    # Calculate the hours saved
    automated_test_execution_time = automated_test_execution_time_min / 60
    time_savings_per_run = manual_test_execution_time - automated_test_execution_time

    # Display the result
    if manual_test_execution_time > 0 and automated_test_execution_time > 0:
        st.success(f'Each automated test run will save you about {time_savings_per_run:.2f} hours.')

        # Data for the bar chart
        df = pd.DataFrame({
            'Type': ['Manual', 'Automated', 'Time Saved'],
            'Time (hours)': [manual_test_execution_time, automated_test_execution_time, time_savings_per_run]
        })

        # Create the bar chart with different colors for each bar
        fig = px.bar(df, x='Type', y='Time (hours)', title='Time Comparison: Manual vs Automated Test Suite',
                     labels={'Time (hours)': 'Time (hours)'},
                     color='Type',
                     color_discrete_map={
                         'Manual': 'blue',
                         'Automated': 'green',
                         'Time Saved': 'orange'
                     },
                     hover_data={'Time (hours)': ':.2f'})

        # Display the bar chart in Streamlit
        st.plotly_chart(fig)
