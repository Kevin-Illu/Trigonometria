import pyxel
import math
from geometry import Circle, Point, Vector

# Parámetros
radius = 100
cx, cy = 130, 130
color = 2
n = 8  # Octágono
tau = 2 * math.pi

# Pre-generamos los puntos para no instanciar el mismo punto dos veces por segmento
vertices = [
    Point(
        cx + radius * math.cos(tau * i / n), cy + radius * math.sin(tau * i / n), color
    )
    for i in range(n)
]

# This is my code
# class NormalVectorAndReflection:
#     def __init__(self) -> None:
#         self.c = Circle(150, 150, 9, 3)
#         self.segments = [(vertices[i], vertices[(i + 1) % n]) for i in range(n)]
#         self.flattern_segments = list(chain.from_iterable(self.segments))
#
#         self.projected_point = None
#         self.current_segment = None
#
#         self.c.apply_force(Vector(0.0, 1))
#
#     def normalize(self, P, NearestP):
#         dx = P.x - NearestP.x
#         dy = P.y - NearestP.y
#
#         length = math.hypot(dx, dy)
#
#         if length < 1e-9:
#             return Vector()
#
#         return Vector(dx / length, dy / length)
#
#     def draw(self):
#         for v in self.segments:
#             a = v[0]
#             b = v[1]
#             pyxel.line(a.x, a.y, b.x, b.y, 10)
#         pyxel.circb(self.c.pos.x, self.c.pos.y, self.c.r, self.c.color)
#
#         # drawing the closest_point
#         if self.projected_point:
#             pyxel.line(
#                 self.c.x,
#                 self.c.y,
#                 self.projected_point.x,
#                 self.projected_point.y,
#                 8,
#             )
#
#         if self.current_segment:
#             A, B = self.current_segment
#             pyxel.line(A.x, A.y, B.x, B.y, 11)
#
#     def update(self):
#         best_segment = None
#         min_dist = float("inf")
#         # finding the nearest segment
#         for A, B in self.segments:
#             d = Geometry.distance_point_to_segment_sq(self.c, A, B)
#
#             if d < min_dist:
#                 min_dist = d
#                 best_segment = (A, B)
#
#         if best_segment:
#             A, B = best_segment
#             self.current_segment = best_segment
#
#             self.best_point_on_segment = A
#             closest = Geometry.closest_point_on_segment(self.c, A, B)
#             self.projected_point = closest
#
#             if min_dist <= self.c.r * self.c.r:
#                 # normal ( C - P)
#                 nx = self.c.x - closest.x
#                 ny = self.c.y - closest.y
#
#                 length = math.hypot(nx, ny)
#
#                 if length > 1e-9:
#                     nx /= length
#                     ny /= length
#
#                     # Dot product
#                     dot = self.c.vel.x * nx + self.c.vel.y * ny
#
#                     if dot < 0:
#                         self.c.vel.x -= 2 * dot * nx
#                         self.c.vel.y -= 2 * dot * ny
#
#                         # penetration correction
#                         self.c.pos.x = closest.x + nx * self.c.r
#                         self.c.pos.y = closest.y + ny * self.c.r
#
#         # move the circle
#         self.c.update()


# This is ChatGpt Code :0
class NormalVectorAndReflection:
    def __init__(self):
        self.circle = Circle(150, 150, 9, 3)
        self.circle.vel = Vector(2, 3)
        self.segments = [(vertices[i], vertices[(i + 1) % n]) for i in range(n)]

    def update(self):
        # aplicar colisiones contra todos los segmentos
        for A, B in self.segments:
            self.circle.resolve_collision_with_segment(A, B)

        self.circle.update()

    def draw(self):
        for A, B in self.segments:
            pyxel.line(A.x, A.y, B.x, B.y, 10)

        pyxel.circb(self.circle.x, self.circle.y, self.circle.r, self.circle.color)
