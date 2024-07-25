import pyautogui
import pyscreeze
import time
from helper import monstro_no_battle
from coordenadas import PESCA


locate = (1629, 538, 291, 91)
px,py=1333,363


#pyautogui.displayMousePosition()
hotkey_list = ['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12']



def atack_pesca(x,y):
    pyautogui.moveTo(x,y)
    time.sleep(.5)
    pyautogui.click(x,y)
    for i in range(3):
        for key in hotkey_list:
                pyautogui.press(key)


def init_bot_pesca():
    if monstro_no_battle()==True:
        atack_pesca(1741,421)  
    else:
        locate=monstro_no_battle()
        pyautogui.hotkey('shift', 'f1')
        time.sleep(2.2)
        pyautogui.hotkey('shift', 'f1')

        pyautogui.click(PESCA)
    time.sleep(0.5) 
