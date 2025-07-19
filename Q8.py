import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm

# Black-Scholes formulas
def bs_call(S, K, T, r, sigma):
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2)*T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return S * norm.cdf(d1) - K * np.exp(-r*T)*norm.cdf(d2)

def bs_put(S, K, T, r, sigma):
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2)*T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return K * np.exp(-r*T)*norm.cdf(-d2) - S * norm.cdf(-d1)

# Payoff functions
def payoff_call(S_T, K):
    return np.maximum(S_T - K, 0)

def payoff_put(S_T, K):
    return np.maximum(K - S_T, 0)

# Profit calculation for a strategy
def calc_profit(S_T, positions):
    """
    positions: list of tuples
      (option_type, strike, position, premium)
      option_type: 'call' or 'put'
      position: +1 (long) or -1 (short)
      premium: initial option price paid/received
    """
    total_payoff = np.zeros_like(S_T)
    total_cost = 0
    for opt_type, K, pos, premium in positions:
        if opt_type == 'call':
            payoff = payoff_call(S_T, K)
        else:
            payoff = payoff_put(S_T, K)
        total_payoff += pos * payoff
        total_cost += pos * premium
    return total_payoff - total_cost

# Parameters
S0 = 32
sigma = 0.30
r = 0.05

# Price ranges to calculate profits for
S_T = np.linspace(10, 50, 400)

# (a) Bull Spread (calls) K=25,30; T=0.5
T_a = 0.5
c25 = bs_call(S0, 25, T_a, r, sigma)
c30 = bs_call(S0, 30, T_a, r, sigma)
bull_spread = [('call', 25, 1, c25), ('call', 30, -1, c30)]
profit_bull = calc_profit(S_T, bull_spread)
cost_bull = c25 - c30

# (b) Bear Spread (puts) K=25,30; T=0.5
p25 = bs_put(S0, 25, T_a, r, sigma)
p30 = bs_put(S0, 30, T_a, r, sigma)
bear_spread = [('put', 25, -1, p25), ('put', 30, 1, p30)]
profit_bear = calc_profit(S_T, bear_spread)
cost_bear = -p25 + p30

# (c) Butterfly Spread (calls) K=25,30,35; T=1.0
T_c = 1.0
c25_1 = bs_call(S0, 25, T_c, r, sigma)
c30_1 = bs_call(S0, 30, T_c, r, sigma)
c35_1 = bs_call(S0, 35, T_c, r, sigma)
butterfly_calls = [('call', 25, 1, c25_1), ('call', 30, -2, c30_1), ('call', 35, 1, c35_1)]
profit_butterfly_calls = calc_profit(S_T, butterfly_calls)
cost_butterfly_calls = c25_1 - 2*c30_1 + c35_1

# (d) Butterfly Spread (puts) K=25,30,35; T=1.0
p25_1 = bs_put(S0, 25, T_c, r, sigma)
p30_1 = bs_put(S0, 30, T_c, r, sigma)
p35_1 = bs_put(S0, 35, T_c, r, sigma)
butterfly_puts = [('put', 25, 1, p25_1), ('put', 30, -2, p30_1), ('put', 35, 1, p35_1)]
profit_butterfly_puts = calc_profit(S_T, butterfly_puts)
cost_butterfly_puts = p25_1 - 2*p30_1 + p35_1

# (e) Straddle at K=30, T=0.5
c30_5 = bs_call(S0, 30, T_a, r, sigma)
p30_5 = bs_put(S0, 30, T_a, r, sigma)
straddle = [('call', 30, 1, c30_5), ('put', 30, 1, p30_5)]
profit_straddle = calc_profit(S_T, straddle)
cost_straddle = c30_5 + p30_5

# (f) Strangle K=25 (put), 35 (call), T=0.5
p25_5 = bs_put(S0, 25, T_a, r, sigma)
c35_5 = bs_call(S0, 35, T_a, r, sigma)
strangle = [('put', 25, 1, p25_5), ('call', 35, 1, c35_5)]
profit_strangle = calc_profit(S_T, strangle)
cost_strangle = p25_5 + c35_5

# Create summary DataFrame with initial cost and sample profits
df = pd.DataFrame({
    'Final Stock Price': S_T,
    'Bull Spread Profit': profit_bull,
    'Bear Spread Profit': profit_bear,
    'Butterfly Calls Profit': profit_butterfly_calls,
    'Butterfly Puts Profit': profit_butterfly_puts,
    'Straddle Profit': profit_straddle,
    'Strangle Profit': profit_strangle,
})

print("Initial setup costs (premiums) for each position:")
print(f" (a) Bull Spread cost: ${cost_bull:.4f}")
print(f" (b) Bear Spread cost: ${cost_bear:.4f}")
print(f" (c) Butterfly Calls cost: ${cost_butterfly_calls:.4f}")
print(f" (d) Butterfly Puts cost: ${cost_butterfly_puts:.4f}")
print(f" (e) Straddle cost: ${cost_straddle:.4f}")
print(f" (f) Strangle cost: ${cost_strangle:.4f}")

print("\nSample profit table (first 15 rows):")
print(df.head(15))

# Plot profit diagrams
plt.figure(figsize=(14, 9))
plt.plot(S_T, profit_bull, label='Bull Spread (Calls)')
plt.plot(S_T, profit_bear, label='Bear Spread (Puts)')
plt.plot(S_T, profit_butterfly_calls, label='Butterfly Spread (Calls)')
plt.plot(S_T, profit_butterfly_puts, label='Butterfly Spread (Puts)')
plt.plot(S_T, profit_straddle, label='Straddle')
plt.plot(S_T, profit_strangle, label='Strangle')
plt.axhline(0, color='black', linewidth=0.5)
plt.xlabel('Final Stock Price $S_T$')
plt.ylabel('Profit')
plt.title('Profit Profiles of Option Strategies at Expiration')
plt.legend()
plt.grid(True)
plt.show()
