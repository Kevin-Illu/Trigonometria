import pyxel

from triangulos_circulos import Triangulo1
from triangulos_2 import Triangulos2


planes = [Triangulos2, Triangulo1]
currentPlane = planes[0]


class App:
    def __init__(self):
        pyxel.init(255, 255, title="Lab1")

        self.plane = currentPlane()

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        self.plane.update()

    def draw(self):
        pyxel.cls(0)
        pyxel.text(5, 5, "Presiona Q para salir", 7)

        self.plane.draw()


App()
