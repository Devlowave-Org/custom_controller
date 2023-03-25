import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# set the keys and change it from qwerty to azerty
key_z = Keycode.W
key_q = Keycode.A
key_s = Keycode.S
key_d = Keycode.D
keyboard = Keyboard(usb_hid.devices)


# the functions that send the keys
def send_key_z():
    keyboard.press(key_z)
    keyboard.release(key_z)

def send_key_q():
    keyboard.press(key_q)
    keyboard.release(key_q)

def send_key_s():
    keyboard.press(key_s)
    keyboard.release(key_s)

def send_key_d():
    keyboard.press(key_d)
    keyboard.release(key_d)
    
def send_key_r():
    keyboard.press(key_r)
    keyboard.release(key_r)


# this is for debugging :
# send_key_z()
# send_key_q()
# send_key_s()
# send_key_d()
# send_key_r()
