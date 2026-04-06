import pyxel

from circle_vs_segment_collisions import CircleVSSegmentCollisions
from circles import Circles
from distance_point_to_segment import DistancePointToSegment
from nearest_point import NearestPoint
from normal_vector_and_reflection import NormalVectorAndReflection
from triangulos_circulos import Triangulo1
from triangulos_2 import Triangulos2


planes = [
    NormalVectorAndReflection,
    CircleVSSegmentCollisions,
    DistancePointToSegment,
    Circles,
    NearestPoint,
    Triangulos2,
    Triangulo1,
]
currentPlane = planes[0]


class App:
    def __init__(self):
        pyxel.init(255, 255, title="Lab1")
        pyxel.mouse(True)
        self.plane = currentPlane()
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        self.plane.update()

    def draw(self):
        pyxel.cls(0)
        pyxel.text(100, 250, "Presiona Q para salir", 7)

        self.plane.draw()


App()
