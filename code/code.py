import time
import board
import buttons
from send_key import *

# create the buttons
up = buttons.Button(board.PIN)
left = buttons.Button(board.PIN)
down = buttons.Button(board.PIN)
right = buttons.Button(board.PIN)
reset = buttons.Button(board.PIN)

while True:
    if not up.btn.value:
        send_key_z()
    elif not left.btn.value:
        send_key_q()
    elif not down.btn.value:
        send_key_s()
    elif not right.btn.value:
        send_key_d()
    elif not reset.btn.value:
        send_key_r()
    else:
        pass
    
    time.sleep(0.1)
