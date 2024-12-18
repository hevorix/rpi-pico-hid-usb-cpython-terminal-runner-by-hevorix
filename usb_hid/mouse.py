import usb_hid
from adafruit_hid.mouse import Mouse
import time
import math
#hevorix
mouse = Mouse(usb_hid.devices)

def move_in_circle(radius=10, steps=360):
    for angle in range(0, steps):
        x = int(radius * math.cos(math.radians(angle)))
        y = int(radius * math.sin(math.radians(angle)))
        mouse.move(x, y)
        time.sleep(0.01) 
time.sleep(1)

move_in_circle(radius=10, steps=360) 
