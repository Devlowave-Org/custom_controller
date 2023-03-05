import time
import board
import buttons
from send_key import *

# create the buttons
up = buttons.Button(board.GP14)
left = buttons.Button(board.GP10)
down = buttons.Button(board.GP2)
right = buttons.Button(board.GP27)

while True:
    if not up.btn.value:
        send_key_z()
    elif not left.btn.value:
        send_key_q()
    elif not down.btn.value:
        send_key_s()
    elif not right.btn.value:
        send_key_d()
    else:
        pass
    
    time.sleep(0.1)
