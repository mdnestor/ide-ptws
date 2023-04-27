import numpy as np
from scipy import ndimage
from typing import Callable

def simulate_integrodifference(x: np.ndarray, u0: np.ndarray, K: np.ndarray, f: Callable, n_steps: int):
  soln = [u0]
  for i in range(n_steps):
    u = soln[-1]
    L, R = u[0], u[-1]
    fu = np.apply_along_axis(f, 0, u)
    u_next = ndimage.convolve(fu, K, mode="nearest")
    u_next[0] = f(L)
    u_next[-1] = f(R)
    soln.append(u_next)
  soln = np.array(soln)
  return soln
