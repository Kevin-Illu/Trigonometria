import math
import random


class Geometry:
    def distance_sq(self, p1, p2):
        dx = p2.x - p1.x
        dy = p2.y - p1.y

        return dx * dx + dy * dy

    def distance_sqrt(self, p1, p2):
        return math.sqrt(self.distance_sq(p1, p2))

    def get_nearest_point(self, target, points):
        nearest = points[0]
        current_nearest_distance = self.distance_sq(target, nearest)

        for point in points[1:]:
            distance = self.distance_sq(target, point)

            if distance < current_nearest_distance:
                current_nearest_distance = distance
                nearest = point

        return nearest

    def closest_point_on_segment(self, P, A, B):
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

        return (closest_x, closest_y)

    def distance_point_to_segment_sq(self, P, A, B):
        cx, cy = self.closest_point_on_segment(P, A, B)

        dx = P.x - cx
        dy = P.y - cy

        return dx * dx + dy * dy


class Point:
    def __init__(self, x=None, y=None, color=None):
        self.x = x if x is not None else random.randint(0, 255)
        self.y = y if y is not None else random.randint(0, 255)
        self.color = color if color is not None else random.randint(1, 10)


class Circle:
    def __init__(self, x=None, y=None, r=None, color=None):
        self.x = x if x is not None else random.randint(10, 250)
        self.y = y if y is not None else random.randint(10, 250)
        self.r = r if r is not None else random.randint(1, 5)
        self.color = color if color is not None else random.randint(5, 11)
        self.colliding = False
        self.g = Geometry()

    def is_colliding_with_circle(self, circle):
        r_sum = self.r + circle.r
        return self.g.distance_sq(self, circle) <= r_sum * r_sum

    def is_colliding_with_segment(self, A, B):
        x, y = self.g.closest_point_on_segment(self, A, B)
        return self.g.distance_sq(self, Point(x, y)) <= self.r * self.r
