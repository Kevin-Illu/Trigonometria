import pyxel
from geometry import Circle, Geometry, Point


class CircleVSSegmentCollisions:
    def __init__(self):
        self.e = 20
        self.g = Geometry()
        self.c = Circle(5 * self.e, 5 * self.e, 1 * self.e, 10)
        self.pa = Point(2 * self.e, 2 * self.e, 2)
        self.pb = Point(10 * self.e, 2 * self.e, 2)

        x, y = self.g.closest_point_on_segment(self.c, self.pa, self.pb)
        self.closest_point = Point(x, y, 6)

    def draw(self):
        c_color = 9

        if self.c.colliding:
            c_color = 8

        # projection
        pyxel.line(
            self.closest_point.x,
            self.closest_point.y,
            self.c.x,
            self.c.y,
            c_color,
        )

        pyxel.circb(self.c.x, self.c.y, self.c.r, c_color)

        pyxel.line(self.pa.x, self.pa.y, self.pb.x, self.pb.y, 3)
        pyxel.pset(self.pa.x, self.pa.y, self.pa.color)
        pyxel.pset(self.pb.x, self.pb.y, self.pb.color)

    def update(self):
        self.c.colliding = False

        self.c.x = pyxel.mouse_x
        self.c.y = pyxel.mouse_y

        x, y = self.g.closest_point_on_segment(self.c, self.pa, self.pb)
        self.closest_point.x = int(x)
        self.closest_point.y = int(y)

        self.c.colliding = self.c.is_colliding_with_segment(self.pa, self.pb)
