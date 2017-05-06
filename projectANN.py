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

def sigmoid (x):
    return np.divide(1., np.add(1., np.exp(-x)))

def create_vec():
    return np.random.rand(1, 50)

def plot_vec (v):
    plt.plot(v)

def plot_synapses (neurons, syn):
    for i in range( num_neurons ):
        for j in range( i ):
            w = int(3*abs(syn[i,j])+1)
            if syn[i,j] > 0: # Excitatory
                plt.plot ([neurons[0,i], neurons[0,j]],# X
                          [neurons[1,i],neurons[1,j]], # Y
                          color='k', linewidth=w)
            else: # Inhibitory
                plt.plot ([neurons[0,i], neurons[0,j]],# X
                          [neurons[1,i],neurons[1,j]], # Y
                          color=[0,0,.8], linewidth=w)

def update (neurons, syn):
    #return sigmoid( np.dot(neurons, syn) )
    tmp = np.empty([num_neurons], dtype=float)

    for i in range( num_neurons ):
        tmp[i] = np.sum( np.multiply(syn[i,:], neurons[i]) )

        if tmp[i] > 1.: tmp[i] = 1.
        elif tmp[i] < 0.: tmp[i] = 0.

    return tmp

def generation ():
    p = create_vec()
    p_fit = fitness(p)

    fits = []
    genes = np.empty([50,5000], dtype=float)
    neuronValues = np.empty([50,num_neurons], dtype=float)
    neuronPositions = np.empty([2,num_neurons], dtype=float)
    synapses = np.empty([num_neurons, num_neurons], dtype=float)

    for i in range( num_neurons ):
        for j in range( num_neurons ):
            synapses[i,j] = random.random() * 2 - 1

    # Init first row to random
    for i in range(num_neurons):
        neuronValues[0,i] = random.random()

    # init neuron positions
    angle = 0.
    angleDelta = 2 * np.pi / num_neurons
    for i in range(num_neurons):
        x = np.sin(angle)
        y = np.cos(angle)
        angle += angleDelta
        neuronPositions[0,i] = x
        neuronPositions[1,i] = y

    #plot_synapses(neuronPositions, synapses)

    #plt.plot(neuronPositions[0,:], neuronPositions[1,:], 'ko',markerfacecolor=[1,1,1], markersize=18)

    for i in range(1,50):
        neuronValues[i,:] = update(neuronValues[i-1,:], synapses)

    print(neuronValues)

    # Plot neurons
    plt.imshow(neuronValues, cmap=cm.gray, aspect='auto', interpolation='none')

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

    #plot_vec(fits)

    return genes

#genes = np.array((50,5000))

num_neurons = 10
for i in range(1):
    print('Run ', i)
    genes = generation()

    #if i == 4:
        #plt.imshow(genes, cmap=cm.gray, aspect='auto', interpolation='none')

plt.show()
