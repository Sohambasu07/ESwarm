import random
import numpy as np
import matplotlib.pyplot as plt
from Particle import Particle
from Space import Space
from pso_config import *
from Plot import *

n_iterations = int(input("Maximum number of iterations: "))
target_error = np.float64(input("Minimum Target Error: "))#float(1e-8)
n_particles = int(input("Number of particles: "))
arr = []
frames = []

search_space = Space(1, target_error, n_particles)
particles_vector = [Particle() for _ in range(search_space.n_particles)]
search_space.particles = particles_vector
iteration = 0
print("INITIAL: ")
plot_particles(iter = iteration, particles = search_space.particles, gbest = search_space.gbest_value)


while (iteration < n_iterations):
    search_space.set_pbest()
    search_space.set_gbest()

    if (abs(search_space.gbest_value - search_space.target) <= search_space.target_error):
        break
    
    
    search_space.move_particles()
    iteration += 1
    print("ITERATION: ", iteration)
    plot_particles(iter = iteration, particles = search_space.particles, gbest = search_space.gbest_value)
print("FINAL: ")
plot_particles(iter = iteration, particles = search_space.particles, gbest = search_space.gbest_value, plot = False)
make_gif(iters = n_iterations)
print("The best solution is: ", search_space.gbest_position, " in n_iterations: ", iteration)