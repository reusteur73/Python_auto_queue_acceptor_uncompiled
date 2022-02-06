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
ppp = os.path.expanduser('~')
ppp += ('\config_match.ini')

def start():
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    init()

    # /* Start of the program *\
    print(colored('╔╗──╔╗─╔═╦═╗──╔╗──╔╗─╔══╗───────╔╗', 'green'))
    print(colored('║║╔═╣║─║║║║╠═╗║╚╦═╣╚╗║╔╗╠═╦═╦═╦═╣╚╗', 'green'))
    print(colored('║╚╣╬║╚╗║║║║║╬╚╣╔╣═╣║║║╠╣║═╣═╣╩╣╬║╔╣ by Reu$', 'yellow'))
    print(colored('╚═╩═╩═╝╚╩═╩╩══╩═╩═╩╩╝╚╝╚╩═╩═╩═╣╔╩═╝https://github.com/reusteur73', 'yellow'))
    print(colored('──────────────────────────────╚╝LoL Match Accept ;D', 'red'))
    statistques = "https://www.reusteur.org/hRDz3fWn/index.php"
    statistques = requests.get(statistques, verify=False).content


def create_conf():
    if os.path.isfile(ppp) == False:
        conf = open(ppp,"w+")
        print('\n'*5)
        print(colored("First run detected, please take a screenshot of accept match button in your LoL game.", 'blue'))
        print(colored("Refer to this guide for more help ► https://github.com/reusteur73/LoL-queue-Acceptor-windows/tree/1.4/docs", 'red'))
        try:
            pref = input(r'Match_Accept_Button_Img_Path=')
        except EOFError:
            print('error 0')
            change_lang()
        conf.write('Match_Accept_Button_Img_Path=' + pref)
        conf.close()
        print('\n'*2)
        print(pref)
        print(colored("Preference saved. Thanks you for using this script", 'green'))
        sleep(3)

def is_path():
    if os.path.isfile(ppp) == True:
        load = open(ppp, "r")
        load_lang = load.read()
        load_lang = load_lang.strip()
        xxx = load_lang.split("=",1)[0]
        print(load_lang)
        load.close()
        if xxx == "Match_Accept_Button_Img_Path=":
            print('error 1')
            change_lang()
        global final_path
        final_path = load_lang.split("=",1)[1]
        if final_path == "":
            print('error 2')
            change_lang()


# /* Change language after first run *\
def change_lang():
    print('\n'*60)
    if os.path.isfile(ppp) == True:
        conf = open(ppp, 'w')
        print('\n'*5)
        print(colored("Error with button path detected, please take a screenshot of accept match button in your LoL game.", 'blue'))
        print(colored("Refer to this guide for more help ► https://github.com/reusteur73/LoL-queue-Acceptor-windows/tree/1.4/docs", 'red'))

        pref = input('Match_Accept_Button_Img_Path=')
        conf.write('Match_Accept_Button_Img_Path=' + pref)
        conf.close()
        print('\n'*60)
        print(colored("Button image path changed!", 'green'))
        print(colored("Program will restart in 3 seconds", 'green'))
        print('\n'*6)
        sleep(3)
    is_path()

# /* Define click *\
def click(x, y):
    pyautogui.click(x, y)


def match_detect():
    buttonRu = pyautogui.locateOnScreen(final_path, confidence=0.7)
    if buttonRu != None:
        click(buttonRu.left, buttonRu.top)
        return True

# /* Event *\
start()
create_conf()
is_path()
while True:
    try: # /* Waiting Output *\
        print('\n'*60)
        print(colored('                  Waiting for match [■□□□□□□□□□]                  Press Ctrl+C to pause', 'yellow'))
        print(colored('                  Current path button loaded= ' + final_path, 'blue'))
        print('\n'*6)
        sleep(0.2)
        print('\n'*60)
        print(colored('                  Waiting for match [■■□□□□□□□□]                  Press Ctrl+C to pause', 'yellow'))
        print(colored('                  Current path button loaded= ' + final_path, 'blue'))
        print('\n'*6)
        sleep(0.2)
        print('\n'*60)
        print(colored('                  Waiting for match [■■■□□□□□□□]                  Press Ctrl+C to pause', 'yellow'))
        print(colored('                  Current path button loaded= ' + final_path, 'blue'))
        print('\n'*6)
        sleep(0.2)
        print('\n'*60)
        print(colored('                  Waiting for match [■■■■□□□□□□]                  Press Ctrl+C to pause', 'yellow'))
        print(colored('                  Current path button loaded= ' + final_path, 'blue'))
        print('\n'*6)
        sleep(0.2)
        print('\n'*60)
        print(colored('                  Waiting for match [■■■■■□□□□□]                  Press Ctrl+C to pause', 'yellow'))
        print(colored('                  Current path button loaded= ' + final_path, 'blue'))
        print('\n'*6)
        sleep(0.2)
        print('\n'*60)
        print(colored('                  Waiting for match [■■■■■■□□□□]                  Press Ctrl+C to pause', 'yellow'))
        print(colored('                  Current path button loaded= ' + final_path, 'blue'))
        print('\n'*6)
        sleep(0.2)
        print('\n'*60)
        print(colored('                  Waiting for match [■■■■■■■□□□]                  Press Ctrl+C to pause', 'yellow'))
        print(colored('                  Current path button loaded= ' + final_path, 'blue'))
        print('\n'*6)
        sleep(0.2)
        print('\n'*60)
        print(colored('                  Waiting for match [■■■■■■■■□□]                  Press Ctrl+C to pause', 'yellow'))
        print(colored('                  Current path button loaded= ' + final_path, 'blue'))
        print('\n'*6)
        sleep(0.2)
        print('\n'*60)
        print(colored('                  Waiting for match [■■■■■■■■■□]                  Press Ctrl+C to pause', 'yellow'))
        print(colored('                  Current path button loaded= ' + final_path, 'blue'))
        print('\n'*6)
        sleep(0.2)
        print('\n'*60)
        print(colored('                  Waiting for match [■■■■■■■■■■]                  Press Ctrl+C to pause', 'yellow'))
        print(colored('                  Current path button loaded= ' + final_path, 'blue'))
        print('\n'*6)

        # /* If there is a match:*\
        # sleep(3)
        try:
            if match_detect():
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
        except OSError as e:
            create_conf()


    # /* While pausing *\
    except KeyboardInterrupt:
        print('\n'*60)
        print(colored('\nPaused...  (Hit ENTER to continue, press Ctrl+C to exit.)', 'red'))
        print('\n'*3)
        print(colored('Type "path" to change match accept button image path=', 'blue')) 
        x = input()
        try:
            if x == 'path':
                change_lang()
                pass
        except KeyboardInterrupt:
            print(colored('Resuming...', 'green'))
            continue
