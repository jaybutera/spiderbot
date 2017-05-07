import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib import *
import os
import time

num_sensors = 4
num_motors = 8
epochs = 50

def fitness (v):
    fitsFileName = "/Users/jaybutera/Documents/Unity/QuadBot/Assets/fitness.out"
    if(os.path.exists(fitsFileName)):
        os.remove(fitsFileName) #begin run without any fitness file already in the folder.

    weightsFileName = "/Users/jaybutera/Documents/Unity/QuadBot/Assets/ANN.out"
    #weightsFileName = "ANN.out"

    np.savetxt(weightsFileName, v, delimiter=',')

    while not os.path.exists(fitsFileName):
        time.sleep(.05)

    fitness = float(open(fitsFileName, 'r').read())
    os.remove(fitsFileName)

    return fitness

def perturb (v):
    x = np.copy(v)

    for i in range( x.shape[0] ):
        for j in range( x.shape[1] ):
            if random.random() < .05:
                x[0][i] = (random.random()-.5)*2 # [-1,1]
    return x

def create_weights():
    #numpy.random.normal(0.0, pow(num_sensors, - 0.5),(num_sensors, num_motors))
    return np.random.rand(num_sensors, num_motors)

def plot_vec (v):
    plt.plot(v)

def generation ():
    p = create_weights()
    p_fit = fitness(p)

    fits = []
    #genes = np.empty([num_sensors, num_motors, epochs], dtype=float)

    for epoch in range(epochs):
        #if epoch % int(epochs * .1) == 0:
        print('[{0}] fitness: {1}'.format(epoch, p_fit))

        child = perturb(p)
        child_fit = fitness(child)

        if (child_fit > p_fit):
            p = child
            p_fit = child_fit

        #- Logging
        #for i in range(num_):
            #genes[i][epoch] = p_fit

        fits.append(p_fit)
        #-

    plot_vec(fits)


generation()
plt.show()
