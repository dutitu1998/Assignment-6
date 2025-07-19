import numpy as np

S0 = 40
r = 0.10
T = 1.0

# (a)
F0 = S0 * np.exp(r * T)
V0 = 0

# (b)
t = 0.5
S_t = 45
T_t = T - t

F_t_new = S_t * np.exp(r * T_t)
F_t_old = F0

V_t = np.exp(-r * T_t) * (F_t_old - F_t_new)

print(f"(a) Forward price at inception: ${F0:.2f}")
print(f"(a) Initial value of forward contract: ${V0:.2f}")
print(f"(b) Forward price at 6 months: ${F_t_new:.2f}")
print(f"(b) Value of forward contract at 6 months: ${V_t:.2f}")
