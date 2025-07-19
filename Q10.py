import numpy as np

F0 = 60
K = 60
sigma = 0.30
r = 0.08
T = 0.5
n = 2
dt = T / n

u = np.exp(sigma * np.sqrt(dt))
d = 1 / u
p = (np.exp(r * dt) - d) / (u - d)
discount = np.exp(-r * dt)

# Step 2 futures prices
F_uu = F0 * u * u
F_ud = F0 * u * d  # = F0
F_dd = F0 * d * d

# Option payoffs at maturity
C_uu = max(F_uu - K, 0)
C_ud = max(F_ud - K, 0)
C_dd = max(F_dd - K, 0)

# Backward induction to step 1
C_u = discount * (p * C_uu + (1 - p) * C_ud)
C_d = discount * (p * C_ud + (1 - p) * C_dd)

# Backward induction to time 0
C_0 = discount * (p * C_u + (1 - p) * C_d)

print(f"European Call Option Value: ${C_0:.2f}")
print("Early exercise of American call on futures is not optimal.")
