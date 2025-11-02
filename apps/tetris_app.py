import time

def run(oled):
    oled.fill(0)
    oled.text("Tetris launching...", 0, 20)
    oled.show()
    time.sleep(1)

    # TODO: implement Tetris logic here
    oled.fill(0)
    oled.text("Tetris Game", 0, 20)
    oled.show()
    time.sleep(2)
