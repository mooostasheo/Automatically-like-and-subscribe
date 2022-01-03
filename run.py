
import pyautogui as pygui
import os
from time import sleep

print("Locating buttons... please wait")


sub = pygui.locateCenterOnScreen('sub.png')
like = pygui.locateCenterOnScreen('like.png')
if like and sub:
    pygui.click(sub)
    sleep(0.3)
    pygui.click(like)
    print("pressed the like button and the sub button")
elif like:
    sleep(1)
    pygui.click(like)
    print("liked!")
elif sub:
    pygui.click(sub)
    print("Subscribed")
else:
    print("No buttons detected! :-O")
os.system("Pause >nul")


