# Name: Matthew Phillips
# Date: 11/13/2026
# Program Name: Paycheck Calculator
# Description: Write a program that prints a weekly pay stub with taxes taken out, plus yearly totals.

employee = "Avery"
hpr = 16
hours = 25
gross = hours * hpr
FEDERAL_TAX_RATE = 0.10
STATE_TAX_RATE = 0.035
SOCIAL_SECURITY_RATE = 0.062
MEDICARE_RATE = 0.0145
WEEKS_PER_YEAR = 52
fedtax = gross * FEDERAL_TAX_RATE
statetax = gross * STATE_TAX_RATE
socialtax = gross * SOCIAL_SECURITY_RATE
medicare = gross * MEDICARE_RATE
total = fedtax + statetax + socialtax + medicare

print(f"Employee name: {employee}")
print(f"Hourly pay rate: {hpr:.2f}")
print(f"Hours worked this week: {hours}")
print()
print("=" * 32)
print(f"PAY STUB: {employee}")
print("=" * 32)
print(f"Hours worked:       {hours}")
print(f"Hourly rate:        ${hpr:.2f}")
print(f"Gross pay:          ${gross:.2f}")
print("-" * 32)
print(f"Federal tax (10%):  ${fedtax:.2f}")
print(f"State Tax (3.5%):   ${statetax:.2f}")
print(f"Social Security:    ${socialtax:.2f}")
print(f"Medicare:           ${medicare:.2f}")
print(f"Total Taken Out:    ${total:.2f}")
print("-" * 32)
print(f"NET PAY:            ${(gross - total):.2f}")
print("=" * 32)
print(f"You keep {(100-(total / gross * 100)):.1f}% of what you earn.")
print(f"Yearly gross:   ${(gross * WEEKS_PER_YEAR):.2f}")
print(f"Yearly net:     ${((gross - total) * WEEKS_PER_YEAR):.2f}")
