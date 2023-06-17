import time
from board import *
import usb_hid
from adafruit_hid.mouse import Mouse
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from digitalio import DigitalInOut, Pull, Direction

# IO setup
led_pins = (GP16, GP19, GP20, GP26)
leds = []

for pin in led_pins:
    led = DigitalInOut(pin)
    led.direction = Direction.OUTPUT
    led.value = False
    leds.append(led)

btn_switch = DigitalInOut(GP4)
btn1 = DigitalInOut(GP8)
btn2 = DigitalInOut(GP12)

btn_switch.direction = Direction.INPUT
btn_switch.pull = Pull.UP
btn1.direction = Direction.INPUT
btn1.pull = Pull.UP
btn2.direction = Direction.INPUT
btn2.pull = Pull.UP

mouse = Mouse(usb_hid.devices)
kbd = Keyboard(usb_hid.devices)

# var init
init_ts = int(time.monotonic())
time_elapsed = 0

############################################
# mode behaviors
############################################

def mode0_func():
    if not btn1.value:
        while not btn1.value:
            time.sleep(0.01)
        kbd.press(Keycode.LEFT_ARROW)
        kbd.release(Keycode.LEFT_ARROW)
    
    if not btn2.value:
        while not btn2.value:
            time.sleep(0.01)
        kbd.press(Keycode.RIGHT_ARROW)
        kbd.release(Keycode.RIGHT_ARROW)

def mode1_func():
    # TODO: add your own code for mode1
    pass


def mode2_func():
    # TODO: add your own code for mode2
    pass


def mode3_func():
    # TODO: add your own code for mode3
    pass

funcs = [
    mode0_func,
    mode1_func,
    mode2_func,
    mode3_func,
]


mode = 0
leds[mode].value = True


while True:
    # update time_elapsed
    ts = int(time.monotonic())
    time_elapsed = ts - init_ts
    
    if not btn_switch.value:
        while not btn_switch.value:
            time.sleep(0.01)
        
        leds[mode].value = False
        mode = mode + 1
        if mode == len(leds):
            mode = 0
        leds[mode].value = True
        
        continue
    
    funcs[mode]()
        
    time.sleep(0.1)
        