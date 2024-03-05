import pyautogui
import pyscreeze

X_CLICK=877
Y_CLICK=629
CLICK_POSITION=(877,629)
RGB_CLICK=(66, 115,  41)

X_TARGET=1744
Y_TARGET=688

close_position=(1903,796)

loot_positon=(1750,820)
X_LOOT=1853
Y_LOOT=798
RGB_LOOT=(11,  17,  35)

X_ATAQUE=1730
Y_ATAQUE=473
ATAQUE_POSITION=(1730,473)
RGB_ATAQUE=(255,  255,  255)

hotkey_list=['f1','f2','f3','f4','f5','f6','f7','f8','f9','f10','f11','f12']

def get_target():
    get_loot()
    pyautogui.sleep(2.5)
    pyautogui.moveTo(X_ATAQUE,Y_ATAQUE)


def get_loot():   
    pyautogui.click(loot_positon,clicks=5)
    pyautogui.sleep(1)
    pyautogui.click(close_position)

    
def atack():
     pyautogui.press(hotkey_list)

while True:
    

    target= pyautogui.pixelMatchesColor(X_ATAQUE, Y_ATAQUE, RGB_ATAQUE)
    if target:
        pyautogui.click(ATAQUE_POSITION)
        pyautogui.sleep(0.5)
        atack()
        pyautogui.sleep(2)
        pyautogui.click(CLICK_POSITION, button='right') 
        pyautogui.sleep(3)
        get_target()