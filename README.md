# Loan Processing Tool Coding Contest

Welcome to the Loan Processing Tool Coding Contest!

## Objective
Create a loan processing tool that takes user application data and decides which bank to send the loan application to based on their underwriting guidelines. The tool should utilize financial metrics such as cash flow, net income, Debt Coverage Ratio (DCR), gross profit, and total income (loss).

## Rules
- The contest runs from [Start Date] to [End Date].
- Fork this repository and create a pull request with your solution.
- Your solution must pass all the test cases to be considered.

## Prizes
- 1st Place: $1000
- 2nd Place: $500
- 3rd Place: $250

## Getting Started
1. Fork this repository.
2. Clone the forked repository to your local machine.
3. Implement your solution in `starter_code/main.py`.
4. Run the tests locally using `python -m unittest discover -s tests`.
5. Push your changes and create a pull request.

## Problem Statement
You need to build a function that processes loan applications and decides the best bank to send the application to based on their underwriting guidelines. The function should use financial metrics such as cash flow, net income, DCR, gross profit, and total income (loss).

### Input
- A dictionary containing the applicant's information (e.g., credit score, loan amount, business type, financial metrics).

### Output
- The name of the bank that the application should be sent to.

### Example
```python
application_data = {
    "credit_score": 720,
    "loan_amount": 50000,
    "business_type": "retail",
    "cash_flow": 100000,
    "net_income": 25000,
    "DCR": 1.5,
    "gross_profit": 50000,
    "total_income_loss": 20000
}
