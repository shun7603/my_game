import pyxel


SCREEN_WIDTH = 160
SCREEN_HEIGHT = 120

class App:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, title="サプーゲーム")
        pyxel.mouse(True)
        pyxel.load("my_resource.pyxres")
        self.player_x = SCREEN_WIDTH // 2
        pyxel.run(self.update, self.draw)

    def update(self):
       if pyxel.btnp(pyxel.KEY_ESCAPE):
           pyxel.quit()

       if pyxel.btn(pyxel.KEY_RIGHT) and self.player_x < SCREEN_WIDTH - 12:
           self.player_x += 1
       elif pyxel.btn(pyxel.KEY_LEFT) and self.player_x > -4:
           self.player_x -= 1

           
    def draw(self):
        pyxel.cls(pyxel.COLOR_DARK_BLUE)
        # 石
        pyxel.blt(SCREEN_WIDTH // 2, 0, 0 ,8, 0, 8, 8, pyxel.COLOR_BLACK)
        # プレーヤー
        pyxel.blt(self.player_x, SCREEN_HEIGHT * 4 // 5, 0, 16, 0, 16, 16, 
                  pyxel.COLOR_BLACK)

App()