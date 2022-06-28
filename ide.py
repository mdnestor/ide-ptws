import numpy as np
from scipy.ndimage import convolve

def ide_simulate(growth_fn, kernel_fn, initial_cd, n_iters,
                 xmin, xmax, step_size,
                 boundary_mode='constant', cval=0.0):
  """
  Main IDE simulation function.
  :param function growth_fn: Growth function, takes density and position (floats) and returns float.
  :param function kernel_fn: Kernel function, takes position (float), returns float.
  :param function initial_cd: Initial condition, takes position (float), returns float.
  :param int n_iters: Number of simulation iterations.
  :param float xmin: Left domain bound.
  :param float xmax: Right domain bound.
  :param float step_size: Domain step size.
  :param str boundary_mode: Boundary condition, passed to scipy.ndimage.convolve.
  :param float cval: Constant value to use outside of domain. Only used if boundary_mode='constant'.
  """
  growth_fn = np.vectorize(growth_fn)
  kernel_fn = np.vectorize(kernel_fn)
  initial_cd = np.vectorize(initial_cd)
  
  domain = np.linspace(xmin, xmax, num=1+int((xmax-xmin)/dx), endpoint=True)
  results = [initial_cd(domain)]
  
  k = kernel_fn(domain)
  
  for i in range(n_iters):
    u = results[i]
    gu = growth_fn(u, domain)
    u_next = convolve(k, gu, mode=boundary_mode, cval=cval) / np.sum(k)
    results.append(u_next)
  
  return results