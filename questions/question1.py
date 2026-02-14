# page1.py
import streamlit as st
import plotly.express as px
import pandas as pd
from utils.translations import get_text, format_number


def show(language='en'):
    st.subheader(get_text(language, 'question1', 'title'))

    # Input fields
    manual_test_execution_time = st.number_input(
        get_text(language, 'question1', 'input_manual'), 
        min_value=0
    )
    automated_test_execution_time_min = st.number_input(
        get_text(language, 'question1', 'input_automated'),
        min_value=0
    )

    # Calculate the hours saved
    automated_test_execution_time = automated_test_execution_time_min / 60
    time_savings_per_run = manual_test_execution_time - automated_test_execution_time

    # Display the result
    if manual_test_execution_time > 0 and automated_test_execution_time > 0:
        formatted_time = format_number(time_savings_per_run, 2, language)
        st.success(get_text(language, 'question1', 'result_message').format(time=formatted_time))

        # Data for the bar chart
        df = pd.DataFrame({
            get_text(language, 'question1', 'chart_type'): [
                get_text(language, 'question1', 'label_manual'),
                get_text(language, 'question1', 'label_automated'),
                get_text(language, 'question1', 'label_saved')
            ],
            get_text(language, 'question1', 'chart_yaxis'): [
                manual_test_execution_time, 
                automated_test_execution_time, 
                time_savings_per_run
            ]
        })

        # Create the bar chart with different colors for each bar
        fig = px.bar(
            df, 
            x=get_text(language, 'question1', 'chart_type'), 
            y=get_text(language, 'question1', 'chart_yaxis'), 
            title=get_text(language, 'question1', 'chart_title'),
            labels={get_text(language, 'question1', 'chart_yaxis'): get_text(language, 'question1', 'chart_yaxis')},
            color=get_text(language, 'question1', 'chart_type'),
            color_discrete_map={
                get_text(language, 'question1', 'label_manual'): 'blue',
                get_text(language, 'question1', 'label_automated'): 'green',
                get_text(language, 'question1', 'label_saved'): 'orange'
            },
            hover_data={get_text(language, 'question1', 'chart_yaxis'): ':.2f'}
        )

        # Display the bar chart in Streamlit
        st.plotly_chart(fig)
