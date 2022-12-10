
import random
import math
import numpy as np
import matplotlib.pyplot as plt

def reduce_temp(temp):
    return temp * 0.8

def calc_y(x):
    return (math.sin(x) / math.tan(x)) * (x+1)

def simulated_annealing(env, temp, iterations):
   # choose a starting value from the environment, this is the current best
    best = np.random.choice(env)
    # evaluate the output given this current best value with the function
    # function = (sin(x)/tan(x)) * (x+1)
    current = calc_y(best)
    # keep a list of the x values tried for graphing
    best_x = []
    # run the algorithm for the given number of iterations to try to get as close
    # as possible to the global maxima
    for i in range(iterations):
        # chose the next value to try
        next_x = best + np.random.normal()
        delta = calc_y(next_x) - current
        # decide whether to use this value with the probability function e^(deltaE/Temperature)
        if next_x > 1 or next_x < 0 or np.log(np.random.rand()) * temp > delta:
            next_x = best
        
        # the chosen value is now the best
        best = next_x
        # evaluate the current
        current = calc_y(best)
        # reduce the temperature
        temp = reduce_temp(temp)
        # append the best to the list for graphing
        best_x.append(best)
        
    return best, best_x

# graphing
space = np.linspace(-1,1,500)
x, best_x = simulated_annealing(space, 50, 500)
y = [calc_y(i) for i in space]
plt.xlabel("x")
plt.ylabel("y")
plt.plot(space, y)
plt.scatter(x, calc_y(x))
best_y = [calc_y(i) for i in best_x]
plt.plot(best_x, best_y)
plt.show()
