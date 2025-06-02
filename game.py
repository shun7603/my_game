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
           
       if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
          if 20 <= pyxel.mouse_x <= 40 and 50 <= pyxel.mouse_y <= 70:
                self.number -= 1
          elif 100 <= pyxel.mouse_x <= 120 and 50 <= pyxel.mouse_y <= 70:
                 self.number += 1
           
    def draw(self):
        pyxel.cls(pyxel.COLOR_DARK_BLUE)
        pyxel.text(70, 60, f"{self.number}", pyxel.COLOR_YELLOW)
        pyxel.text(30, 60, "-", pyxel.COLOR_WHITE)
        pyxel.text(110, 60, "+", pyxel.COLOR_WHITE)

App()