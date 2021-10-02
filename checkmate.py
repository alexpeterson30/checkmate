  from tkinter import*
import os
import urllib
import requests
from contextlib import suppress
import time


os.system('clear')
# site = "https://www.google.com"

def telegram_bot_sendtext(bot_message):
   endpt = 'https://api.telegram.org/bot'
   bot_token = '1301415216:AAHO2QF7FZOJ4mTxBeF02lL19w7-BQhm3lA'
   action = '/sendMessage?chat_id='
   bot_chatID = '@websitechecktest'
   mode = '&parse_mode=Markdown&text='
   
   send_text = endpt + bot_token + action + bot_chatID + mode + bot_message
   response = requests.get(send_text)
   return response.json()
