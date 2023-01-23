def mortgage_payment(borrowed, rate):
    r = rate / 12 / 100
    n = 30 * 12
    return borrowed * (r * (1 + r) ** n) / (((1 + r) ** n) - 1)

borrowed = float(input("Enter the amount of money borrowed: "))
rate = float(input("Enter the annual interest rate: "))

print("Monthly mortgage payment: $" + str(mortgage_payment(borrowed, rate)))