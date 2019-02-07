#!/usr/bin/env python3

import configparser
import subprocess
import json

config = configparser.ConfigParser()
config.read('chat.conf')
botToken = config['Telegram']['BotToken']

url = "https://api.telegram.org/bot" + botToken + "/getUpdates"
response = subprocess.Popen(["curl", "-s", "-X", "POST", url], stdout=subprocess.PIPE).stdout.read()

try:
	data = json.loads(response)
	latestMsg = data["result"][-1]
except:
	print("No messages")
	exit()

username = latestMsg["message"]["from"]["username"]
name = latestMsg["message"]["from"]["first_name"]
chatID = latestMsg["message"]["chat"]["id"]
content = latestMsg["message"]["text"]

print("Message from: " + name)
print("Content: " + content)
