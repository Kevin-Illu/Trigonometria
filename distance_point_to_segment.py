from geometry import Geometry, Point
import pyxel


class DistancePointToSegment:
    def __init__(self):
        self.g = Geometry()
        e = 30
        self.pa = Point(1 * e, 1 * e)
        self.pb = Point(5 * e, 5 * e)
        self.p = Point(13 * e, 5 * e)
        self.closest_point = Point(0, 0)

    def draw(self):
        # drawing the distance between the A and P
        dx = self.p.x - self.pa.x
        dy = self.p.y - self.pa.y
        pyxel.line(self.pa.x, self.pa.y, self.pa.x + dx, self.pa.y + dy, 5)

        # line between A and B
        pyxel.line(self.pa.x, self.pa.y, self.pb.x, self.pb.y, 10)

        # drawing the closest_point
        if self.closest_point is not None:
            # line
            pyxel.line(
                self.p.x, self.p.y, self.closest_point.x, self.closest_point.y, 9
            )

            # point
            pyxel.pset(int(self.closest_point.x), int(self.closest_point.y), 8)

        # Points
        pyxel.pset(self.pa.x, self.pa.y, 8)
        pyxel.pset(self.pb.x, self.pb.y, 8)
        pyxel.pset(self.p.x, self.p.y, 9)

        # Debug visual
        d = self.g.distance_point_to_segment_sq(self.p, self.pa, self.pb)
        pyxel.text(5, 5, f"d^2: {int(d)}", 7)

    def update(self):
        self.p.x = pyxel.mouse_x
        self.p.y = pyxel.mouse_y

        closest_x, closest_y = self.g.closest_point_on_segment(self.p, self.pa, self.pb)
        self.closest_point.x = int(closest_x)
        self.closest_point.y = int(closest_y)
