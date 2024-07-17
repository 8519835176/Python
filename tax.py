# Function to calculate tax based on income
def calculate_tax(income):
    if income <= 150000:
        return 0
    elif 150001 <= income <= 300000:
        return (income - 150000) * 0.10
    elif 300001 <= income <= 500000:
        return (150000 * 0.10) + (income - 300000) * 0.20
    else:
        return (150000 * 0.10) + (200000 * 0.20) + (income - 500000) * 0.30

# Take income as input from the user
try:
    income = float(input("Enter the income: "))
    
    # Ensure income is non-negative
    if income < 0:
        print("Income cannot be negative.")
    else:
        # Calculate tax
        tax = calculate_tax(income)
        
        # Print the tax
        print(f"Tax = {tax:.2f}")

except ValueError:
    print("Please enter a valid number.")
