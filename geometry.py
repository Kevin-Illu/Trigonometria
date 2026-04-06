import math
import random


class Geometry:
    @staticmethod
    def distance_sq(p1, p2):
        dx = p2.x - p1.x
        dy = p2.y - p1.y

        return dx * dx + dy * dy

    @staticmethod
    def distance_sqrt(p1, p2):
        return math.sqrt(Geometry.distance_sq(p1, p2))

    @staticmethod
    def get_nearest_point(target, points):
        nearest = points[0]
        current_nearest_distance = Geometry.distance_sq(target, nearest)

        for point in points[1:]:
            distance = Geometry.distance_sq(target, point)

            if distance < current_nearest_distance:
                current_nearest_distance = distance
                nearest = point

        return nearest

    @staticmethod
    def closest_point_on_segment(P, A, B):
        APx = P.x - A.x
        APy = P.y - A.y

        ABx = B.x - A.x
        ABy = B.y - A.y

        dot = APx * ABx + APy * ABy
        len_sq = ABx * ABx + ABy * ABy

        t = dot / len_sq if len_sq != 0 else 0

        # clamp just limit the point to stay
        # inside of the segment.
        t = max(0, min(1, t))

        # create a new vector that tell us
        # where is the point projection.
        closest_x = A.x + t * ABx
        closest_y = A.y + t * ABy

        return Vector(closest_x, closest_y)

    @staticmethod
    def distance_point_to_segment_sq(P, A, B):
        closest = Geometry.closest_point_on_segment(P, A, B)

        dx = P.x - closest.x
        dy = P.y - closest.y

        return dx * dx + dy * dy


class Point:
    def __init__(self, x=None, y=None, color=None):
        x = x if x is not None else random.randint(0, 255)
        y = y if y is not None else random.randint(0, 255)

        self.pos = Vector(x, y)
        self.vel = Vector(0, 0)
        self.color = color if color is not None else random.randint(1, 10)

    @property
    def x(self):
        return self.pos.x

    @property
    def y(self):
        return self.pos.y

    def update(self):
        self.pos = self.pos + self.vel


class Circle:
    def __init__(self, x=None, y=None, r=None, color=None):
        x = x if x is not None else random.randint(10, 250)
        y = y if y is not None else random.randint(10, 250)

        self.color = color if color is not None else random.randint(5, 11)
        self.colliding = False
        self.r = r if r is not None else random.randint(1, 5)

        self.pos = Vector(x, y)
        self.vel = Vector(0, 0)
        self.acc = Vector(0, 0)

    @property
    def x(self):
        return self.pos.x

    @property
    def y(self):
        return self.pos.y

    def is_colliding_with_circle(self, circle):
        r_sum = self.r + circle.r
        return Geometry.distance_sq(self, circle) <= r_sum * r_sum

    def is_colliding_with_segment(self, A, B):
        return Geometry.distance_point_to_segment_sq(self, A, B) <= self.r * self.r

    def apply_force(self, force):
        self.acc = self.acc + force

    def update(self):
        self.vel.iadd(self.acc)
        self.pos.iadd(self.vel)
        self.acc.x, self.acc.y = 0.0, 0.0


class Vector:
    __slots__ = ("x", "y")

    def iadd(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def magnitude(self):
        return math.hypot(self.x, self.y)

    def normalize(self):
        mag = self.magnitude()
        return Vector(self.x / mag, self.y / mag) if mag > 1e-9 else Vector(0, 0)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
