import numpy as np
import matplotlib.pyplot as plt
import imageio

def plot_particles(iter, particles, gbest, figsz = (7,7), x_min = -10, x_max = 10, y_min = -10, y_max = 10, plot = True):
    n = 1
    x_list = []
    y_list = []
    for particle in particles:
        particle.__str__(n)
        x_list.append(particle.position[0])
        y_list.append(particle.position[1])
        n += 1
    if plot:
        plt.figure(figsize = figsz)
        plt.title("Iteration: " + str(iter) + ", Best position: " + str(gbest))
        plt.xlim(x_min, x_max)
        plt.ylim(y_min, y_max)
        plt.grid(b=True)
        plt.scatter(x_list, y_list, 8,'r','o')
        plt.savefig(f'./Simulations/sim_{iter}.png', transparent = False, facecolor = 'white')

def make_gif(iters):
    frames = []
    for i in range(iters + 1):
        frames.append(imageio.imread(f'./Simulations/sim_{i}.png'))
    imageio.mimsave('./Simulations/PSO_Run.gif', frames)


