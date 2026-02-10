from machine import Pin
import time
import neopixel

ir = Pin(15, Pin.IN)
buzzer = Pin(27, Pin.OUT)
np = neopixel.NeoPixel(Pin(4), 16)

active = 0

while True:
    ir_val = ir.value()

    if ir_val == 0 and active == 0:
        active = 1

        i = 0
        while i < 16:
            np[i] = (255, 0, 0)   
            np.write()

            buzzer.on()
            time.sleep(0.1)
            buzzer.off()

            time.sleep(0.15)
            i= i=1

        i = 0
        while i < 16:
            if i == 0:
                np[i] = (255, 0, 0)
            else:
                np[i] = (0, 0, 0)
            i= i + 1

        np.write()

    else:
        if ir_val == 1:
            active = 0

    time.sleep(0.05)

