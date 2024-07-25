import pyautogui


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
