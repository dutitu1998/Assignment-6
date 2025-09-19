import numpy as np

S0 = 40                  # Initial stock price
r = 0.10                 # Risk-free interest rate (continuous)
T = 1                    # Maturity in years

F0 = S0 * np.exp(r * T)  # Forward price at t=0
V0 = 0                   # Value at initiation is zero

print("(a) Forward Price at initiation:", F0)
print("    Value of forward contract at initiation:", V0)

# --- (b) 6 months later ---
t = 0.5                  # 6 months have passed
St = 45                  # Stock price after 6 months
time_remaining = T - t   # Time remaining = 0.5 years

# New forward price at time t
Ft = St * np.exp(r * time_remaining)

# Value of original forward contract
Vt = St - F0 * np.exp(-r * time_remaining)

print("\n(b) Forward Price 6 months later:", Ft)
print("    Value of original forward contract at 6 months:", Vt)
