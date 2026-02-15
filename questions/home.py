# home.py
import streamlit as st
import math
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd
import numpy as np
from datetime import datetime
from utils.translations import get_text, format_number
from utils.persistence import get_value
from utils.pdf_generator import generate_executive_summary
from utils.date_utils import generate_next_6_months


def show(language='en'):
    st.write(get_text(language, 'home', 'instructions'))
    
    st.write("")
    st.write("")
    
    # Add full report export button
    st.subheader(get_text(language, 'pdf', 'executive_summary'))
    
    # Check if any data exists
    has_q1_data = get_value('q1_manual_test_execution_time', 0) > 0 and get_value('q1_automated_test_execution_time_min', 0) > 0
    has_q2_data = get_value('q2_initial_investment', 0) > 0 and get_value('q2_time_savings_per_run', 0) > 0
    has_q3_data = get_value('q3_n', 0) > 0
    
    if not (has_q1_data or has_q2_data or has_q3_data):
        st.info(get_text(language, 'pdf', 'no_data_warning'))
    else:
        if st.button(get_text(language, 'pdf', 'download_full_report'), key='home_full_report'):
            questions_data = {}
            
            # Prepare Question 1 data if available
            if has_q1_data:
                manual_time = get_value('q1_manual_test_execution_time', 0)
                auto_time_min = get_value('q1_automated_test_execution_time_min', 0)
                auto_time = auto_time_min / 60
                time_savings = manual_time - auto_time
                
                # Recreate Q1 chart
                df = pd.DataFrame({
                    get_text(language, 'question1', 'chart_type'): [
                        get_text(language, 'question1', 'label_manual'),
                        get_text(language, 'question1', 'label_automated'),
                        get_text(language, 'question1', 'label_saved')
                    ],
                    get_text(language, 'question1', 'chart_yaxis'): [
                        manual_time, 
                        auto_time, 
                        time_savings
                    ]
                })
                
                fig1 = px.bar(
                    df, 
                    x=get_text(language, 'question1', 'chart_type'), 
                    y=get_text(language, 'question1', 'chart_yaxis'), 
                    title=get_text(language, 'question1', 'chart_title'),
                    color=get_text(language, 'question1', 'chart_type'),
                    color_discrete_map={
                        get_text(language, 'question1', 'label_manual'): 'blue',
                        get_text(language, 'question1', 'label_automated'): 'green',
                        get_text(language, 'question1', 'label_saved'): 'orange'
                    }
                )
                
                questions_data['q1'] = {
                    'inputs': {
                        'manual_time': manual_time,
                        'automated_time_min': auto_time_min
                    },
                    'results': {
                        'time_savings': time_savings,
                        'formatted_savings': format_number(time_savings, 2, language)
                    },
                    'chart': fig1
                }
            
            # Prepare Question 2 data if available
            if has_q2_data:
                investment = get_value('q2_initial_investment', 0)
                savings_per_run = get_value('q2_time_savings_per_run', 0)
                runs_to_break_even = math.ceil(investment / savings_per_run) if savings_per_run != 0 else float('inf')
                
                # Recreate Q2 chart
                if savings_per_run > 0:
                    runs = np.arange(0, int(runs_to_break_even) + 10, 1)
                    cumulative_savings = runs * savings_per_run
                    
                    fig2 = go.Figure()
                    hover_template = (
                        f"{get_text(language, 'question2', 'hover_runs')}: %{{x}}<br>"
                        f"{get_text(language, 'question2', 'hover_savings')}: %{{y:.2f}} "
                        f"{get_text(language, 'question1', 'chart_yaxis').split('(')[1].replace(')', '')}"
                        "<extra></extra>"
                    )
                    
                    fig2.add_trace(go.Scatter(
                        x=runs, y=cumulative_savings,
                        mode='lines+markers',
                        name=get_text(language, 'question2', 'chart_trace'),
                        hovertemplate=hover_template,
                    ))
                    
                    fig2.add_hline(
                        y=investment, 
                        line_dash="dash", 
                        line_color="red", 
                        annotation_text=get_text(language, 'question2', 'chart_annotation'),
                        annotation_position="top right"
                    )
                    
                    fig2.update_layout(
                        title=get_text(language, 'question2', 'chart_title'),
                        xaxis_title=get_text(language, 'question2', 'chart_xaxis'),
                        yaxis_title=get_text(language, 'question2', 'chart_yaxis'),
                        legend=dict(yanchor="top", y=0.99, xanchor="right", x=0.99)
                    )
                    
                    questions_data['q2'] = {
                        'inputs': {
                            'initial_investment': investment,
                            'time_savings': savings_per_run
                        },
                        'results': {
                            'runs_to_break_even': runs_to_break_even
                        },
                        'chart': fig2
                    }
            
            # Prepare Question 3 data if available
            if has_q3_data:
                TH = get_value('q3_th', 0)
                MT = get_value('q3_mt', 0)
                N = get_value('q3_n', 0)
                A = get_value('q3_a', 0)
                
                # Recreate Q3 calculations
                potential_array = []
                MAINTENANCE_HOURS_NEW = MT
                for i in range(1, 7):
                    MAINTENANCE_HOURS_NEW += (MT / N) * A
                    potential_array.append(TH - MAINTENANCE_HOURS_NEW)
                
                can_afford = potential_array[0] > 0 if potential_array else False
                
                # Recreate Q3 chart
                fig3, ax = plt.subplots()
                months = generate_next_6_months(language)
                ax.plot(months, potential_array, marker='o')
                ax.axhline(0, color='red', linestyle='--', linewidth=0.5)
                ax.set_xlabel(get_text(language, 'question3', 'chart_xaxis'))
                ax.set_ylabel(get_text(language, 'question3', 'chart_yaxis'))
                ax.grid(True)
                
                questions_data['q3'] = {
                    'inputs': {
                        'TH': TH,
                        'MT': MT,
                        'N': N,
                        'A': A
                    },
                    'results': {
                        'potential_array': potential_array,
                        'can_afford': can_afford
                    },
                    'chart': fig3
                }
            
            # Generate comprehensive PDF
            pdf_buffer = generate_executive_summary(language, questions_data)
            
            # Create download button
            filename = f"test_automation_executive_summary_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
            st.download_button(
                label=get_text(language, 'pdf', 'download_full_report'),
                data=pdf_buffer,
                file_name=filename,
                mime='application/pdf',
                key='home_download_full_pdf'
            )
