import numpy as np

# Given data
T = 5          # Maturity in years
y = 0.11       # Continuously compounded yield
c = 0.08       # Coupon rate
F = 100        # Face value of the bond
C = c * F      # Annual coupon payment

# (a) Calculate bond price using a for loop
PV_coupons = 0
for t in range(1, T+1):          # t = 1,2,...,T
    PV_coupons += C * np.exp(-y * t)
PV_face = F * np.exp(-y * T)
price = PV_coupons + PV_face

# (b) Calculate Macaulay Duration
weighted_sum = 0
for t in range(1, T+1):
    weighted_sum += t * C * np.exp(-y * t)
weighted_sum += T * PV_face
duration = weighted_sum / price

# (c) Approximate price change for yield decrease of 0.2% (0.002)
delta_y = -0.002
delta_price_approx = -duration * price * delta_y
new_price_approx = price + delta_price_approx

# (d) Exact price for new yield y = 10.8% (0.108)
y_new = 0.108
PV_coupons_new = 0
for t in range(1, T+1):
    PV_coupons_new += C * np.exp(-y_new * t)
PV_face_new = F * np.exp(-y_new * T)
price_new = PV_coupons_new + PV_face_new

# Display results
print("(a) Bond price at 11% yield:", price)
print("(b) Macaulay Duration:", duration, "years")
print("(c) Approximate new price after 0.2% yield decrease:", new_price_approx)
print("(d) Exact new price at 10.8% yield:", price_new)
print("Difference between approximation and exact:", abs(price_new - new_price_approx))

