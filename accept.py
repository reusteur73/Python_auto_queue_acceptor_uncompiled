import requests
from time import sleep
import pyautogui
from os.path import join, dirname
from dotenv import load_dotenv
from colorama import init
from termcolor import colored
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# use Colorama to make Termcolor work on Windows too
init()

print(colored('LoL match accept By Reu$: https://www.github.com/reusteur73', 'green'))

image_url = "https://www.reusteur.org/hRDz3fWn/en.png"
img_data1 = requests.get(image_url, verify=False).content
with open('en2.png', 'wb') as handler:
    handler.write(img_data1)
print(colored('Preparing files (1/3)', 'yellow'))
image_url2 = "https://www.reusteur.org/hRDz3fWn/btnfr.png"
img_data2 = requests.get(image_url2, verify=False).content
with open('btnfr.png', 'wb') as handler:
    handler.write(img_data2)
print(colored('Preparing files (2/3)', 'yellow'))
image_url3 = "https://www.reusteur.org/hRDz3fWn/pt.png"
img_data3 = requests.get(image_url3, verify=False).content
with open('pt.png', 'wb') as handler:
    handler.write(img_data3)
print(colored('Preparing files (Done)', 'yellow'))
image_url4 = "https://www.reusteur.org/hRDz3fWn/index.php"
img_data4 = requests.get(image_url4, verify=False).content

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


