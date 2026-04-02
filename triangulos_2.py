import pyxel
from geometry import Geometry, Point


class Triangulos2:
    def __init__(self):
        self.points_count = 10
        self.points = [Point() for i in range(self.points_count)]
        self.trigo = Geometry()

    def draw(self):
        # drawing the points
        for point in self.points:
            x, y, color = point.x, point.y, point.color
            pyxel.pset(x, y, color)

        half = self.points_count // 2

        # connecting points with lines
        for i in range(half):
            p1 = self.points[i]
            p2 = self.points[i + half]

            dx = p2.x - p1.x
            dy = p2.y - p1.y

            d = self.trigo.distance_sq(p1, p2)

            small = 1
            big = 6

            color = small if d < 20000 else big

            if d > 50000:
                color = 8

            # drawing the hipotenusa?
            # pyxel.line(p1.x, p1.y, p2.x, p2.y, color)

            # drawing the ady
            pyxel.line(p1.x, p1.y, p2.x, p1.y, 1)

            # drawing the op
            pyxel.line(p2.x, p1.y, p2.x, p2.y, 1)

            # drawing the vector
            pyxel.line(p1.x, p1.y, p1.x + dx, p1.y + dy, color)

    def update(self):
        pass
