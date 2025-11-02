# import time
# from machine import I2C, Pin
# from lib.ds3231 import DS3231  # You must have this driver

# def run(oled):
#     i2c = I2C(1, scl=Pin(3), sda=Pin(2))
#     rtc = DS3231(i2c)

#     while True:
#         oled.fill(0)
#         dt = rtc.datetime()
#         oled.text("Clock App", 0, 0)
#         oled.text(f"{dt[4]:02d}:{dt[5]:02d}:{dt[6]:02d}", 20, 30)
#         oled.text("Press SELECT to exit", 0, 56)
#         oled.show()
#         time.sleep(1)
#         # Exit on SELECT press
#         if Pin(15, Pin.IN, Pin.PULL_UP).value() == 0:
#             break
