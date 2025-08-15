# LOAN PAYMENT CALCULATOR
# No non-standard dependencies required
#Change
# Purpose: Compute monthly payment and total interest for a fixed-rate loan.

def monthly_payment(principal, annual_rate_percent, years):
    # Calculate a monthly mortgage/loan payment using the standard amortization formula
    r = (annual_rate_percent / 100.0) / 12.0  # Convert annual percentage rate to monthly decimal rate
    n = int(years * 12)  # Total number of monthly payments
    if r == 0:  # Handle zero-interest edge case
        return principal / n  # If no interest, simply divide principal by number of months
    factor = (1 + r) ** n  # Compound growth factor across n months
    return principal * r * factor / (factor - 1)  # Standard fixed-payment formula

# --- Simple user interaction ---
P = float(input("Loan amount (principal): "))  # Read the principal from the user
APR = float(input("Annual interest rate (percent): "))  # Read the APR in percent
Y = float(input("Term (years): "))  # Read the loan term in years

m = monthly_payment(P, APR, Y)  # Compute the monthly payment
n = int(Y * 12)  # Total number of payments
total_paid = m * n  # Total amount paid over the life of the loan
total_interest = total_paid - P  # Interest is total paid minus original principal

print(f"Monthly payment: {m:.2f}")  # Show the monthly payment rounded to 2 decimals
print(f"Total paid over {n} months: {total_paid:.2f}")  # Show the total paid
print(f"Total interest: {total_interest:.2f}")  # Show the total interest component
