import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
import time

time.sleep(1)
keyboard = Keyboard(usb_hid.devices)
#developed by @hevorix
def open_run_window():
    keyboard.press(Keycode.WINDOWS)  
    time.sleep(0.1)
    keyboard.press(Keycode.R)       
    time.sleep(0.1)
    keyboard.release_all()          


def type_text(text):
    for char in text:
        if char.isupper():
            keyboard.press(Keycode.SHIFT, getattr(Keycode, char.upper()))
        elif char.islower():
            keyboard.press(getattr(Keycode, char.upper()))
        elif char == ":":
            keyboard.press(Keycode.SHIFT, Keycode.SEMICOLON)
        elif char == "/":
            keyboard.press(Keycode.FORWARD_SLASH)
        elif char == ".":
            keyboard.press(Keycode.PERIOD)
        elif char == "-":
            keyboard.press(Keycode.MINUS)
        else: 
            keyboard.press(getattr(Keycode, char.upper(), Keycode.SPACE))
        keyboard.release_all()

def open_cmd_and_run():
    open_run_window()
    time.sleep(0.5)
    type_text("cmd")
    time.sleep(0.5)
    keyboard.press(Keycode.ENTER)
    keyboard.release_all()
    time.sleep(1)
    type_text("curl ascii.live/forrest")
    time.sleep(0.5)
    keyboard.press(Keycode.ENTER)
    keyboard.release_all()

time.sleep(5)
open_cmd_and_run()
