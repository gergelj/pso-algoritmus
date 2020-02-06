import numpy as np


class Particle:
    def __init__(self, min_v, max_v):
        self.position = (max_v - min_v) * np.random.random(2) + min_v
        self.best_position = self.position
        self.best_value = None
        self.prev_v = np.random.random(2)


class Swarm:
    def __init__(self):
        self.global_best_value = None
        self.global_best_position = None
        self.particles = []
