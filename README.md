This is a solver of integrodifference equations in 1-dimension written in Python 3 used in this paper: [arXiv:2202.00234](https://arxiv.org/abs/2202.00234).

The main function is given in `ide.py` and there are examples of its usage in `/examples/`.

## Background

The integrodifference equation (for a definition see [1]) is given by

$$ u_{t+1} = \int_{-\infty}^{\infty} k(x-y) f(u_t(y)) dy $$

where each $u_t:\mathbb{R} \to \mathbb{R}$, $k$ is a convolution kernel, and $f$ is some function.
## Usage

The inputs to the solver are
- a 1d array of locations `x`
- a 1d scalar array `u` with same shape as x,
- a 1d convolution kernel `K`,
- a callable `f: float -> float`,
- the number of steps `n` to simulate
The result is an array of shape (n,k) where k is the length of x.

Here is an example usage, simulating with $f(x) = 2x(1-x)$, and $k(x)=$ the zero centered unit variance Gaussian in 1d from scipy.stats:

```python3
import numpy as np
from ide import simulate_integrodifference
from scipy import stats

x = np.linspace(-8, 8, 1024)
dx = (x[-1] - x[0]) / len(x)

# Gaussian kernel
r = 4
K = stats.norm.pdf(np.arange(-r, r+dx, dx))
K /= np.sum(K)

u0 = 0.5 * np.heaviside(-2.0 - x, 1.0)
f = lambda y: 2.0 * y * (1.0 - y)

soln = simulate_integrodifference(x, u0, K, f, 10)
```
The result is a 2d array which we can visualize as a heatmap:

```python3
import matplotlib.pyplot as plt
plt.imshow(soln, aspect="auto", extent=[x[0], x[-1], 0, soln.shape[0]], interpolation="none")
plt.colorbar()
plt.savefig("examples/example_01b.png")
```

![](/examples/example_01b.png)
