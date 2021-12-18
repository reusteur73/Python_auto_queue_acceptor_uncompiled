import requests
from time import sleep
import time
import pyautogui
import os
from os.path import join, dirname
from dotenv import load_dotenv
import sys
from colorama import init
from termcolor import colored

# use Colorama to make Termcolor work on Windows too
init()

print(colored('LoL match accept By Reu$: https://www.github.com/reusteur73', 'green'))

image_url = "http://www.reusteur.org/hRDz3fWn/en.png"
img_data1 = requests.get(image_url).content
with open('en2.png', 'wb') as handler:
    handler.write(img_data1)
print(colored('Preparing files (1/3)', 'yellow'))
image_url2 = "http://www.reusteur.org/hRDz3fWn/btnfr.png"
img_data2 = requests.get(image_url2).content
with open('btnfr.png', 'wb') as handler:
    handler.write(img_data2)
print(colored('Preparing files (2/3)', 'yellow'))
image_url3 = "http://www.reusteur.org/hRDz3fWn/pt.png"
img_data3 = requests.get(image_url3).content
with open('pt.png', 'wb') as handler:
    handler.write(img_data3)
print(colored('Preparing files (Done)', 'yellow'))


def click(x, y):
    pyautogui.click(x, y)


def check_screen():
    button = pyautogui.locateOnScreen('en2.png', confidence=0.7)
    buttonFr = pyautogui.locateOnScreen('btnfr.png', confidence=0.7)
    buttonPt = pyautogui.locateOnScreen('pt.png', confidence=0.7)

    if button != None:
        click(button.left, button.top)
        return True
    
    if buttonFr != None:
        click(buttonFr.left, buttonFr.top)
        return True

    if buttonPt != None:
        click(buttonPt.left, buttonPt.top)
        return True


while True:
    try:
        print(colored('Waiting for match...                   press ctrl+C to pause', 'yellow'))
        sleep(3)
        if check_screen():
            print(colored('Match accepted!', 'green'))
            sleep(6)
    except KeyboardInterrupt:
        print(colored('\nPausing...  (Hit ENTER to continue, type ctrl+C to exit.)', 'red'))
        try:
            response = input()
            if response == 'quit':
                break
            print(colored('Resuming...', 'green'))
        except KeyboardInterrupt:
            print(colored('Resuming...', 'green'))
            continue

