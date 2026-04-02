import pyxel
import random
import math


# TODO: create a way to make Point pairs
# based on the points in the array


class Trigonometria:
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


class Triangulos2:
    def __init__(self):
        self.points_count = 12
        self.points = [Point() for i in range(self.points_count)]

    def draw(self):
        # drawing the points
        for point in self.points:
            x, y, color = point.x, point.y, point.color
            pyxel.pset(x, y, color)

        half = self.points_count // 2

        # connecting points with lines
        for i in range(half):
            p1 = self.points[i - 1]
            p2 = self.points[(i + half) - 1]

            dx = p2.x - p1.x
            dy = p2.y - p1.y

            # drawing the hipotenusa?
            pyxel.line(p1.x, p1.y, p2.x, p2.y, i + 1)

            # drawing the ady
            pyxel.line(p1.x, p1.y, p2.x, p1.y, i + 1)

            # dragin the op
            pyxel.line(p2.x, p1.y, p2.x, p2.y, i + 1)

    def update(self):
        pass
