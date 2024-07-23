import pyautogui
import pyscreeze
import time
locate = (1629, 538, 291, 91)
px,py=1102,521

#pyautogui.displayMousePosition()
hotkey_list = ['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12']


def monstro_no_battle():
     try:
        locate=pyautogui.locateOnScreen("imgs/battle_box.png", confidence=0.9)
        print('Sem monstros no battle')
        left = int(locate.left)
        top = int(locate.top)
        width = int(locate.width)
        height = int(locate.height)
        
        locate_int = (left, top, width, height)

        return locate_int
     except pyautogui.ImageNotFoundException:
        print('Monstros no battle')
        return True

def atack(x,y):
    pyautogui.moveTo(x,y)
    time.sleep(.5)
    pyautogui.click(x,y)
    for i in range(3):
        for key in hotkey_list:
                pyautogui.press(key)

cond = True
x,y=(1629,538)


while cond:
    
    if monstro_no_battle()==True:
        atack(1645,627)  
    else:
        locate=monstro_no_battle()
        pyautogui.hotkey('shift', 'f1')
        time.sleep(2.2)
        pyautogui.hotkey('shift', 'f1')

        pyautogui.click(px,py)
    time.sleep(0.5) 






