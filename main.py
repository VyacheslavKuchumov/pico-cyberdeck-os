from machine import Pin, I2C
from lib.ssd1306 import SSD1306_I2C
import time
from animation import boot_animation
from menu import Menu
from apps import clock_app, tetris_app, comms_app

# === Initialize I2C and OLED ===
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=200000)
oled = SSD1306_I2C(128, 64, i2c, addr=0x3C)

# === Boot animation ===
boot_animation(oled)

# === Define available apps ===
apps = [
    ("Clock", clock_app.run),  # Replace with clock_app.run
    ("Tetris", tetris_app.run),
    ("Stuff", print("Comms app placeholder")),  # Replace with comms_app.run
]

# === Create and show menu ===
menu = Menu(oled, apps)
menu.run()
