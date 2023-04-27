import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

from ide import simulate_integrodifference

x = np.linspace(-8, 8, 2**10)
dx = (x[-1] - x[0]) / len(x)

# Gaussian kernel
r = 4
K = stats.norm.pdf(np.arange(-r, r+dx, dx))
K /= np.sum(K)

u0 = 0.5 * np.heaviside(-2.0 - x, 1.0)
f = lambda y: 2.0 * y * (1.0 - y)

soln = simulate_integrodifference(x, u0, K, f, 10)

for i in range(soln.shape[0]):
  plt.plot(x, soln[i], color="blue")
plt.show()
plt.savefig("example_01a.png")

plt.imshow(soln, aspect="auto", extent=[x[0], x[-1], 0, soln.shape[0]], interpolation="none")
plt.colorbar()
plt.show()
plt.savefig("example_01b.png")
