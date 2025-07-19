# To determine which investment is preferable, we will calculate the present value (PV)
# of each investment using the given continuously compounded annual interest rate of 4.33%.
# The investment with the higher present value is the better choice

import math  # To use math.exp for continuous compounding

# Given data
r = 0.0433  # Continuously compounded annual interest rate
payments_A = [225, 215, 250, 225, 205]  # Investment A payments
payments_B = [220, 225, 250, 250, 210]  # Investment B payments

# Function to calculate present value of a list of payments
def calculate_pv(payments, rate):
    pv = 0
    for t, payment in enumerate(payments, start=1):  # t starts from 1
        pv += payment * math.exp(-rate * t)  # Discount using continuous compounding
    return pv

# Calculate present values for both investments
pv_A = calculate_pv(payments_A, r) #This line calls a function named calculate_pv() and assigns the result to the variable pv_A.
pv_B = calculate_pv(payments_B, r)

# Determine the preferable investment by comparing present values
if pv_A > pv_B:
    preferable = "A"
    print("Investment A is preferable.")
elif pv_B > pv_A:
    preferable = "B"
    print("Investment B is preferable.")
else:
    preferable = "None"
    print("Both investments are equally preferable.")

# Display results
print(f"Present Value of Investment A: ${pv_A:.2f}")
print(f"Present Value of Investment B: ${pv_B:.2f}")
print(f"Preferable Investment: {preferable}")
