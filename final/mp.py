## Tell mouse position after certain period of time
from pynput.mouse import Controller
import time

#def position():
mouse = Controller()
 # Read pointer position
 #return mouse.position
time.sleep(10)
while True:
    print(mouse.position)
    x,y = mouse.position
    if x < 566:
        print("you are going outside the screen")
    if x > 1348:
        print("you are going outside the screen")
    if y < 220:
        print("you are going outside the screen")
    if y > 888:
        print("you are going outside the screen")
    time.sleep(1)
