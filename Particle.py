import numpy as np
import random
import matplotlib.pyplot as plt
from pso_config import *

class Particle():
    def __init__(self):
        self.position = np.array([(-1) ** (bool(random.getrandbits(1))) * random.random() * 10,
                                  (-1) ** (bool(random.getrandbits(1))) * random.random() * 10])
        self.pbest_position = self.position
        self.pbest_value = float('inf')
        self.velocity = np.array([0, 0])

    def __str__(self, n):
        print(f"Particle {n} is at ", self.position, " with pbest ", self.pbest_position)

    def move(self):
        self.position = self.position + self.velocity