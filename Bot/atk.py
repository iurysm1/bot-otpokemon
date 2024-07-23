from pynput import keyboard
import pyautogui
import threading
import time

hotkey_list = ['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12']
ativo = False
current_keys = set()
combination = {keyboard.KeyCode(char='z'), keyboard.KeyCode(char='x'), keyboard.KeyCode(char='c')}

X_TARGET=1729
Y_TARGET=490
RGB_ATAQUE=(27,  28,  25)
locate = (1725, 360, 194, 159)
target= pyautogui.pixelMatchesColor(X_TARGET, Y_TARGET, RGB_ATAQUE)


def check_is_attacking():
    return pyautogui.locateOnScreen('imgs/atacking.png')

def ataque():
    while ativo:
        pyautogui.moveTo(X_TARGET, Y_TARGET)
        pyautogui.click()
        pyautogui.press(hotkey_list)
        time.sleep(1)

def on_combination():
    global ativo
    if ativo:
        ativo = False
    else:
        ativo = True
        thread = threading.Thread(target=ataque)
        thread.start()

def on_press(key):
    if key in combination:
        current_keys.add(key)
        if all(k in current_keys for k in combination):
            on_combination()

def on_release(key):
    try:
        current_keys.remove(key)
    except KeyError:
        pass

# Cria e inicia o listener do teclado
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
