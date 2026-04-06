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

        pyxel.circb(
            round(self.circle.x),
            round(self.circle.y),
            round(self.circle.r),
            self.circle.color,
        )
