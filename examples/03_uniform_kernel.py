import numpy as np
import matplotlib.pyplot as plt

from ide import simulate_integrodifference
from threepiece_growth import threepiece_growth

x = np.linspace(-4, 4, 1000)
dx = (x[-1] - x[0]) / len(x)

r = 1
kernel_fn = lambda x: 0.5 * np.heaviside(1 - np.abs(x), 1)
K = kernel_fn(np.arange(-r, r+dx, dx))
K /= np.sum(K)

u0 = np.heaviside(-x, 1.0)
n = 10
soln = simulate_integrodifference(x, u0, K, f, n)

for i in range(1,n):
  plt.plot(x, soln[i], color=(i/n,1-i/n,0))
plt.show()
plt.savefig("example_03a.png")

x = np.linspace(-8, 8, 1000)
dx = (x[-1] - x[0]) / len(x)

r = 1
kernel_fn = lambda x: 0.5 * np.heaviside(1 - np.abs(x), 1)
K = kernel_fn(np.arange(-r, r+dx, dx))
K /= np.sum(K)

# compact initial condition
R = 2
u0 = np.heaviside(R - np.abs(x), 1.0)
n = 10
soln = simulate_integrodifference(x, u0, K, f, n)

for i in range(1,n):
  plt.plot(x, soln[i], color=(i/n,1-i/n,0))
plt.show()
plt.savefig("example_03b.png")
