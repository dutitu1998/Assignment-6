import numpy as np
import matplotlib.pyplot as plt

# Given parameters
K_call = 45
K_put = 40
call_premium = 3
put_premium = 4
total_premium = call_premium + put_premium

# Range of underlying asset prices at expiration
S = np.linspace(20, 70, 500)

# Payoff of long call = max(S - K_call, 0)
call_payoff = np.maximum(S - K_call, 0)

# Payoff of long put = max(K_put - S, 0)
put_payoff = np.maximum(K_put - S, 0)

# Total profit = Call payoff + Put payoff - Total premium paid
total_profit = call_payoff + put_payoff - total_premium

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(S, total_profit, label='Strangle Profit', color='blue')
plt.axhline(0, color='black', linewidth=0.7, linestyle='--')
plt.axvline(K_put, color='red', linestyle=':', label='Put Strike ($40)')
plt.axvline(K_call, color='green', linestyle=':', label='Call Strike ($45)')
plt.title('Profit Diagram of Long Strangle (Buy Call @ 45, Put @ 40)')
plt.xlabel('Stock Price at Expiration ($)')
plt.ylabel('Profit ($)')
plt.grid(True)
plt.legend()
plt.show()
