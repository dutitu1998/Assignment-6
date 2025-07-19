import numpy as np

# Given data
S0 = 484
K = 480
r = 0.10
q = 0.03
sigma = 0.25
T = 2/12
n = 4
dt = T / n

u = np.exp(sigma * np.sqrt(dt))
d = 1 / u
p = (np.exp((r - q) * dt) - d) / (u - d)
discount = np.exp(-r * dt)

# Initialize stock price tree
stock_prices = np.zeros((n + 1, n + 1))
for i in range(n + 1):
    for j in range(i + 1):
        stock_prices[i, j] = S0 * (u ** j) * (d ** (i - j))

# Initialize option values at maturity (put payoff)
option_values = np.maximum(K - stock_prices[n, :], 0)

# Backward induction
for i in range(n - 1, -1, -1):
    for j in range(i + 1):
        continuation_value = discount * (p * option_values[j + 1] + (1 - p) * option_values[j])
        exercise_value = K - stock_prices[i, j]
        option_values[j] = max(exercise_value, continuation_value)

print(f"The estimated value of the 2-month American put option is: ${option_values[0]:.4f}")
