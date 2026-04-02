import pyxel
import random
import math


# TODO: create a way to make Point pairs
# based on the points in the array


class Trogonometria:
    def distance(self, p1, p2):
        dx = p2.x - p1.x
        dy = p2.y - p1.y

        return dx * dx + dy * dy

    def distance_sqrt(self, p1, p2):
        return math.sqrt(self.distance(p1, p2))


class Point:
    def __init__(self, x=None, y=None, color=None):
        self.x = x or random.randint(50, 100)
        self.y = y or random.randint(1, 200)
        self.color = color or random.randint(1, 10)


class Triangulos2:
    def __init__(self):
        self.points_count = 10
        self.points = [Point() for i in range(self.points_count)]

    def draw(self):
        # drawing the points
        for point in self.points:
            x, y, color = point.x, point.y, point.color
            pyxel.pset(x, y, color)

    def update(self):
        pass
