import pyautogui
import pyscreeze


X_TARGET=1744
Y_TARGET=688

close_position=(1904,793)

loot_positon=(1750,820)
X_LOOT=1903
Y_LOOT=796
RGB_LOOT=(224, 179,  75)


X_ATAQUE=1748
Y_ATAQUE=454
RGB_ATAQUE=(255,  0,  0)


hotkey_list=['f1','f2','f3','f4','f5','f6','f7','f8','f9','f10','f11','f12']


def get_loot():    
    pyautogui.click(loot_positon,clicks=5)
    pyautogui.click(close_position)


def atack():
     pyautogui.press(hotkey_list)



while True:
    loot= pyautogui.pixelMatchesColor(X_LOOT, Y_LOOT, RGB_LOOT)
    if loot:
        get_loot()

    target= pyautogui.pixelMatchesColor(X_ATAQUE, Y_ATAQUE, RGB_ATAQUE)
    if target:
        atack()


        




