from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

# Initialize I2C on Pico
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=200000)

print("I2C devices:", [hex(addr) for addr in i2c.scan()])

# Create display object (adjust addr if scan shows 0x3d)
oled = SSD1306_I2C(128, 64, i2c, addr=0x3C)

# Test output
oled.fill(0)
oled.text("Hello, Pico!", 0, 0)
oled.text("SSD1306 OK", 0, 10)
oled.show()
