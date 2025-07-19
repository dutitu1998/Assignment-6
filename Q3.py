import math

# Given data
payments = [460, 235, 640, 370, 330, 250]  # Payments from year 1 to 6
r_nominal = 0.045  # Annual nominal interest rate
n_compounding = 4  # Quarterly compounding

# Calculate Effective Annual Rate (EAR)
EAR = (1 + r_nominal / n_compounding) ** n_compounding - 1

# Calculate Present Value
pv_total = 0
for t, payment in enumerate(payments, start=1):
    pv = payment / ((1 + EAR) ** t)
    pv_total += pv

print(f"Effective Annual Rate (EAR): {EAR:.6f} or {EAR * 100:.4f}%")
print(f"Present Value of the Investment: {pv_total:.2f}")