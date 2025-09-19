import numpy as np
import matplotlib.pyplot as plt

# Parameters
K_call = 45
K_put = 40
call_premium = 3
put_premium = 4
total_premium = call_premium + put_premium

S = np.linspace(20, 70, 500)

call_payoff = np.maximum(S - K_call, 0)
put_payoff = np.maximum(K_put - S, 0)

# Total profit
total_profit = call_payoff + put_payoff - total_premium

# Minimal plotting
plt.plot(S, total_profit)               # Profit curve
plt.axhline(0, color='k', ls='--')    # Zero profit line
plt.title('Profit Diagram of Long Strangle (Buy Call @ 45, Put @ 40)')
plt.xlabel('Stock Price at Expiration ($)')
plt.ylabel('Profit ($)')
plt.show()
