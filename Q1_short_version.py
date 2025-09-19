import math
r=0.043
payments_A=[225,215,250,225,205]
payments_B=[220,225,250,250,210]
def calculate_pv(payments,r):
    pv=0
    for t,payment in enumerate(payments,start=1):
     pv+=payment*math.exp(-r*t)
    return pv # we need present value .so it would need to be return
pv_A=calculate_pv(payments_A,r)
pv_B=calculate_pv(payments_B,r)
if pv_A> pv_B:
   print("Investment A is better option")
elif pv_B> pv_A:
   print("Investment B is better option")
else:
   print("None")

print("Present value of option A is=" ,pv_A)
print("Present value of option B is=",pv_B)

