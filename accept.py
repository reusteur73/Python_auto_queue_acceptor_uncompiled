from tarfile import GNUTYPE_LONGLINK
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
import telebot
from discord_webhook import DiscordWebhook

ppp = os.path.expanduser('~')
ppp += ('\config_match.ini')
global notifier
def start():
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    init()

    # /* Start of the program *\
    print(colored('                  ╔╗──╔╗─╔═╦═╗──╔╗──╔╗─╔══╗───────╔╗', 'green'))
    print(colored('                  ║║╔═╣║─║║║║╠═╗║╚╦═╣╚╗║╔╗╠═╦═╦═╦═╣╚╗ by Reu$', 'green'))
    print(colored('                  ║╚╣╬║╚╗║║║║║╬╚╣╔╣═╣║║║╠╣║═╣═╣╩╣╬║╔╣https://github.com/reusteur73', 'yellow'))
    print(colored('                  ╚═╩═╩═╝╚╩═╩╩══╩═╩═╩╩╝╚╝╚╩═╩═╩═╣╔╩═╝LoL Match Accept ;D', 'yellow'))
    print(colored('                  ──────────────────────────────╚╝ V1.5.1', 'red'))
    statistques = "https://www.reusteur.org/hRDz3fWn/index.php"
    try:
        statistques = requests.get(statistques, verify=False, timeout=10).content
    except (requests.exceptions.ConnectTimeout, requests.exceptions.ProxyError) as EE:
        pass
    sleep(1)

def create_conf():
    if os.path.isfile(ppp) == False:
        conf = open(ppp,"w+")
        print('\n'*5)
        print(colored("                  First run detected, please take a screenshot of accept match button in your LoL game.", 'blue'))
        print(colored("                  Refer to this guide for more help ► https://github.com/reusteur73/LoL-queue-Acceptor-windows/tree/1.4/docs", 'red'))
        try:
            pref = input(r'Match_Accept_Button_Img_Path=')
        except EOFError:
            change_lang()
        conf.write('Match_Accept_Button_Img_Path=' + pref + "\n")
        conf.close()
        print('\n'*60)
        print(colored("                  Would you like to be notified on Discord or Telegram when a match is accepted?", 'green'))
        print()
        print(colored('                  [1] - To set Discord Accepted Match Notifier.', 'blue'))
        print(colored('                  [2] - To set Telegram Accepted Match Notifier.', 'blue'))
        print(colored('                  [3] - No Notifier.', 'blue'))
        print()
        choix = input("Choice(must be number) =")
        if isinstance(int(choix), int) == False:
            print('\n'*60)
            print(colored("                  Please choose a number!", 'green'))
            print('\n'*3)
            sleep(2)
            create_conf()
        if choix == "1" :
            discord()
        if choix == "2":
            telegram()
        if choix == "3":
            global notifier
            notifier = "none"
            pass
        print(colored("                  Preference saved. Thanks you for using this script", 'green'))
        sleep(3)

def telegram():
    print('\n'*60)
    print(colored("                  To set Telegram Notifier, we just need two informations: your user_ID and token api_key", 'green'))
    print(colored("                  Please refer to this guide to get your user_id ► https://www.alphr.com/telegram-find-user-id/", 'green'))
    print(colored(r"                  And this guide to get your token api_key ► https://stackoverflow.com/questions/43291868/where-to-find-the-telegram-api-key#:~:text=Log%20in%20to%20your%20Telegram,one%20api_id%20connected%20to%20it", 'green'))
    print('\n'*3)
    global tele_token, tele_user_id, notifier
    tele_token = input("Enter Telegram Token =")
    tele_user_id = input("Now enter your user_id =") 
    if os.path.isfile(ppp) == True:
        conf = open(ppp, 'r')
        kdhjg = conf.readlines()
        conf.close()
        btn = kdhjg[0]
        if kdhjg[1] != None:
            conf = open(ppp, 'w')
            conf.write(btn)
            conf.close()
        conf = open(ppp, 'a')
        conf.write('Telegram_Token=' + tele_token + "\n")
        conf.write('Telegram_User_Id=' + tele_user_id + "\n")
        conf.write('Notifier_Method=Telegram' + "\n")
        conf.close()
    print(colored("                  Telegram Bot setup sucessfully! A test message will be send.", 'green'))
    print('\n'*3)
    # Create bot
    bot = telebot.TeleBot(token=tele_token)
    bot.send_message(tele_user_id, 'This is a test message ! ☺')
    sleep(2)
    notifier_method()

def discord():
    print('\n'*60)             
    print(colored("                  To set Discord Notifier, we just need one information: your channel discord webhook:", 'green'))
    print(colored("                  Please refer to this really simple guide to create an url ► https://help.dashe.io/en/articles/2521940-how-to-create-a-discord-webhook-url", 'green'))
    print('\n'*3)
    global disc_webhook, notifier
    disc_webhook = input("Enter Discord Webhook URL =")
    if os.path.isfile(ppp) == True:
        conf = open(ppp, 'r')
        kdhjg = conf.readlines()
        conf.close()
        btn = kdhjg[0]
        if index_in_list(kdhjg, 1) == True:
            conf = open(ppp, 'w')
            conf.write(btn)
            conf.close()

        conf = open(ppp, 'a')
        conf.write('Discord_Webhook_Url=' + disc_webhook + "\n")
        conf.write('Notifier_Method=Discord' + "\n")
        conf.close()
    notifier = "discord"
    print(colored("                  Discord Notifier setup sucessfully! A test message will be send.", 'green'))
    print('\n'*3)
    # Create bot
    webhook = DiscordWebhook(url=disc_webhook, content='This is a test message ☺')
    webhook.execute()
    sleep(2)
    notifier_method()

def index_in_list(a_list, index):
    return (index < len(a_list))

def is_path():
    global tele_token, tele_user_id, notifier, disc_webhook
    if os.path.isfile(ppp) == True:
        load = open(ppp, "r")
        load_lang = load.readlines()
        load.close()
        if load_lang != []:
            ligne1 = load_lang[0]
            img_path = ligne1.split("=",1)[1]
            if img_path == "Match_Accept_Button_Img_Path=":
                change_lang()
            global final_path
            final_path = img_path
            if final_path == "":
                change_lang()
        else:
            change_lang()
        if index_in_list(load_lang, 1) == True:
            ligne2= load_lang[1]
            if ligne2 == "Notifier_Disabled\n":
                pass
            if ligne2 != "Notifier_Disabled\n":
                set_option1 = ligne2.split("=",1)[0]
                option1 = ligne2.split("=",1)[1]
            else:
                set_option1 = "Notifier_Disabled"
    
            if set_option1 == "Telegram_Token":
                ligne3 = load_lang[2]
                option2 = ligne3.split("=",1)[1]
                notifier = "tele"
                tele_token = option1
                tele_user_id = option2
        else:
            pass
        if index_in_list(load_lang, 1) == True:
            if set_option1 == "Discord_Webhook_Url":
                notifier = "discord"
                disc_webhook = option1

def notifier_method():
    if os.path.isfile(ppp) == True:
        conf = open(ppp, 'r')
        lignes = conf.readlines()
        conf.close()
        last = lignes[-1]
        global notif
        if last == "Notifier_Disabled\n":
            notif = "None"
        else:
            notif = last.split("=",1)[1]
        if notif == "Discord":
            pass
        if notif == "Telegram":
            pass
        if notif == "":
            notif = "None"
        notif = notif.strip()

def change_notifier():
    if os.path.isfile(ppp) == True:
        conf = open(ppp, 'r')
        lignes = conf.readlines()
        conf.close()
        ligne1 = lignes[0]
        if int(x) == 2:
            discord()
        if int(x) == 3:
            telegram()

def disable_notifier():
    if os.path.isfile(ppp) == True:
        conf = open(ppp, 'r')
        lignes = conf.readlines()
        conf.close()
        btn = lignes[0]
        conf = open(ppp, 'w')
        conf.write(btn)
        conf.write("Notifier_Disabled" + "\n")
        conf.close()
        print('\n'*60)
        print(colored("                         Notifier disabled sucessfully!", 'blue'))
        print('\n'*3)
        sleep(3)
        notifier_method()

# /* Change language after first run *\
def change_lang():
    print('\n'*60)
    if os.path.isfile(ppp) == True:
        conf = open(ppp, 'r')
        lignes = conf.readlines()
        conf.close()
        print('\n'*5)
        print(colored("                  Error with button path detected, please take a screenshot of accept match button in your LoL game.", 'blue'))
        print(colored("                  Refer to this guide for more help ► https://github.com/reusteur73/LoL-queue-Acceptor-windows/tree/1.4/docs", 'red'))
        pref = input('Match_Accept_Button_Img_Path=')
        conf = open(ppp, 'w')
        conf.write('Match_Accept_Button_Img_Path=' + pref + "\n")
        if index_in_list(lignes, 1) == True:
            ligne2 = lignes[1]
            if ligne2 != None:
                conf.write(ligne2)
            if ligne2 != "":
                conf.write(ligne2)
        if index_in_list(lignes, 2) == True:
            ligne3 = lignes[2]
            if ligne3 != None:
                conf.write(ligne3)
            if ligne3 != "":
                conf.write(ligne3)
        conf.close()
        notifier_method()
        print('\n'*60)
        print(colored("                  Button image path changed!", 'green'))
        print(colored("                  Program will restart in 3 seconds", 'green'))
        print('\n'*6)
        sleep(3)
    is_path()

# /* Define click *\
def click(x, y):
    pyautogui.click(x, y)

def match_detect():
    buttonRu = pyautogui.locateOnScreen(final_path.strip(), confidence=0.7)
    if buttonRu != None:
        click(buttonRu.left, buttonRu.top)
        if notif == "Telegram":
            bot = telebot.TeleBot(token=tele_token.strip())
            bot.send_message(tele_user_id.strip(), 'A match has been accepted! ☺')
        else:
            pass
        if notif == "Discord":
            webhook = DiscordWebhook(url=disc_webhook.strip(), content='@everyone A match has been accepted! ☺')
            webhook.execute()
        else:
            pass
        return True

# /* Event *\
start()
create_conf()
is_path()
notifier_method()

while True:
    try: # /* Waiting Output *\
        print('\n'*60)
        print(colored('                  Waiting for match [■□□□□□□□□□]                  Press Ctrl+C to pause and get settings.', 'yellow'))
        print(colored('                  Current path button loaded = ' + final_path + "                  Notification Method = " + notif, 'blue'))
        print('\n'*6)
        sleep(0.2)
        print('\n'*60)
        print(colored('                  Waiting for match [■■□□□□□□□□]                  Press Ctrl+C to pause and get settings.', 'yellow'))
        print(colored('                  Current path button loaded = ' + final_path + "                  Notification Method = " + notif, 'blue'))
        print('\n'*6)
        sleep(0.2)
        print('\n'*60)
        print(colored('                  Waiting for match [■■■□□□□□□□]                  Press Ctrl+C to pause and get settings.', 'yellow'))
        print(colored('                  Current path button loaded = ' + final_path + "                  Notification Method = " + notif, 'blue'))
        print('\n'*6)
        sleep(0.2)
        print('\n'*60)
        print(colored('                  Waiting for match [■■■■□□□□□□]                  Press Ctrl+C to pause and get settings.', 'yellow'))
        print(colored('                  Current path button loaded = ' + final_path + "                  Notification Method = " + notif, 'blue'))
        print('\n'*6)
        sleep(0.2)
        print('\n'*60)
        print(colored('                  Waiting for match [■■■■■□□□□□]                  Press Ctrl+C to pause and get settings.', 'yellow'))
        print(colored('                  Current path button loaded = ' + final_path + "                  Notification Method = " + notif, 'blue'))
        print('\n'*6)
        sleep(0.2)
        print('\n'*60)
        print(colored('                  Waiting for match [■■■■■■□□□□]                  Press Ctrl+C to pause and get settings.', 'yellow'))
        print(colored('                  Current path button loaded = ' + final_path + "                  Notification Method = " + notif, 'blue'))
        print('\n'*6)
        sleep(0.2)
        print('\n'*60)
        print(colored('                  Waiting for match [■■■■■■■□□□]                  Press Ctrl+C to pause and get settings.', 'yellow'))
        print(colored('                  Current path button loaded = ' + final_path + "                  Notification Method = " + notif, 'blue'))
        print('\n'*6)
        sleep(0.2)
        print('\n'*60)
        print(colored('                  Waiting for match [■■■■■■■■□□]                  Press Ctrl+C to pause and get settings.', 'yellow'))
        print(colored('                  Current path button loaded = ' + final_path + "                  Notification Method = " + notif, 'blue'))
        print('\n'*6)
        sleep(0.2)
        print('\n'*60)
        print(colored('                  Waiting for match [■■■■■■■■■□]                  Press Ctrl+C to pause and get settings.', 'yellow'))
        print(colored('                  Current path button loaded = ' + final_path + "                  Notification Method = " + notif, 'blue'))
        print('\n'*6)
        sleep(0.2)
        print('\n'*60)
        print(colored('                  Waiting for match [■■■■■■■■■■]                  Press Ctrl+C to pause and get settings.', 'yellow'))
        print(colored('                  Current path button loaded = ' + final_path + "                  Notification Method = " + notif, 'blue'))
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
        print(colored('\n                  Paused...  (Hit ENTER to continue, press Ctrl+C to exit.)', 'red'))
        print()
        print(colored('                  [1] - To change accept match button path', 'blue')) 
        print(colored('                  [2] - To set Discord Accepted Match Notifier', 'blue'))
        print(colored('                  [3] - To set Telegram Accepted Match Notifier', 'blue'))
        print(colored('                  [4] - To Disable Match Accept Notifier', 'blue'))
        print('\n'*3)
        x = input("Choice (must be number) =")
        if isinstance(int(x), int):
            try:
                if int(x) == 1:
                    change_lang()
                    pass
                if int(x) == 2:
                    change_notifier()
                    pass
                if int(x) == 3:
                    change_notifier()
                    pass
                if int(x) == 4:
                    print('\n'*60)
                    print(colored('                 Are you sure you want to turn off notifications?', 'blue'))
                    print(colored('                 (Y)es or (N)o', 'blue'))

                    z = input('Choice(Y or N) =')
                    if str(z) == "Y":
                        disable_notifier()
                    else:
                        print('\n'*60)
                        print(colored('                Operation cancelled1', 'blue'))
                        print('\n'*3)
                        sleep(2.5)
            except KeyboardInterrupt:
                print(colored('                  Resuming...', 'green'))
                continue
        else:
            print('\n'*60)
            print(colored('                 Please enter a number in the list', 'red'))
            print('\n'*3)
            sleep(3)
