# date_utils.py

import datetime
from utils.translations import get_months


def generate_next_6_months(language='en'):
    """
    Generate a list of the next 6 month abbreviations in the specified language.
    
    Args:
        language (str): Language code ('en', 'de', 'fr', or 'lb')
        
    Returns:
        list: List of 6 month abbreviations
    """
    # Get the current month and year
    current_date = datetime.datetime.now()
    current_month = current_date.month
    current_year = current_date.year

    # Get month names for the selected language
    month_names = get_months(language)

    # Generate the next 6 months
    months = []
    for i in range(1, 7):  # Start from 1 to get the next month
        month = current_month + i
        year = current_year
        if month > 12:
            month -= 12
            year += 1
        # Use month index (1-12) to get localized month name
        months.append(month_names[month - 1])

    return months
