import os, pyautogui, configparser, telebot, requests, urllib3
from time import sleep
from discord_webhook import DiscordWebhook
from colorama import init
from termcolor import colored
from tqdm import tqdm
try:
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    init()
    def first_run():
        
        if not os.path.isfile('config.ini'):
            print('\n'*60)
            print(colored('                  ╔╗──╔╗─╔═╦═╗──╔╗──╔╗─╔══╗───────╔╗', 'green'))
            print(colored('                  ║║╔═╣║─║║║║╠═╗║╚╦═╣╚╗║╔╗╠═╦═╦═╦═╣╚╗ by Reu$', 'green'))
            print(colored('                  ║╚╣╬║╚╗║║║║║╬╚╣╔╣═╣║║║╠╣║═╣═╣╩╣╬║╔╣https://github.com/reusteur73', 'yellow'))
            print(colored('                  ╚═╩═╩═╝╚╩═╩╩══╩═╩═╩╩╝╚╝╚╩═╩═╩═╣╔╩═╝LoL Match Accept ;D', 'yellow'))
            print(colored('                  ──────────────────────────────╚╝ V1.6.0', 'red'))
            print('\n'*6)
            sleep(2)
            try:
                requests.get('https://www.reusteur.org/hRDz3fWn/index.php', verify=False, timeout=10).content
            except (requests.exceptions.ConnectTimeout, requests.exceptions.ProxyError) as EE:
                pass
            print('\n'*60)
            print(colored('\n                                     First run detected, please setup config file, its really quick.', 'green'))
            print(colored('\n                                     Please enter the path of the screenshot : ', 'green'))
            print(colored('\n                                     If you need help, you got a complete guide here ► https://github.com/reusteur73/Python-queue-Acceptor-LoL-compiled/blob/1.5.2/docs/readme.md', 'green'))
            print(colored('\n                                     Example : C:\\Users\\User\\Desktop\\screenshot.png', 'green'))
            print('\n'*6)
            screenshot_path = input('\nScreenshot path : ')
            print('\n'*60)
            print(colored('\n                                     Please enter the notification method : discord_webhook, telegram_message, or none', 'green'))
            print('\n'*6)
            notification_method = input('\nNotification method : ')
            if notification_method == 'discord_webhook':
                print('\n'*60)
                print(colored('\n                                     Please enter the discord webhook url : ', 'green'))
                print('\n'*6)
                discord_webhook_url = input('\nDiscord webhook url : ')
            if notification_method == 'telegram_message':
                print('\n'*60)
                print(colored('\n                                     Please enter the telegram bot token : ', 'green'))
                print('\n'*6)
                telegram_bot_token = input('\nTelegram bot token : ')
                print('\n'*60)
                print(colored('\n                                     Please enter the telegram chat id : ', 'green'))
                print('\n'*6)
                telegram_chat_id = input('\nTelegram chat id : ')
            if notification_method == 'none':
                notification_method = 'none'
            config = configparser.ConfigParser()
            config['DEFAULT'] = {'screenshot_path': screenshot_path, 'notification_method': notification_method}
            if notification_method == 'discord_webhook':
                config['discord_webhook'] = {'discord_webhook_url': discord_webhook_url}
            if notification_method == 'telegram_message':
                config['telegram_message'] = {'telegram_bot_token': telegram_bot_token, 'telegram_chat_id': telegram_chat_id}
            with open('config.ini', 'w') as configfile:
                config.write(configfile)
            print('\n'*60)
            print(colored('\n                                     Config file set', 'blue'))
            print('\n'*6)
        else:
            print('\n'*60)
            print(colored('                  ╔╗──╔╗─╔═╦═╗──╔╗──╔╗─╔══╗───────╔╗', 'green'))
            print(colored('                  ║║╔═╣║─║║║║╠═╗║╚╦═╣╚╗║╔╗╠═╦═╦═╦═╣╚╗ by Reu$', 'green'))
            print(colored('                  ║╚╣╬║╚╗║║║║║╬╚╣╔╣═╣║║║╠╣║═╣═╣╩╣╬║╔╣https://github.com/reusteur73', 'yellow'))
            print(colored('                  ╚═╩═╩═╝╚╩═╩╩══╩═╩═╩╩╝╚╝╚╩═╩═╩═╣╔╩═╝LoL Match Accept ;D', 'yellow'))
            print(colored('                  ──────────────────────────────╚╝ V1.6.0', 'red'))
            print('\n'*6)
            sleep(2)
            try:
                requests.get('https://www.reusteur.org/hRDz3fWn/index.php', verify=False, timeout=10).content
            except (requests.exceptions.ConnectTimeout, requests.exceptions.ProxyError) as EE:
                pass
            print('\n'*60)
            print(colored('\n                                     Config file already setup.', 'green'))
            print('\n'*6)
            sleep(1)

    def load_config():
        config = configparser.ConfigParser()
        config.read('config.ini')
        return config

    def get_notification_method():
        config = load_config()
        return config['DEFAULT']['notification_method']

    def get_screenshot_path():
        config = load_config()
        return config['DEFAULT']['screenshot_path']

    def get_discord_webhook_url():
        config = load_config()
        return config['discord_webhook']['discord_webhook_url']

    def get_telegram_bot_token():
        config = load_config()
        return config['telegram_message']['telegram_bot_token']

    def get_telegram_chat_id():
        config = load_config()
        return config['telegram_message']['telegram_chat_id']

    def accept_match():
        try:
            screenshot_path = get_screenshot_path()
            screenshot = pyautogui.locateOnScreen(screenshot_path, confidence=0.7)
            if screenshot is not None:
                print(colored('\n                                     Match detected', 'green'))
                pyautogui.click(screenshot)
                print(colored('\n                                     Match accepted', 'green'))
                if get_notification_method() == 'discord_webhook':
                    webhook = DiscordWebhook(url=get_discord_webhook_url(), content='Match accepted')
                    webhook.execute()
                if get_notification_method() == 'telegram_message':
                    telegram_bot_token = get_telegram_bot_token()
                    telegram_chat_id = get_telegram_chat_id()
                    telegram_bot = telebot.TeleBot(token=telegram_bot_token.strip())
                    telegram_bot.send_message(telegram_chat_id, 'Match accepted')
                if get_notification_method() == 'none':
                    pass
            else:
                print('\n'*60)
                print(colored('\n                                     No match detected.', 'red'))
                print('\n'*6)
                pass
        except OSError:
            print('\n'*60)
            print(colored('\n                                     /!\ File missing, or path incorect ! You need change in config.ini file, the screenshot path /!\ ', 'red'))
            print(colored('                                                          Sleeping for infinity...', 'red'))
            print('\n'*6)
            sleep(1000)
    first_run()
    while True:
        try:
            accept_match()
            sleep(1.5)
            print('\n'*60)
            print(colored('                                              Waiting match...', 'green'))
            print(colored('                                     Press CTRL + C to pause research', 'green'))
            print(colored('                                     Current notification method = ' + get_notification_method() +'', 'green'))
            print('\n'*6)
            for i in tqdm(range(3), unit='s',colour="blue"):
                sleep(1)
        except KeyboardInterrupt:
            print('\n'*60)
            print(colored('\n                                                         /!\ Script stopped /!\ ', 'red'))
            print(colored('\n                                     If you want to change notification methode enter number [1]', 'green'))
            print(colored('\n                                     To change screenshot path enter number [2]', 'green'))
            print(colored('\n                                     To resume match research just press ENTER', 'green'))
            print(colored('\n                                     If you want to quit script press CTRL+C', 'green'))
            print('\n'*6)
            choice = input('\nChoice : ')
            if choice == '1':
                print(colored('\n                                     Please enter the notification method : discord_webhook, telegram_message, or none', 'green'))
                notification_method = input('\nNotification method : ')
                config = load_config()
                config['DEFAULT']['notification_method'] = notification_method
                if notification_method == 'discord_webhook':
                    print(colored('\n                                     Please enter the discord webhook url', 'green'))
                    discord_webhook_url = input('\nDiscord webhook url : ')
                    config['discord_webhook'] = {'discord_webhook_url': discord_webhook_url}
                    config['discord_webhook']['discord_webhook_url'] = discord_webhook_url
                if notification_method == 'telegram_message':
                    print(colored('\n                                     Please enter the telegram bot token', 'green'))
                    telegram_bot_token = input('\nTelegram bot token : ')
                    print(colored('\n                                     Please enter the telegram chat id', 'green'))
                    telegram_chat_id = input('\nTelegram chat id : ')
                    config['telegram_message'] = {'telegram_bot_token': telegram_bot_token, 'telegram_chat_id': telegram_chat_id}
                    config['telegram_message']['telegram_bot_token'] = telegram_bot_token
                    config['telegram_message']['telegram_chat_id'] = telegram_chat_id
                if notification_method == 'none':
                    notification_method = 'none'
                config['DEFAULT']['notification_method'] = notification_method
                with open('config.ini', 'w') as configfile:
                    config.write(configfile)
                print(colored('\n                                     Config file changed', 'green'))
            if choice == '2':
                print(colored('\n                                     Please enter the screenshot path', 'green'))
                screenshot_path = input('\nScreenshot path : ')
                config = load_config()
                config['DEFAULT']['screenshot_path'] = screenshot_path
                with open('config.ini', 'w') as configfile:
                    config.write(configfile)
                print(colored('\n                                     Config file changed !', 'green'))
            if choice == '':
                print('\n'*60)
                print(colored('\n                                     Resuming match research', 'green'))
                print('\n'*6)
                sleep(2)
                pass
except Exception as e:
    print(colored('\n                                     /!\ Error in config file /!\ ', 'red'))
    print(colored('                                                          Try reinstall script from Github', 'red'))
    print(colored('                                                          Sleeping for infinity...' 'red'))
    print(colored('                                                          Error : ' + str(e), 'red'))
    print('\n'*6)
    sleep(1000)
