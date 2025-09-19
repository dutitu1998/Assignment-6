import numpy as np
import matplotlib.pyplot as plt

# Constants
K = 150
premium = 5
S = np.linspace(100, 200, 500)

# Payoff & Profit
payoff_long_call  = np.maximum(S - K, 0); 
profit_long_call  = payoff_long_call - premium
payoff_short_call = -np.maximum(S - K, 0); 
profit_short_call = payoff_short_call + premium
payoff_long_put   = np.maximum(K - S, 0); 
profit_long_put   = payoff_long_put - premium
payoff_short_put  = -np.maximum(K - S, 0); 
profit_short_put  = payoff_short_put + premium

plt.figure(figsize=(10,7))
plt.suptitle('Options Payoff & Profit (K=150, Premium=5)', fontsize=14)

# (2,2,1) Long Call
plt.subplot(2,2,1)
plt.plot(S, payoff_long_call, label='Payoff')
plt.plot(S, profit_long_call, '--', label='Profit')
plt.axhline(0, color='k', lw=0.5);
plt.axvline(K, color='r', ls=':')
plt.title('Long Call'); 
plt.legend();
plt.grid(True)

# (2,2,2) Short Call
plt.subplot(2,2,2)
plt.plot(S, payoff_short_call, label='Payoff')
plt.plot(S, profit_short_call, '--', label='Profit')
plt.axhline(0, color='k', lw=0.5); 
plt.axvline(K, color='r', ls=':')
plt.title('Short Call');
plt.legend();
plt.grid(True)

# (2,2,3) Long Put
plt.subplot(2,2,3)
plt.plot(S, payoff_long_put, label='Payoff')
plt.plot(S, profit_long_put, '--', label='Profit')
plt.axhline(0, color='k', lw=0.5); 
plt.axvline(K, color='r', ls=':')
plt.title('Long Put');
plt.legend();
plt.grid(True)

# (2,2,4) Short Put
plt.subplot(2,2,4)
plt.plot(S, payoff_short_put, label='Payoff')
plt.plot(S, profit_short_put, '--', label='Profit')
plt.axhline(0, color='k', lw=2);
plt.axvline(K, color='r', ls=':')
plt.title('Short Put'); 
plt.xlabel('stock price')
plt.legend();
plt.grid(True)

#plt.tight_layout(rect=[0,0.03,1,0.95])
plt.show()
