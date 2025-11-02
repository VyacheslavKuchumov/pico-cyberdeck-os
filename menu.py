from machine import Pin
import time
from controls import Controls

class Menu:
    def __init__(self, oled, apps):
        self.oled = oled
        self.apps = apps
        self.index = 0
        self.controls = Controls()

    def draw(self):
        self.oled.fill(0)
        self.oled.text("== Main Menu ==", 0, 0)
        for i, (name, _) in enumerate(self.apps):
            prefix = ">" if i == self.index else " "
            self.oled.text(f"{prefix} {name}", 0, 12 + i*10)
        self.oled.show()

    def run(self):
        self.draw()
        while True:
            if not self.controls.btn_up.value():
                self.index = (self.index - 1) % len(self.apps)
                self.draw()
                time.sleep(0.2)
            if not self.controls.btn_down.value():
                self.index = (self.index + 1) % len(self.apps)
                self.draw()
                time.sleep(0.2)
            if not self.controls.btn_select.value():
                _, func = self.apps[self.index]
                func(self.oled)
                self.draw()
