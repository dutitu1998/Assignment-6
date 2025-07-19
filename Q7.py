import math

# Given values
S = 19           # Current stock price
C = 1            # Call option price
K = 20           # Strike price
r = 0.03         # Risk-free rate (continuous compounding)
T = 4/12         # Time to maturity in years

# Apply Put-Call Parity
P = C + K * math.exp(-r * T) - S

# Output
print(f"Price of the 4-month European put option: ${P:.4f}")
