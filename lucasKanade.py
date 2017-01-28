import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

def optFlow(Ix, Iy, It, sigma):
    Ix = Ix.flatten()
    Iy = Iy.flatten()
    It = It.flatten()

    size = Ix.size
    sigma = sigma*size
    #gaussWindow = signal.gaussian(size, std=sigma)
    gaussWindow = np.ones(size)

    weightedIx = gaussWindow * Ix
    weightedIy = gaussWindow * Iy

    A = np.zeros((2, 2))
    B = np.zeros((2, 1))

    A[0, 0] = np.inner(weightedIx, Ix)
    A[1, 1] = np.inner(weightedIy, Iy)
    A[0, 1] = np.inner(weightedIx, Iy)

    A[1, 0] = A[0, 1]

    B[0] = -np.inner(weightedIx, It)
    B[1] = -np.inner(weightedIy, It)

    return np.linalg.solve(A, B)

Ix = np.random.random((50, 40))
Iy = np.random.random((50, 40))
It = np.random.random((50, 40))

print(optFlow(Ix, Iy, It, .15))
