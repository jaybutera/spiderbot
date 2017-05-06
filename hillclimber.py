import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib import *

def fitness (v):
    return np.mean(v)

def perturb (v):
    x = np.copy(v)

    for i in range( x.size ):
        if random.random() < .05:
            x[0][i] = random.random()
    return x

def create_vec():
    return np.random.rand(1, 50)

def plot_vec (v):
    plt.plot(v)

def generation ():
    p = create_vec()
    p_fit = fitness(p)

    fits = []
    genes = np.empty([50,5000], dtype=float)

    for epoch in range(5000):
        if epoch % 1000 == 0:
            print('[{0}] fitness: {1}'.format(epoch, p_fit))

        child = perturb(p)
        child_fit = fitness(child)

        if (child_fit > p_fit):
            p = child
            p_fit = child_fit

        #- Logging
        for i in range(50):
            genes[i][epoch] = p_fit

        fits.append(p_fit)
        #-

    plot_vec(fits)

    return genes

#genes = np.array((50,5000))

for i in range(1):
    print('Run ', i)
    genes = generation()

    if i == 4:
        print(genes)
        #plt.imshow(genes, cmap=cm.gray, aspect='auto', interpolation='none')

plt.show()
