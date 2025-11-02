import time
from machine import I2C, Pin
from lib.ds3231 import RTC  
from controls import Controls

def run(oled):
    
    rtc = RTC(sda_pin=2, scl_pin=3, port=1)
    controls = Controls()

    while True:
        oled.fill(0)
        current_time = rtc.DS3231_ReadTime(mode=1)
        oled.text("Clock App", 0, 0)
        oled.text(current_time, 22, 30)
        oled.show()
        time.sleep(0.2)
        # Exit on CANCEL press
        if not controls.btn_cancel.value():
            break
