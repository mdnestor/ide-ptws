from typing import List, Callable
import numpy as np

H = lambda x: np.heaviside(x, 1.0)

def make_piecewise(A: List[float], B: List[float]) -> Callable:
  assert(len(B) + 1 == len(A))
  f = lambda x: np.sum([(B[i+1] - B[i]) * H(x - A[i+1]) for i in range(len(B) - 1)])
  return np.vectorize(f)
