import pyxel
import math


class Pytagoras:
    def distance(self, p1, p2):
        x1, y1 = p1
        x2, y2 = p2

        dx = x2 - x1
        dy = y2 - y1

        distance = math.sqrt(dx * dx + dy * dy)
        return distance

    def distance_sq(self, p1, p2):
        x1, y1 = p1
        x2, y2 = p2

        dx = x2 - x1
        dy = y2 - y1

        return dx * dx + dy * dy

    def is_inside_circle(self, center, point, radius):
        return self.distance_sq(center, point) <= radius * radius


class Plane:
    def __init__(self):
        self.p1 = (10, 30)
        self.p2 = (80, 140)
        self.pytagoras = Pytagoras()

        self.center = (80, 80)
        self.radius = 20

    def draw(self):
        pyxel.cls(0)

        x1, y1 = self.p1
        x2, y2 = self.p2

        dx = x2 - x1
        dy = y2 - y1

        # cateto 1
        pyxel.line(x1, y1, x1 + dx, y1, 9)
        # cateto 2
        pyxel.line(x2, y1 + dy, x2, y1, 10)

        pyxel.line(x1, y1, x2, y2, 8)

        pyxel.pset(x1, y1, 7)
        pyxel.pset(x2, y2, 7)

        # drawing a line between the two points
        d = self.pytagoras.distance(self.p1, self.p2)

        pyxel.text((x2 + x1) // 2, (y2 + y1) // 2, f"dist: {d:.2f}", 7)

        # drawing the circle.
        cx, cy = self.center
        pyxel.circb(cx, cy, self.radius, 7)

        point = (pyxel.mouse_x, pyxel.mouse_y)
        px, py = point

        # line from the center of the circle and the point (mouse)
        pyxel.line(cx, cy, px, py, 5)
        inside = self.pytagoras.is_inside_circle(self.center, point, self.radius)

        # drawing the point to check if is inside or not
        color = 11 if inside else 8
        text = "is colliding at:" if inside else ""

        pyxel.pset(px, py, color)
        pyxel.text(px, py, f"{text} ({px}, {py})", color)

    def update(self):
        # print(self.distance(p1, p2))
        pass
