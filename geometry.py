import math
import random


class Geometry:
    @staticmethod
    def closest_point_on_segment(P, A, B):
        AP = P.pos - A.pos
        AB = B.pos - A.pos

        len_sq = AB.x * AB.x + AB.y * AB.y
        if len_sq == 0:
            return A.pos

        t = AP.dot(AB) / len_sq
        t = max(0, min(1, t))

        return A.pos + AB * t


class Vector:
    __slots__ = ("x", "y")

    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def iadd(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def magnitude(self):
        return math.hypot(self.x, self.y)

    def normalize(self):
        mag = self.magnitude()
        return Vector(self.x / mag, self.y / mag) if mag > 1e-9 else Vector(0, 0)

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def reflect(self, normal):
        dot = self.dot(normal)
        return self - normal * (2.0 * dot)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


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
        self.pos.iadd(self.vel)


class Circle:
    def __init__(self, x=None, y=None, r=None, color=None):
        x = x if x is not None else random.randint(10, 250)
        y = y if y is not None else random.randint(10, 250)

        self.pos = Vector(x, y)
        self.vel = Vector(0, 0)
        self.acc = Vector(0, 0)

        self.r = r if r is not None else random.randint(1, 5)
        self.color = color if color is not None else random.randint(5, 11)

    @property
    def x(self):
        return self.pos.x

    @property
    def y(self):
        return self.pos.y

    def apply_force(self, force):
        self.acc.iadd(force)

    def resolve_collision_with_segment(self, A, B):
        closest = Geometry.closest_point_on_segment(self, A, B)

        diff = self.pos - closest
        dist_sq = diff.x * diff.x + diff.y * diff.y

        if dist_sq > self.r * self.r or dist_sq < 1e-9:
            return False

        n = diff.normalize()
        dot = self.vel.dot(n)

        if dot < 0:
            # rebotando la velocidad
            self.vel = self.vel.reflect(n)

            # Corregir penetración (separar el círculo del segmento)
            # Esto evita que el círculo 'tiemble' o se hunda
            self.pos = closest + (n * self.r)

        return True

    def update(self):
        self.vel.iadd(self.acc)
        self.pos.iadd(self.vel)
        self.acc = Vector(0, 0)
