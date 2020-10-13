# Import
import keyboard
import time

# Variables
timesReloaded = 0

# Epic Gamer Code
while True:
    time.sleep(6)
    keyboard.press('ctrl')
    keyboard.press('r')
    keyboard.release('ctrl')
    keyboard.release('r')
    timesReloaded = timesReloaded + 1
    print("Reload Number", timesReloaded, "Complete!")