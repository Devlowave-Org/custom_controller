import board
from digitalio import DigitalInOut, Direction, Pull


class Button:
    def __init__(self, pin):
        self.pin = pin
        self.btn = DigitalInOut(self.pin)
        self.btn.direction = Direction.INPUT
        self.btn.pull = Pull.UP
