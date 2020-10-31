## Tell mouse position after certain period of time
from pynput.mouse import Controller
import time
from screenshot import click_screenshot
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
        print("Clicking screenshot")
        click_screenshot()
    if x > 1348:
        print("you are going outside the screen")
        print("Clicking screenshot")
        click_screenshot()
    if y < 220:
        print("you are going outside the screen")
        print("Clicking screenshot")
        click_screenshot()
    if y > 888:
        print("you are going outside the screen")
        print("Clicking screenshot")
        click_screenshot()
    time.sleep(1)
