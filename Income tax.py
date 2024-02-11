#Data
flat_tax_rate = 0.20
standard_deduction = 10000
deduction = 3000

# Calculate gross income, dependents and tax income
gross_income = float(input("Enter your gross income: $"))
num_dependents = int(input("Enter the number of dependents: "))

# Formula
tax_income = gross_income - standard_deduction - (num_dependents * deduction)

# Probabilities
if tax_income < 0:
    tax_income = 0

# Formal #2
income_tax = tax_income * flat_tax_rate

print("Your income tax is: $" + str(round(income_tax, 2)))
