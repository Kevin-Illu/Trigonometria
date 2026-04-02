import pyxel
from geometry import Point, Geometry


class NearestPoint:
    def __init__(self):
        self.g = Geometry()
        self.target = Point(0, 0)
        self.points = [Point() for i in range(10)]
        self.nearest_point = self.get_nearest_point(self.target, self.points)

    def get_nearest_point(self, target, points):
        nearest = points[0]
        current_nearest_distance = self.g.distance_sq(target, nearest)

        for point in points[1:]:
            distance = self.g.distance_sq(target, point)

            if distance < current_nearest_distance:
                current_nearest_distance = distance
                nearest = point

        return nearest

    def draw(self):
        # line to the nearest
        pyxel.line(
            self.target.x, self.target.y, self.nearest_point.x, self.nearest_point.y, 8
        )

        # draw the target
        pyxel.pset(self.target.x, self.target.y, 10)

        # draw the points
        for p in self.points:
            color = 3
            if p is self.nearest_point:
                color = 11
            pyxel.pset(p.x, p.y, color)

        # highlight del nearest
        pyxel.pset(self.nearest_point.x, self.nearest_point.y, 11)

        d = self.g.distance_sq(self.target, self.nearest_point)
        pyxel.text(5, 5, f"d^2: {d}", 7)

    def update(self):
        self.target.x = pyxel.mouse_x
        self.target.y = pyxel.mouse_y

        self.nearest_point = self.get_nearest_point(self.target, self.points)
