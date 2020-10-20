# Import
import keyboard
import time

# Variables
timesSpammed = 0

# Epic Gamer Code
time.sleep(10)

while True:
    time.sleep(2)
    keyboard.press_and_release('h+e+h+e')
    keyboard.press_and_release('enter')
    timesSpammed = timesSpammed + 1
    print("Times Spammed:", timesSpammed)