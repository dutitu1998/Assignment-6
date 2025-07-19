import numpy as np
from scipy.stats import norm

# Given parameters
S = 30
K = 29
r = 0.05
sigma = 0.25
T = 4/12  # 4 months

# Black-Scholes d1 and d2
d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
d2 = d1 - sigma * np.sqrt(T)

# European call price
call_price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)

# American call price (equal to European call here)
american_call_price = call_price

# European put price
put_price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)

# Verify put-call parity
put_call_parity_lhs = call_price + K * np.exp(-r * T)
put_call_parity_rhs = put_price + S
parity_holds = np.isclose(put_call_parity_lhs, put_call_parity_rhs)

print(f"European Call Price: ${call_price:.4f}")
print(f"American Call Price: ${american_call_price:.4f}")
print(f"European Put Price: ${put_price:.4f}")
print(f"Put-Call Parity holds? {'Yes' if parity_holds else 'No'}")
