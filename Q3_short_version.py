import math

# Given data
payments = [460, 235, 640, 370, 330, 250]  # Payments from year 1 to 6
r_nominal = 0.045  # Annual nominal interest rate
n_compounding = 4  # Quarterly compounding

# Step 1: Calculate Effective Annual Rate (EAR)
EAR = (1 + r_nominal / n_compounding) ** n_compounding - 1

# Step 2: Calculate Present Value of each payment
pv_total = 0
for t, payment in enumerate(payments, start=1):
    pv = payment / ((1 + EAR) ** t)  # Discount each payment
    pv_total += pv  # Add to total PV

# Step 3: Print results (simple output)
print("Effective Annual Rate (EAR):", EAR)
print("Present Value of the Investment:", pv_total)
