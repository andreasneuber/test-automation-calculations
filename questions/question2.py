# page2.py
import math
import streamlit as st
import plotly.graph_objs as go
import numpy as np
from utils.translations import get_text
from utils.persistence import get_value, update_value

def show(language='en'):
    st.subheader(get_text(language, 'question2', 'title'))

    # Input variables with file persistence
    initial_investment = st.number_input(
        get_text(language, 'question2', 'input_investment'), 
        min_value=0,
        value=get_value('q2_initial_investment', 0),
        step=1,
        on_change=lambda: update_value('q2_initial_investment', st.session_state.q2_invest_input),
        key='q2_invest_input'
    )
    time_savings_per_run = st.number_input(
        get_text(language, 'question2', 'input_savings'), 
        min_value=0,
        value=get_value('q2_time_savings_per_run', 0),
        step=1,
        on_change=lambda: update_value('q2_time_savings_per_run', st.session_state.q2_savings_input),
        key='q2_savings_input'
    )

    # Calculate the number of runs to break even
    if time_savings_per_run != 0:
        runs_to_break_even = math.ceil(initial_investment / time_savings_per_run)
        st.success(get_text(language, 'question2', 'result_message').format(runs=runs_to_break_even))
    else:
        runs_to_break_even = float('inf')

    if initial_investment > 0 and time_savings_per_run > 0:
        # Create the data for the graph
        runs = np.arange(0, int(runs_to_break_even) + 10, 1)
        cumulative_savings = runs * time_savings_per_run

        # Create the Plotly figure
        fig = go.Figure()

        # Build hover template with translated labels
        hover_template = (
            f"{get_text(language, 'question2', 'hover_runs')}: %{{x}}<br>"
            f"{get_text(language, 'question2', 'hover_savings')}: %{{y:.2f}} "
            f"{get_text(language, 'question1', 'chart_yaxis').split('(')[1].replace(')', '')}"
            "<extra></extra>"
        )

        fig.add_trace(go.Scatter(
            x=runs, y=cumulative_savings,
            mode='lines+markers',
            name=get_text(language, 'question2', 'chart_trace'),
            hovertemplate=hover_template,
        ))

        fig.add_hline(
            y=initial_investment, 
            line_dash="dash", 
            line_color="red", 
            annotation_text=get_text(language, 'question2', 'chart_annotation'),
            annotation_position="top right"
        )

        fig.update_layout(
            title=get_text(language, 'question2', 'chart_title'),
            xaxis_title=get_text(language, 'question2', 'chart_xaxis'),
            yaxis_title=get_text(language, 'question2', 'chart_yaxis'),
            legend=dict(yanchor="top", y=0.99, xanchor="right", x=0.99)
        )

        # Display the Plotly figure in Streamlit
        st.plotly_chart(fig)
