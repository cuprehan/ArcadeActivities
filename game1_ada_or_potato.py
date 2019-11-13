import arcade

# Define constants
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
BACKGROUND_COLOR = arcade.color.BLACK
GAME_TITLE = "Ada or Potato"
GAME_SPEED = 1/60

TIMER_MAXIMUM = 100

ADA_IMAGE = arcade.load_texture("images/ada.png", scale=.5)
POTATO_IMAGE = arcade.load_texture("images/potato.png", scale=.5)

class Ada_Or_Potato(arcade.Window):
    sprites: arcade.SpriteList
    score: int

    def __init__(self):
        """ Initialize variables """
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, GAME_TITLE)
        self.logo_list = None
        self.score = 0
        self.timer = 0

    def setup(self):
        """ Setup the game (or reset the game) """
        arcade.set_background_color(BACKGROUND_COLOR)
        self.score = 0
        self.logo_list = arcade.SpriteList()
        self.logo_list.append(ada())
        self.logo_list.append(potato())

    def on_draw(self):
        """ Called when it is time to draw the world """
        arcade.start_render()
        self.logo_list.draw()
        score = self.score
        score = str(score)
        arcade.draw_text("Your score:" + score, 10, 20, arcade.color.WHITE, 14)

    def on_update(self, delta_time):
        """ Called every frame of the game (1/GAME_SPEED times per second)"""
        self.logo_list.update()
        self.timer = self.timer + (1/60)

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        if 1 <= self.timer % 2 < 2:
            self.score = self.score + 1
        else:
            self.score = self.score - 1


class ada(arcade.Window):
    def __init__(self):
        """ Initialize variables """
        super().__init__("images/ada.png")
        

    def on_update(self, delta_time):
        """ Called every frame of the game (1/GAME_SPEED times per second)"""

class potato(arcade.Window):
    def __init__(self):
        """ Initialize variables """
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, GAME_TITLE)

    def on_update(self, delta_time):
        """ Called every frame of the game (1/GAME_SPEED times per second)"""

def main():
    window = Ada_Or_Potato()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
