## Tell mouse position after certain period of time
from pynput.mouse import Controller
import time

#def position():
mouse = Controller()
 # Read pointer position
 #return mouse.position

while True:
    print(mouse.position)
    time.sleep(1)
