import board
import time
from send_key import *
from digitalio import DigitalInOut, Direction, Pull

# init the up button
up_btn = DigitalInOut(board.GP4)
up_btn.direction = Direction.INPUT
up_btn.pull = Pull.DOWN

# init the left button
left_btn = DigitalInOut(board.GP8) 
left_btn.direction = Direction.INPUT
left_btn.pull = Pull.DOWN

# init the down button
down_btn = DigitalInOut(board.GP2)
down_btn.direction = Direction.INPUT 
down_btn.pull = Pull.DOWN

# init the right button
right_btn = DigitalInOut(board.GP6)
right_btn.direction = Direction.INPUT
right_btn.pull = Pull.DOWN

# init the reset button
reset_btn = DigitalInOut(board.GP10)
reset_btn.direction = Direction.INPUT
reset_btn.pull = Pull.DOWN

while True:
    if up_btn.value:
        send_key_z()
    elif left_btn.value:
        send_key_q()
    elif down_btn.value:
        send_key_s()
    elif right_btn.value:
        send_key_d()
    elif reset_btn.value:
        send_key_r()
    else:
        continue
    time.sleep(0.3)
