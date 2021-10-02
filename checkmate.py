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
def hello():
    global site
    site = mytext.get()
    print(site)
    with suppress(Exception):  ## https://hg.python.org/cpython/rev/406b47c64480 
        while (1):
            try:
                x = (urllib.request.urlopen(site).getcode())  
                ## Will return 200 if status = OK
                if x == 200:
                        print("Connected successfully. Sent message to telegram")
                        s = f"Connected Successfully to {site}"
                        telegram_bot_sendtext(s)
                        show_text = Label(root, text = s)
                        show_text.pack()
                        break
    else:
                    print("Something is wrong")
            except:
                e="Trying again"
                print(e)
                show_e = Label(root, text = e)
                show_e.pack()
                time.sleep(1)
                continue
