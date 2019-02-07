#!/usr/bin/env python3

import configparser
import subprocess
import sys
from urllib.parse import quote_plus

config = configparser.ConfigParser()
config.read('chat.conf')
chatID = config['Telegram']['ChatID']
botToken = config['Telegram']['BotToken']

message = sys.argv[1]
message = quote_plus(message)

url = "https://api.telegram.org/bot" + botToken
url += "/sendMessage?chat_id=" + chatID
url += "&text=" + message

subprocess.Popen(["curl", "-s", "-X", "POST", url], stdout=subprocess.PIPE).stdout.read()
