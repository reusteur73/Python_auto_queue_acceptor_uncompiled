from time import sleep
import pyautogui
import os
from os.path import join, dirname
from dotenv import load_dotenv



def click(x, y):
    pyautogui.click(x, y)


def check_screen():
    button = pyautogui.locateOnScreen('ABSOLUTE_PATH_TO/queue_acceptor/en.png', confidence=0.7)
    buttonPt = pyautogui.locateOnScreen('ABSOLUTE_PATH_TO/queue_acceptor/pt.png', confidence=0.7)

    if button != None:
        click(button.left, button.top)
        return True

    if buttonPt != None:
        click(buttonPt.left, buttonPt.top)
        return True

    return False
print('Waiting for match...')
while True:
    if check_screen():
        print('Match accepted.')
        sleep(6)

