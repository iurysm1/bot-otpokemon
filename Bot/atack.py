import pyautogui
import pyscreeze
import time
from helper import monstro_no_battle
from coordenadas import BATTLE

hotkey_list = ['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12']


def atack(x,y):
    #pyautogui.click(x,y)
    time.sleep(1)
    for i in range(3):
        for key in hotkey_list:
                pyautogui.press(key)



def init_bot():
    if monstro_no_battle()==True:
        atack(BATTLE)  
    else:
        locate=monstro_no_battle()
    time.sleep(0.5) 









