import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt

class IDE():
    def __init__(self, growth_fn, kernel_fn):
        self.g  = growth_fn
        self.k  = kernel_fn

class IDESimulation():
    def __init__(self, ide, initial_condition, num_iters, domain_size, step_size, boundary_condition = 'nearest'):
        n = 1 + int(1 + domain_size/step_size)

        self.ide = ide
        self.initial_condition = initial_condition
        self.domain = np.linspace(-domain_size/2, domain_size/2, n)
        self.boundary_condition = boundary_condition

        self.run(num_iters)
        self.plot()

    def run(self, num_iters, plot=True):
        x = self.domain
        U = np.zeros((num_iters + 1, x.shape[0]))

        (g, k) = (self.ide.g, self.ide.k)

        U[0] = self.initiail_condition(x)
        for i in range(num_iters):
            kx = k(x)
            U[i + 1] = ndimage.convolve(g(U[i]), kx, mode =
            self.boundary_condition) / np.sum(kx)
        self.results = U[:,::-1]

    def plot(self):
        self.plot_heatmap()
        self.plot_diffmap()

    def plot_heatmap(self):
        x = self.domain
        y = np.arange(self.results.shape[0])

        X, Y = np.meshgrid(x, y)
        Z = self.results

        fig, ax = plt.subplots()

        c = ax.pcolormesh(X, Y, Z,
                          cmap='coolwarm',
                          vmin=np.min(Z),
                          vmax=np.max(Z))

        ax.axis([np.min(X), np.max(X), np.min(Y), np.max(Y)])

        fig.colorbar(c, ax=ax)

        ax.set_xlabel('$x$ (position)')
        ax.set_ylabel('$n$ (time step)')

        plt.show()

    def plot_diffmap(self):
        x = self.domain
        y = np.arange(self.results.shape[0])

        X, Y = np.meshgrid(x, y)
        Z = self.results
        Z = np.gradient(Z, axis=0)
        Z /= np.sign(Z)

        fig, ax = plt.subplots()

        c = ax.pcolormesh(X, Y, Z,
                          cmap='coolwarm',
                          vmin=np.min(Z),
                          vmax=np.max(Z))

        ax.axis([np.min(X), np.max(X), np.min(Y), np.max(Y)])

        fig.colorbar(c, ax=ax)

        ax.set_xlabel('$x$ (position)')
        ax.set_ylabel('$n$ (time step)')
        plt.gca().invert_yaxis()
        plt.show()
