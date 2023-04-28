This is a solver of integrodifference equations in 1-dimension written in Python 3 used in this paper: [arXiv:2202.00234](https://arxiv.org/abs/2202.00234). (Tested in Python 3.9.16.)

The main function is given in [ide.py](ide.py) and there are examples of its usage in [/examples/](/examples/). Example 01 is a well-known model while examples 02 and 03 use the model from the paper.

## Background

The integrodifference equation (for a definition see [1] or [Wikipedia](https://en.wikipedia.org/wiki/Integrodifference_equation)) can be written as

$$ u_{t+1}(x) = \int_\Omega k(x-y) f(u_t(y)) dy $$

where each $u_t$ is a scalar function on $\Omega$, $k$ is a convolution kernel (often is a probability kernel) and $f$ is some scalar function. Our solver just handles the case $\Omega = \mathbb{R}^1$.

[1]: Lutscher (2019).  Integrodifference Equations in Spatial Ecology. DOI: [10.1007/978-3-030-29294-2](https://doi.org/10.1007/978-3-030-29294-2).

## Usage

The main solver is `simulate_integrodifference` in [ide.py](ide.py). it takes five inputs:
- `x`, a 1d array of locations,
- `u`, a 1d scalar array with same shape as x,
- `K`, a 1d convolution kernel,
- `f`, a callable `float -> float`,
- `n`, the number of steps to simulate

The result is an array of shape (n,k) where k is the length of x.
