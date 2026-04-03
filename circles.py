# colisionando.
from geometry import Circle, Geometry
import pyxel


# estan colisionando?
c1 = Circle(80, 190, 10)
c2 = Circle(79, 168, 20)

# no estan colisionando
c3 = Circle(80, 10, 39)
c4 = Circle(11, 90, 29)


class Circles:
    def __init__(self):
        self.circles = [c1, c2, c3, c4]
        self.g = Geometry()

    def draw(self):
        for c in self.circles:
            color = 8 if c.colliding else 4
            pyxel.circb(c.x, c.y, c.r, color)

    def update(self):
        for c1 in self.circles:
            c1.colliding = False

        for i in range(len(self.circles)):
            for j in range(i + 1, len(self.circles)):
                c1 = self.circles[i]
                c2 = self.circles[j]

                if c1.is_colliding(c2):
                    c1.colliding = True
                    c2.colliding = True
