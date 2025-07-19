import numpy as np
import matplotlib.pyplot as plt

# Constants
K = 150      # Strike price
premium = 5  # Option premium
S = np.linspace(100, 200, 500)  # Underlying stock price range

# Payoff and Profit formulas

# (a) Long Call
payoff_long_call = np.maximum(S - K, 0)
profit_long_call = payoff_long_call - premium

# (b) Short Call
payoff_short_call = -np.maximum(S - K, 0)
profit_short_call = payoff_short_call + premium

# (c) Long Put
payoff_long_put = np.maximum(K - S, 0)
profit_long_put = payoff_long_put - premium

# (d) Short Put
payoff_short_put = -np.maximum(K - S, 0)
profit_short_put = payoff_short_put + premium

# Plotting
fig, axs = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle('Options Payoff and Profit Diagrams (K=$150, Premium=$5)', fontsize=14)

# Long Call
axs[0, 0].plot(S, payoff_long_call, label='Payoff')
axs[0, 0].plot(S, profit_long_call, label='Profit', linestyle='--')
axs[0, 0].axhline(0, color='black', linewidth=0.5)
axs[0, 0].axvline(K, color='red', linestyle=':')
axs[0, 0].set_title('Long Call')
axs[0, 0].legend()
axs[0, 0].grid(True)

# Short Call
axs[0, 1].plot(S, payoff_short_call, label='Payoff')
axs[0, 1].plot(S, profit_short_call, label='Profit', linestyle='--')
axs[0, 1].axhline(0, color='black', linewidth=0.5)
axs[0, 1].axvline(K, color='red', linestyle=':')
axs[0, 1].set_title('Short Call')
axs[0, 1].legend()
axs[0, 1].grid(True)

# Long Put
axs[1, 0].plot(S, payoff_long_put, label='Payoff')
axs[1, 0].plot(S, profit_long_put, label='Profit', linestyle='--')
axs[1, 0].axhline(0, color='black', linewidth=0.5)
axs[1, 0].axvline(K, color='red', linestyle=':')
axs[1, 0].set_title('Long Put')
axs[1, 0].legend()
axs[1, 0].grid(True)

# Short Put
axs[1, 1].plot(S, payoff_short_put, label='Payoff')
axs[1, 1].plot(S, profit_short_put, label='Profit', linestyle='--')
axs[1, 1].axhline(0, color='black', linewidth=0.5)
axs[1, 1].axvline(K, color='red', linestyle=':')
axs[1, 1].set_title('Short Put')
axs[1, 1].legend()
axs[1, 1].grid(True)

# Labels
for ax in axs.flat:
    ax.set_xlabel('Stock Price at Expiration ($)')
    ax.set_ylabel('Payoff / Profit ($)')

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
