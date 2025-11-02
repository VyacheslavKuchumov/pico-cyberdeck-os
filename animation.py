import time

def boot_animation(oled):
    oled.fill(0)
    text = "Sluvik's\nPico Cyberdeck"
    lines = text.split('\n')

    # Slide-in effect from right to left
    for offset in range(128, -1, -8):
        oled.fill(0)
        for i, line in enumerate(lines):
            oled.text(line, offset, 16 + i*10)
        oled.show()
        time.sleep(0.05)

    # Small blinking cursor effect
    for _ in range(3):
        oled.text("_", 110, 40)
        oled.show()
        time.sleep(0.3)
        oled.fill_rect(110, 40, 8, 8, 0)
        oled.show()
        time.sleep(0.3)

    time.sleep(0.5)
    oled.fill(0)
    oled.show()
