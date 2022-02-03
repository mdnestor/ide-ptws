import numpy as np
from scipy import ndimage

class IDE():
    def __init__(self, growth_fn, kernel_fn, initial_condition):
        self.g  = growth_fn
        self.k  = kernel_fn
        self.u  = initial_condition

class IDESimulation():
    def __init__(self, ide, num_iters, xmin, xmax, step_size, boundary_condition = 'nearest'):
        self.ide = ide
        n = 1 + int(1 + (xmax - xmin) / step_size)
        self.domain = np.linspace(xmin, xmax, n)
        self.boundary_condition = boundary_condition
        self.results = self.run(num_iters)

    def run(self, num_iters):
        x = self.domain
        U = np.zeros((num_iters + 1, x.shape[0]))

        (g, k) = (self.ide.g, self.ide.k)

        U[0] = self.ide.u(x)
        for i in range(num_iters):
            kx = k(x)
            U[i + 1] = ndimage.convolve(g(U[i]), kx, mode =
            self.boundary_condition) / np.sum(kx)
        return U
