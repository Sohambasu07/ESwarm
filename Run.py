import random
import numpy as np
import matplotlib.pyplot as plt
from Particle import Particle
from Space import Space
from pso_config import *

n_iterations = int(input("Maximum number of iterations: "))
target_error = float(input("Minimum Target Error: "))#float(1e-8)
n_particles = int(input("Enter the number of particles: "))
arr = []

search_space = Space(1, target_error, n_particles)
particles_vector = [Particle() for _ in range(search_space.n_particles)]
search_space.particles = particles_vector
print("INITIAL: ")
search_space.print_particles()
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.grid(b=True)
plt.show()

iteration = 0
while (iteration < n_iterations):
    search_space.set_pbest()
    search_space.set_gbest()

    if (abs(search_space.gbest_value - search_space.target) <= search_space.target_error):
        break

    search_space.move_particles()
    iteration += 1
    search_space.print_particles()
    plt.title(iteration)
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.grid(b=True)
    plt.show()
print("FINAL: ")
search_space.print_particles()
print("The best solution is: ", search_space.gbest_position, " in n_iterations: ", iteration)