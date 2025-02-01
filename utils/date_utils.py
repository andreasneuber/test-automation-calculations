# date_utils.py

import datetime


def generate_next_6_months():
    # Get the current month and year
    current_date = datetime.datetime.now()
    current_month = current_date.month
    current_year = current_date.year

    # Generate the next 6 months
    months = []
    for i in range(1, 7):  # Start from 1 to get the next month
        month = current_month + i
        year = current_year
        if month > 12:
            month -= 12
            year += 1
        months.append(datetime.date(year, month, 1).strftime('%b'))

    return months
