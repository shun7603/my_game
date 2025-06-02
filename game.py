import pyxel

class App:
    def __init__(self):
        pyxel.init(160, 120, title="サプーゲーム")
        pyxel.mouse(True)
        self.number = 0
        pyxel.run(self.update, self.draw)

    def update(self):
       if pyxel.btnp(pyxel.KEY_ESCAPE):
           pyxel.quit()

    def draw(self):
        pyxel.cls(pyxel.COLOR_DARK_BLUE)
        pyxel.text(70, 60, f"{self.number}", pyxel.COLOR_YELLOW)
        pyxel.text(30, 60, "-", pyxel.COLOR_WHITE)
        pyxel.text(110, 60, "+", pyxel.COLOR_WHITE)

App()