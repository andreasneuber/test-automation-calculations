import streamlit as st

# Set the layout to wide
# st.set_page_config(layout="wide")

# Title of the app
st.title('Test Automation Calculations')

st.subheader('Can a team "afford" the maintenance of [n] more automated tests?')

# Input fields
TH = st.number_input('Monthly available hours for maintenance and implementation tasks (TH):', min_value=0)
MT = st.number_input('Monthly hours dedicated to maintaining existing automated tests (MT):', min_value=0)
N = st.number_input('Total count of all current automated tests (N):', min_value=0)
A = st.number_input('Count of new automated tests to be added (A):', min_value=0)

# Calculate the potential to add more tests (P)
if N > 0:
    P = TH - (MT + ((MT / N) * A))
else:
    P = 'Undefined (N should be greater than 0)'

# Display the result
if isinstance(P, str):
    st.write(P)
else:
    st.write(f'Potential to add more tests (P): {P}')

# Interpretation
if isinstance(P, (int, float)) and P <= 0:
    st.warning('Adding more tests will lead to decay of the automation test suite.')
elif isinstance(P, (int, float)) and P > 0:
    st.success('You can afford to add more automated tests.')
