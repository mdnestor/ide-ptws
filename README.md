This is a solver of integrodifference equations in 1-dimension written in Python 3 used in this paper: [arXiv:2202.00234](https://arxiv.org/abs/2202.00234).

The main function is given in [ide.py](ide.py) and there are examples of its usage in [/examples/](/examples/). Example 01 is a well-known model while examples 02 and 03 use the model from the paper.

## Background

The integrodifference equation (for a definition see [1] or [Wikipedia](https://en.wikipedia.org/wiki/Integrodifference_equation)) can be written as

$$ u_{t+1}(x) = \int_{-\infty}^{\infty} k(x-y) f(u_t(y)) dy $$

where each $u_t:\mathbb{R} \to \mathbb{R}$, $k$ is a convolution kernel, and $f$ is some function.

[1]: Lutscher (2019).  Integrodifference Equations in Spatial Ecology. DOI: [10.1007/978-3-030-29294-2](https://doi.org/10.1007/978-3-030-29294-2)

## Requirements

Python==3.9.16. See [requirements.txt](requirements.txt).

## Usage

The main solver is `simulate_integrodifference` in [ide.py](ide.py). it takes 5 inputs:
- a 1d array of locations `x`
- a 1d scalar array `u` with same shape as x,
- a 1d convolution kernel `K`,
- a callable `f: float -> float`,
- the number of steps `n` to simulate

The result is an array of shape (n,k) where k is the length of x.

## Example

Below is an example of the solver using $f(x)=2x(1-x)$ and $k$ is a N(0,1) Gaussian which we just import from scipy.stats:

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

*Note: t goes from top to bottom (the index is reversed).

### Numerically estimating the traveling wave speed

Let's increase the domain size to (-128, 128) and the number of steps to 100.
The steady states of $f$ are $y=0$ and $y=(r-1)/r$, where $r=2$ (recycling use of $r$ from the definition of the Gaussian kernel).
So we compute the mean of u0, divide by $(r-1)/r$, and treat this as the position of the wavefront as a proportion of the segment from the left and right endpoints of x. We can then take the first difference via numpy.gradient and hope this converges to the true wave speed!

```python3
x = np.linspace(-128, 128, 2**10)
dx = (x[-1] - x[0]) / len(x)

r = 4
K = stats.norm.pdf(np.arange(-r, r+dx, dx))
K /= np.sum(K)

u0 = 0.5 * np.heaviside(-x, 1.0)
f = lambda y: 2.0 * y * (1.0 - y)

soln = simulate_integrodifference(x, u0, K, f, 100)

w = np.mean(soln, axis=1) / 0.5* (x[-1] - x[0]) + x[0]
c = np.gradient(w)

c_est = c[-1]

plt.plot(c, color="red")
plt.xlabel("time step")
plt.ylabel("estimated wavespeed")
plt.legend()
plt.savefig("examples/example_04.png")
```

![](/examples/example_04.png)

```python3
>>> print(c_est)
1.164225807614116
```
