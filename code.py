from machine import Pin
from send_key import *

button = Pin(14, Pin.IN, Pin.PULL_DOWN)

while True:
    if button.value():
        send_key_z()