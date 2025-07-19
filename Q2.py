import numpy as np

# Given data
T = 5
y = 0.11
c = 0.08
F = 100
C = c * F

# (a) Calculate price
times = np.arange(1, T+1)
discount_factors = np.exp(-y * times)
PV_coupons = np.sum(C * discount_factors)
PV_face = F * np.exp(-y * T)
price = PV_coupons + PV_face

# (b) Calculate duration
weights = (times * C * discount_factors)
weights_face = T * F * np.exp(-y * T)
duration = (np.sum(weights) + weights_face) / price

# (c) Price change for yield decrease of 0.2% (0.002)
delta_y = -0.002
delta_price_approx = -duration * price * delta_y
new_price_approx = price + delta_price_approx

# (d) Recalculate price for y = 10.8%
y_new = 0.108
discount_factors_new = np.exp(-y_new * times)
PV_coupons_new = np.sum(C * discount_factors_new)
PV_face_new = F * np.exp(-y_new * T)
price_new = PV_coupons_new + PV_face_new

print(f"(a) Bond price at 11% yield: ${price:.4f}")
print(f"(b) Macaulay Duration: {duration:.4f} years")
print(f"(c) Approximate new price after 0.2% yield decrease: ${new_price_approx:.4f}")
print(f"(d) Exact new price at 10.8% yield: ${price_new:.4f}")
print(f"Difference between approximation and exact: ${abs(price_new - new_price_approx):.6f}")
