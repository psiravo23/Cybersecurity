import sys
import pynput

from pynput.keyboard import Key, Listener

keysPressed = []

def on_press(key):
    global keysPressed

    if key == Key.esc:
        return False

    keysPressed.append(key)

def create_file(keysPressed):
    

with Listener(on_press=on_press) as listener:
    listener.join()
