import numpy as np

def threepiece_growth(a: float, m: float, b: float):
  assert(a < m < b)
  return lambda u: np.heaviside(u-a,1) - (1-m)*np.heaviside(u-b,1)
