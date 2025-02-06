import keyboard
import pydirectinput as pid
from time import sleep as wait

def forage(g_press_num:int = 5):
    for _ in range(g_press_num):
        keyboard.press("G")
        wait(0.1)
    
    pid.press("DOWN")
    wait(0.5)
    

if __name__ == "__main__":
    wait(5)
    while not keyboard.is_pressed("O"):
        forage()
