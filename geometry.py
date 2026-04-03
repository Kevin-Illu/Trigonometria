import math
import random


class Geometry:
    def distance_sq(self, p1, p2):
        dx = p2.x - p1.x
        dy = p2.y - p1.y

        return dx * dx + dy * dy

    def distance_sqrt(self, p1, p2):
        return math.sqrt(self.distance_sq(p1, p2))

    def get_nearest_point(self, target, points):
        nearest = points[0]
        current_nearest_distance = self.distance_sq(target, nearest)

        for point in points[1:]:
            distance = self.distance_sq(target, point)

            if distance < current_nearest_distance:
                current_nearest_distance = distance
                nearest = point

        return nearest


class Point:
    def __init__(self, x=None, y=None, color=None):
        self.x = x if x is not None else random.randint(0, 255)
        self.y = y if y is not None else random.randint(0, 255)
        self.color = color if color is not None else random.randint(1, 10)


class Circle:
    def __init__(self, x=None, y=None, r=None):
        self.x = x if x is not None else random.randint(10, 250)
        self.y = y if y is not None else random.randint(10, 250)
        self.r = r if r is not None else random.randint(1, 5)
        self.colliding = False
        self.g = Geometry()

    def is_colliding(self, circle):
        return self.g.distance_sq(self, circle) <= (self.r + circle.r) * (
            self.r + circle.r
        )
