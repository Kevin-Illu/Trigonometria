import math
import random


class Geometry:
    def distance_sq(self, p1, p2):
        dx = p2.x - p1.x
        dy = p2.y - p1.y

        return dx * dx + dy * dy

    def distance_sqrt(self, p1, p2):
        return math.sqrt(self.distance_sq(p1, p2))


class Point:
    def __init__(self, x=None, y=None, color=None):
        self.x = x or random.randint(0, 255)
        self.y = y or random.randint(0, 255)
        self.color = color or random.randint(1, 10)
