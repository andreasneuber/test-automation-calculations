# Test Automation Calculations

## Can a team "afford" maintenance of [n] more automated tests?

- Monthly available hours for maintenance and implementation tasks: TH
- Monthly hours dedicated to maintaining existing automated tests: MT 
- Total count of all current automated tests: N 
- Count of new automated tests to be added: A 
- Potential to add more tests: P

### Formula
`P = TH – (MT + ((MT / N) x A))`

If P is 0 or negative => Adding more tests will lead to decay of automation test suite.
