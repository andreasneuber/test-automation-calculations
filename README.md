# Test Automation Calculations

## How many work hours can be saved by automating the test suite??

### Formula
`Hours Saved = Manual Test Run Time − Automated Test Run Time`

## How many test runs are needed to counter-balance the initial investment for automating a test suite?

### Formula
`Test Run Number for Break even = Implementation Time / Time savings by automation`

## Can a team "afford" maintenance of [n] more automated tests?

- Monthly available hours for maintenance and implementation tasks: TH
- Monthly hours dedicated to maintaining existing automated tests: MT 
- Total count of all current automated tests: N 
- Count of new automated tests to be added: A 
- Potential to add more tests: P

### Formula
`P = TH – (MT + ((MT / N) x A))`

If P is 0 or negative 
=> Adding more tests will lead to the decay of the automation test suite. Maintenance cannot be kept up.

***

[Docu Streamlit App](docs/Streamlit-App.md)