# pdf_generator.py
"""
PDF generation module for Test Automation Calculations
Generates executive summary reports with charts and results
"""

from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak, Table, TableStyle
from reportlab.lib import colors
from io import BytesIO
from datetime import datetime
import tempfile
import os

from utils.translations import get_text, format_number


def _convert_plotly_to_image(fig, width=6, height=4):
    """
    Convert a Plotly figure to an image BytesIO object
    
    Args:
        fig: Plotly figure object
        width: Width in inches
        height: Height in inches
        
    Returns:
        BytesIO object containing the image
    """
    try:
        # Create a temporary file for the image
        with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as tmp_file:
            tmp_path = tmp_file.name
        
        # Export plotly figure to image file
        fig.write_image(tmp_path, width=width*100, height=height*100)
        
        # Read the image into BytesIO
        with open(tmp_path, 'rb') as f:
            img_bytes = BytesIO(f.read())
        
        # Clean up temp file
        os.unlink(tmp_path)
        
        return img_bytes
    except Exception as e:
        print(f"Error converting Plotly figure: {e}")
        return None


def _convert_matplotlib_to_image(fig, width=6, height=4):
    """
    Convert a Matplotlib figure to an image BytesIO object
    
    Args:
        fig: Matplotlib figure object
        width: Width in inches
        height: Height in inches
        
    Returns:
        BytesIO object containing the image
    """
    try:
        img_bytes = BytesIO()
        fig.set_size_inches(width, height)
        fig.savefig(img_bytes, format='png', dpi=100, bbox_inches='tight')
        img_bytes.seek(0)
        return img_bytes
    except Exception as e:
        print(f"Error converting Matplotlib figure: {e}")
        return None


def generate_executive_summary(language, questions_data, output_path=None):
    """
    Generate a comprehensive executive summary PDF report
    
    Args:
        language (str): Language code ('en', 'de', 'fr', 'lb')
        questions_data (dict): Dictionary containing data for each question
            {
                'q1': {
                    'inputs': {'manual_time': float, 'automated_time_min': float},
                    'results': {'time_savings': float, 'formatted_savings': str},
                    'chart': plotly_figure or None
                },
                'q2': {
                    'inputs': {'initial_investment': float, 'time_savings': float},
                    'results': {'runs_to_break_even': int},
                    'chart': plotly_figure or None
                },
                'q3': {
                    'inputs': {'TH': float, 'MT': float, 'N': int, 'A': int},
                    'results': {'potential_array': list, 'can_afford': bool},
                    'chart': matplotlib_figure or None
                }
            }
        output_path (str): Optional file path to save PDF. If None, returns BytesIO
        
    Returns:
        BytesIO object containing the PDF (if output_path is None)
    """
    # Create PDF buffer
    if output_path:
        buffer = output_path
    else:
        buffer = BytesIO()
    
    # Create PDF document
    doc = SimpleDocTemplate(buffer, pagesize=letter,
                           topMargin=0.75*inch, bottomMargin=0.75*inch,
                           leftMargin=0.75*inch, rightMargin=0.75*inch)
    
    # Container for PDF elements
    elements = []
    
    # Define styles
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#1f77b4'),
        spaceAfter=30,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=16,
        textColor=colors.HexColor('#2c3e50'),
        spaceAfter=12,
        spaceBefore=12,
        fontName='Helvetica-Bold'
    )
    
    subheading_style = ParagraphStyle(
        'CustomSubHeading',
        parent=styles['Heading3'],
        fontSize=12,
        textColor=colors.HexColor('#34495e'),
        spaceAfter=8,
        spaceBefore=8,
        fontName='Helvetica-Bold'
    )
    
    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['BodyText'],
        fontSize=11,
        alignment=TA_JUSTIFY,
        spaceAfter=12
    )
    
    # Add title
    title = Paragraph(get_text(language, 'pdf', 'title'), title_style)
    elements.append(title)
    
    # Add generation date
    date_text = f"{get_text(language, 'pdf', 'generated_date')} {datetime.now().strftime('%Y-%m-%d %H:%M')}"
    date_para = Paragraph(date_text, ParagraphStyle('DateStyle', parent=styles['Normal'], 
                                                     fontSize=10, textColor=colors.grey, 
                                                     alignment=TA_CENTER))
    elements.append(date_para)
    elements.append(Spacer(1, 0.3*inch))
    
    # Add executive summary section
    exec_summary_title = Paragraph(get_text(language, 'pdf', 'executive_summary'), heading_style)
    elements.append(exec_summary_title)
    
    summary_intro = Paragraph(get_text(language, 'pdf', 'summary_intro'), body_style)
    elements.append(summary_intro)
    elements.append(Spacer(1, 0.2*inch))
    
    # Process Question 1 if data exists
    if 'q1' in questions_data and questions_data['q1']:
        q1_data = questions_data['q1']
        
        # Question 1 heading
        q1_title = Paragraph(f"1. {get_text(language, 'pdf', 'q1_summary_label')}", subheading_style)
        elements.append(q1_title)
        
        # Inputs table
        inputs_label = Paragraph(f"<b>{get_text(language, 'pdf', 'inputs_label')}:</b>", body_style)
        elements.append(inputs_label)
        
        if 'inputs' in q1_data:
            manual_time = q1_data['inputs'].get('manual_time', 0)
            auto_time = q1_data['inputs'].get('automated_time_min', 0)
            
            input_data = [
                [get_text(language, 'question1', 'input_manual'), 
                 f"{format_number(manual_time, 1, language)} {get_text(language, 'question1', 'chart_yaxis').split('(')[1].replace(')', '')}"],
                [get_text(language, 'question1', 'input_automated'), 
                 f"{format_number(auto_time, 0, language)} min"]
            ]
            
            input_table = Table(input_data, colWidths=[4*inch, 2*inch])
            input_table.setStyle(TableStyle([
                ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
                ('FONTSIZE', (0, 0), (-1, -1), 10),
                ('TEXTCOLOR', (0, 0), (0, -1), colors.HexColor('#34495e')),
                ('ALIGN', (1, 0), (1, -1), 'RIGHT'),
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
            ]))
            elements.append(input_table)
            elements.append(Spacer(1, 0.1*inch))
        
        # Results
        if 'results' in q1_data:
            results_label = Paragraph(f"<b>{get_text(language, 'pdf', 'results_label')}:</b>", body_style)
            elements.append(results_label)
            
            time_savings = q1_data['results'].get('time_savings', 0)
            result_text = get_text(language, 'question1', 'result_message').format(
                time=format_number(time_savings, 2, language)
            )
            result_para = Paragraph(result_text, body_style)
            elements.append(result_para)
        
        # Add chart if available
        if 'chart' in q1_data and q1_data['chart']:
            elements.append(Spacer(1, 0.1*inch))
            img_bytes = _convert_plotly_to_image(q1_data['chart'])
            if img_bytes:
                img = Image(img_bytes, width=5*inch, height=3.5*inch)
                elements.append(img)
        
        elements.append(Spacer(1, 0.2*inch))
    
    # Process Question 2 if data exists
    if 'q2' in questions_data and questions_data['q2']:
        q2_data = questions_data['q2']
        
        # Question 2 heading
        q2_title = Paragraph(f"2. {get_text(language, 'pdf', 'q2_summary_label')}", subheading_style)
        elements.append(q2_title)
        
        # Inputs table
        inputs_label = Paragraph(f"<b>{get_text(language, 'pdf', 'inputs_label')}:</b>", body_style)
        elements.append(inputs_label)
        
        if 'inputs' in q2_data:
            investment = q2_data['inputs'].get('initial_investment', 0)
            savings = q2_data['inputs'].get('time_savings', 0)
            
            input_data = [
                [get_text(language, 'question2', 'input_investment'), 
                 f"{format_number(investment, 1, language)} h"],
                [get_text(language, 'question2', 'input_savings'), 
                 f"{format_number(savings, 2, language)} h"]
            ]
            
            input_table = Table(input_data, colWidths=[4*inch, 2*inch])
            input_table.setStyle(TableStyle([
                ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
                ('FONTSIZE', (0, 0), (-1, -1), 10),
                ('TEXTCOLOR', (0, 0), (0, -1), colors.HexColor('#34495e')),
                ('ALIGN', (1, 0), (1, -1), 'RIGHT'),
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
            ]))
            elements.append(input_table)
            elements.append(Spacer(1, 0.1*inch))
        
        # Results
        if 'results' in q2_data:
            results_label = Paragraph(f"<b>{get_text(language, 'pdf', 'results_label')}:</b>", body_style)
            elements.append(results_label)
            
            runs = q2_data['results'].get('runs_to_break_even', 0)
            result_text = get_text(language, 'question2', 'result_message').format(runs=runs)
            result_para = Paragraph(result_text, body_style)
            elements.append(result_para)
        
        # Add chart if available
        if 'chart' in q2_data and q2_data['chart']:
            elements.append(Spacer(1, 0.1*inch))
            img_bytes = _convert_plotly_to_image(q2_data['chart'])
            if img_bytes:
                img = Image(img_bytes, width=5*inch, height=3.5*inch)
                elements.append(img)
        
        elements.append(Spacer(1, 0.2*inch))
    
    # Process Question 3 if data exists
    if 'q3' in questions_data and questions_data['q3']:
        q3_data = questions_data['q3']
        
        # Question 3 heading
        q3_title = Paragraph(f"3. {get_text(language, 'pdf', 'q3_summary_label')}", subheading_style)
        elements.append(q3_title)
        
        # Inputs table
        inputs_label = Paragraph(f"<b>{get_text(language, 'pdf', 'inputs_label')}:</b>", body_style)
        elements.append(inputs_label)
        
        if 'inputs' in q3_data:
            TH = q3_data['inputs'].get('TH', 0)
            MT = q3_data['inputs'].get('MT', 0)
            N = q3_data['inputs'].get('N', 0)
            A = q3_data['inputs'].get('A', 0)
            
            input_data = [
                [get_text(language, 'question3', 'input_th'), format_number(TH, 0, language)],
                [get_text(language, 'question3', 'input_mt'), format_number(MT, 0, language)],
                [get_text(language, 'question3', 'input_n'), format_number(N, 0, language)],
                [get_text(language, 'question3', 'input_a'), format_number(A, 0, language)]
            ]
            
            input_table = Table(input_data, colWidths=[4*inch, 2*inch])
            input_table.setStyle(TableStyle([
                ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
                ('FONTSIZE', (0, 0), (-1, -1), 10),
                ('TEXTCOLOR', (0, 0), (0, -1), colors.HexColor('#34495e')),
                ('ALIGN', (1, 0), (1, -1), 'RIGHT'),
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
            ]))
            elements.append(input_table)
            elements.append(Spacer(1, 0.1*inch))
        
        # Results
        if 'results' in q3_data:
            results_label = Paragraph(f"<b>{get_text(language, 'pdf', 'results_label')}:</b>", body_style)
            elements.append(results_label)
            
            can_afford = q3_data['results'].get('can_afford', False)
            A_count = q3_data['inputs'].get('A', 0) if 'inputs' in q3_data else 0
            
            if can_afford:
                result_text = get_text(language, 'question3', 'success_message').format(count=int(A_count))
            else:
                result_text = get_text(language, 'question3', 'warning_message')
            
            result_para = Paragraph(result_text, body_style)
            elements.append(result_para)
        
        # Add chart if available
        if 'chart' in q3_data and q3_data['chart']:
            elements.append(Spacer(1, 0.1*inch))
            img_bytes = _convert_matplotlib_to_image(q3_data['chart'])
            if img_bytes:
                img = Image(img_bytes, width=5*inch, height=3.5*inch)
                elements.append(img)
        
        elements.append(Spacer(1, 0.2*inch))
    
    # Add footer note
    elements.append(Spacer(1, 0.3*inch))
    footer_note = Paragraph(get_text(language, 'pdf', 'footer_note'), 
                           ParagraphStyle('FooterStyle', parent=styles['Normal'], 
                                        fontSize=9, textColor=colors.grey, 
                                        alignment=TA_JUSTIFY, italic=True))
    elements.append(footer_note)
    
    # Build PDF
    doc.build(elements)
    
    if not output_path:
        buffer.seek(0)
        return buffer
    
    return None
