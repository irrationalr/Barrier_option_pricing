# How to calculate barrier option delta by using interpolation method.
# Required Interpolate method from Scipy
import numpy as np
S = []
K = 100

S_ko = 70
V_ko = []

spot_max = 120
spot_min = 80

K_moneyness = S / K
option_price = np.interp(K_moneyness,S_ko/K,V_ko[0])
print("Option Price: ", option_price)
S_min = spot_max
S_max = spot_min

sort_vector = np.sort(np.append(S_ko/K,K_moneyness))
index_left = np.where(sort_vector == K_moneyness)[0][0] -1
ds = (S_max - S_min)/M
delta_t0 = (V_ko[0][index_left] - V_ko[0][index_left-1]) / (2*ds)
print("Delta at time t0: ", delta_t0)