from machine import Pin
class Controls:
    def __init__(self):
        
        self.btn_up = Pin(15, Pin.IN, Pin.PULL_UP)
        self.btn_down = Pin(14, Pin.IN, Pin.PULL_UP)
        self.btn_select = Pin(16, Pin.IN, Pin.PULL_UP)
        self.btn_cancel = Pin(17, Pin.IN, Pin.PULL_UP)