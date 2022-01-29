from tkinter import E
import requests
from time import sleep
import pyautogui
from os.path import join, dirname
from dotenv import load_dotenv
from colorama import init
from termcolor import colored
import urllib3
import os
from tqdm import tqdm

# /* Define all languages *\
lang = ['en_EN', 'fr_FR', 'ja_JP', 'ru_RU','pt_BR', 'pl_PL', 'de_DE', 'es_ES', 'it_IT', 'hu_HU', 'cs_CZ']

def initialisation():

    # /* Settings *\
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    init()

    # /* Start of the program *\
    print(colored('╔╗──╔╗─╔═╦═╗──╔╗──╔╗─╔══╗───────╔╗', 'green'))
    print(colored('║║╔═╣║─║║║║╠═╗║╚╦═╣╚╗║╔╗╠═╦═╦═╦═╣╚╗', 'green'))
    print(colored('║╚╣╬║╚╗║║║║║╬╚╣╔╣═╣║║║╠╣║═╣═╣╩╣╬║╔╣ by Reu$', 'yellow'))
    print(colored('╚═╩═╩═╝╚╩═╩╩══╩═╩═╩╩╝╚╝╚╩═╩═╩═╣╔╩═╝https://github.com/reusteur73', 'yellow'))
    print(colored('──────────────────────────────╚╝LoL Match Accept ;D', 'red'))

    # /* Asking for language at first run *\
    if os.path.isfile('config.txt') == False:
        conf = open("config.txt","w+")
        print('\n'*5)
        print(colored("First run detected, please choose the language of your LoL game", 'blue'))
        print(colored("[0] - en_EN, English. (include AU, GB...)                     [6] - de_DE, Deutsch.", 'green'))
        print(colored("[1] - fr_FR, Français.                                        [7] - es_ES, Español.", 'green'))
        print(colored("[2] - ja_JP, 日本語.                                          [8] - it_IT, Italiano.", 'green'))
        print(colored("[3] - ru_RU, Русский.                                         [9] - hu_HU, Magyar.", 'green'))
        print(colored("[4] - pt_BR, Português.                                       [10] - cs_CZ, Čeština.", 'green'))
        print(colored("[5] - pl_PL, Polski.", 'green'))
        print(colored("[+] - For other language, please visit https://github.com/reusteur73/LoL-queue-Acceptor-windows/tree/master/lib", 'red'))
        pref = int(input('Chosen Language='))
        conf.write('game-language=' + lang[pref])
        conf.close()
        print('\n'*2)
        print(colored("Preference saved. Thanks you for using this script", 'green'))
        sleep(3)
    # /* Else continue *\
    else:
        print('\n'*5)
        print(colored("Language already chosen, to change language again press Ctrl+C while waiting for match.", 'green'))
        sleep(3)
        pass

    # /* Loading choosen language. *\
    load = open("config.txt", "r")
    load_lang = load.read()
    if load_lang != "":
        pass
    else:
        change_lang()
            
    lng = load_lang.split("=",1)[1]
    pos = lang.index(lng)
    process=['EN', 'FR', 'JP', 'RU', 'BR', 'PL', 'DE', 'ES', 'IT', 'HU', 'CZ']
    load.close()
        # /* Preparing Match accept button in all differents languages. *\
    imgs = ['en_EN', 'fr_FR', 'cs_CZ', 'de_DE', 'es_ES', 'it_IT', 'hu_HU', 'pl_PL', 'pt_BR', 'ru_RU', 'ja_JP']
    for img in tqdm(imgs, unit ="file", desc ="Preparing Files"):
        n_url = f"https://www.reusteur.org/hRDz3fWn/{img}.png"
            
            # print(colored('Preparing language {img} ', 'yellow'))
        if os.path.isfile(f'{img}.png') == False:
            img_data = requests.get(n_url, verify=False).content
            sleep(0.3)
            with open(f'{img}.png', 'wb') as handler:
                sleep(0.3)
                handler.write(img_data)
                sleep(0.3)
    else:
        pass
            
        # Il faut ajouter les langues : ko_KR, zh_CN, zh_TW, el_GR

        # /* Stats*\
        statistques = "https://www.reusteur.org/hRDz3fWn/index.php"
        statistques = requests.get(statistques, verify=False).content
        global choice
        choice = process[pos]
        return choice

# /* Change language after first run *\
def change_lang():
    print('\n'*60)
    if os.path.isfile('config.txt') == True:
        conf = open('config.txt', 'w')
        print(colored("Enter the number needed", 'blue'))
        print(colored("[0] - en_EN, English. (include AU, GB...)                     [6] - de_DE, Deutsch.", 'green'))
        print(colored("[1] - fr_FR, Français.                                        [7] - es_ES, Español.", 'green'))
        print(colored("[2] - ja_JP, 日本語.                                          [8] - it_IT, Italiano.", 'green'))
        print(colored("[3] - ru_RU, Русский.                                         [9] - hu_HU, Magyar.", 'green'))
        print(colored("[4] - pt_BR, Português.                                       [10] - cs_CZ, Čeština.", 'green'))
        print(colored("[5] - pl_PL, Polski.", 'green')) 
        print(colored("[+] - For other language, please visit https://github.com/reusteur73/LoL-queue-Acceptor-windows/tree/master/lib", 'red'))

        pref = int(input('Chosen Language='))
        conf.write('game-language=' + lang[pref])
        conf.close()
        print('\n'*60)
        print(colored("Language successfully changed!", 'green'))
        print(colored("Program will restart in 3 seconds", 'green'))
        print('\n'*6)
        sleep(3)
        pass

# /* Define click *\
def click(x, y):
    pyautogui.click(x, y)

# /* All language accept function *\
def EN():
    buttonEn = pyautogui.locateOnScreen('en_EN.png', confidence=0.7)
    if buttonEn != None:
        click(buttonEn.left, buttonEn.top)
        return True
def FR():
    buttonFr = pyautogui.locateOnScreen('fr_FR.png', confidence=0.7)
    if buttonFr != None:
        click(buttonFr.left, buttonFr.top)
        return True
def PT():
    buttonPt = pyautogui.locateOnScreen('pt_BR.png', confidence=0.7)
    if buttonPt != None:
        click(buttonPt.left, buttonPt.top)
        return True
def CZ():
    buttonCz = pyautogui.locateOnScreen('cs_CZ.png', confidence=0.7)
    if buttonCz != None:
        click(buttonCz.left, buttonCz.top)
        return True
def DE():
    buttonDe = pyautogui.locateOnScreen('de_DE.png', confidence=0.7)
    if buttonDe != None:
        click(buttonDe.left, buttonDe.top)
        return True
def ES():
    buttonEs = pyautogui.locateOnScreen('es_ES.png', confidence=0.7)
    if buttonEs != None:
        click(buttonEs.left, buttonEs.top)
        return True
def IT():
    buttonIt = pyautogui.locateOnScreen('it_IT.png', confidence=0.7)
    if buttonIt != None:
        click(buttonIt.left, buttonIt.top)
        return True
def HU():
    buttonHu = pyautogui.locateOnScreen('hu_HU.png', confidence=0.7)
    if buttonHu != None:
        click(buttonHu.left, buttonHu.top)
        return True
def PL():
    buttonPl = pyautogui.locateOnScreen('pl_PL.png', confidence=0.7)
    if buttonPl != None:
        click(buttonPl.left, buttonPl.top)
        return True
def RU():
    buttonRu = pyautogui.locateOnScreen('ru_RU.png', confidence=0.7)
    if buttonRu != None:
        click(buttonRu.left, buttonRu.top)
        return True
def JA():
    buttonJa = pyautogui.locateOnScreen('ja_JP.png', confidence=0.7)
    if buttonJa != None:
        click(buttonJa.left, buttonJa.top)
        return True

# /* Event *\
initialisation()
choice_finals = locals()[choice] # /* Important *\
while True:
    try: # /* Waiting Output *\
        print('\n'*60)
        print(colored('                  Waiting for match [■□□□□□□□□□]                  Press Ctrl+C to pause', 'yellow'))
        print('\n'*6)
        sleep(0.2)
        print('\n'*60)
        print(colored('                  Waiting for match [■■□□□□□□□□]                  Press Ctrl+C to pause', 'yellow'))
        print('\n'*6)
        sleep(0.2)
        print('\n'*60)
        print(colored('                  Waiting for match [■■■□□□□□□□]                  Press Ctrl+C to pause', 'yellow'))
        print('\n'*6)
        sleep(0.2)
        print('\n'*60)
        print(colored('                  Waiting for match [■■■■□□□□□□]                  Press Ctrl+C to pause', 'yellow'))
        print('\n'*6)
        sleep(0.2)
        print('\n'*60)
        print(colored('                  Waiting for match [■■■■■□□□□□]                  Press Ctrl+C to pause', 'yellow'))
        print('\n'*6)
        sleep(0.2)
        print('\n'*60)
        print(colored('                  Waiting for match [■■■■■■□□□□]                  Press Ctrl+C to pause', 'yellow'))
        print('\n'*6)
        sleep(0.2)
        print('\n'*60)
        print(colored('                  Waiting for match [■■■■■■■□□□]                  Press Ctrl+C to pause', 'yellow'))
        print('\n'*6)
        sleep(0.2)
        print('\n'*60)
        print(colored('                  Waiting for match [■■■■■■■■□□]                  Press Ctrl+C to pause', 'yellow'))
        print('\n'*6)
        sleep(0.2)
        print('\n'*60)
        print(colored('                  Waiting for match [■■■■■■■■■□]                  Press Ctrl+C to pause', 'yellow'))
        print('\n'*6)
        sleep(0.2)
        print('\n'*60)
        print(colored('                  Waiting for match [■■■■■■■■■■]                  Press Ctrl+C to pause', 'yellow'))
        print('\n'*6)

        # /* If there is a match:*\
        # sleep(3)
        if choice_finals():
            print('\n'*60)
            print(colored('                  Match accepted! :', 'green'))
            print('\n'*6)
            sleep(1)
            print('\n'*60)
            print(colored('                  Match accepted! :)', 'green'))
            print('\n'*6)
            sleep(1)
            print('\n'*60)
            print(colored('                  Match accepted! ☺', 'green'))
            print('\n'*6)
            sleep(1)

    # /* While pausing *\
    except KeyboardInterrupt:
        print('\n'*60)
        print(colored('\nPaused...  (Hit ENTER to continue, press Ctrl+C to exit.)', 'red'))
        print('\n'*3)
        print(colored('Type "lang" to change game language setting:', 'blue')) 
        x = input()
        try:
            if x == 'lang':
                change_lang()
                pass
        except KeyboardInterrupt:
            print(colored('Resuming...', 'green'))
            continue

