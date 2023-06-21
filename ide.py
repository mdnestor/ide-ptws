import numpy as np
from scipy import ndimage
from typing import Callable

def simulate_integrodifference(x: np.ndarray, u0: np.ndarray, K: np.ndarray, f: Callable, n_steps: int):
  soln = np.zeros((n_steps + 1,) + u0.shape)
  soln[0] = u0
  for t in range(n_steps):
    u = soln[t]
    L = u[0]
    R = u[-1]
    fu = np.apply_along_axis(f, 0, u)
    u_next = ndimage.convolve(fu, K, mode="nearest")
    u_next[0] = f(L)
    u_next[-1] = f(R)
    soln[t + 1] = u_next
  return soln
