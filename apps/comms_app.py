# import time
# from machine import UART, Pin

# def run(oled):
#     uart = UART(0, baudrate=9600, tx=Pin(16), rx=Pin(17))
#     oled.fill(0)
#     oled.text("Comms Module", 0, 0)
#     oled.text("Listening...", 0, 20)
#     oled.show()

#     while True:
#         if uart.any():
#             msg = uart.readline().decode().strip()
#             oled.fill(0)
#             oled.text("Received:", 0, 0)
#             oled.text(msg, 0, 20)
#             oled.show()
#             time.sleep(2)
#         if Pin(15, Pin.IN, Pin.PULL_UP).value() == 0:
#             break
