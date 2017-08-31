from tkinter import *
from tkinter import ttk
import BotClass
import datetime
import os

zeCredentials = BotClass.authorization
def set_credentials():
    zeCredentials.consumer_key = consumer_key.get()
    zeCredentials.consumer_secret = consumer_secret.get()
    zeCredentials.access_token = access_token.get()
    zeCredentials.access_secret = access_token_secret.get()

    save_settings_to_file()

def save_settings_to_file():
    a = []
    read_settings = []

    a.append( zeCredentials.consumer_key)
    a.append( zeCredentials.consumer_secret)
    a.append( zeCredentials.access_token)
    a.append( zeCredentials.access_secret)
    a.append(str(hash_tag.get()))

    if not os.path.isfile("settings.txt"):
        with open("settings.txt", "w") as f:
            for item in a:
                f.write(item + '\n')
    else:
        with open("settings.txt", "r") as f:
            for line in f:
                read_settings.append(line)
       # for derp in read_settings:
       #     print(derp)

def load_settings_file():
    read_settings = []

    
    if not os.path.isfile("settings.txt"):
        print("No file namned settings.txt exists")
    else:
        with open("settings.txt", "r") as f:
            for line in f:
                read_settings.append(line)
        #for derp in read_settings:
         #   print(derp)

    consumer_key.set(read_settings[0][:-1])
    consumer_secret.set(read_settings[1][:-1])
    access_token.set(read_settings[2][:-1])
    access_token_secret.set(read_settings[3][:-1])
    hash_tag.set(read_settings[4][:-1])

    zeCredentials.consumer_key = consumer_key.get()
    zeCredentials.consumer_secret = consumer_secret.get()
    zeCredentials.access_token = access_token.get()
    zeCredentials.access_secret = access_token_secret.get()


def start_ze_shit(zeHash, x):
    stringZeHash = str("#" + zeHash)
    now = datetime.datetime.now()
    todays_date = str(now.year) + '-' + str(now.month) + '-' + str(now.day)
    print("DAGENS DATUM : ", todays_date)
    ze_bot = BotClass.TwitterBot(todays_date , stringZeHash, zeCredentials)
    ze_bot.set_time_to_sleep(x)
    ze_bot.retweeting_thread()

root = Tk()


consumer_key = StringVar()
consumer_secret = StringVar()
access_token = StringVar()
access_token_secret = StringVar()

time_to_sleep = IntVar()

hash_tag = StringVar()

consumer_key.set("Enter Consumer Key")
consumer_secret.set("Enter Consumer Token")
access_token.set("Enter Access Token")
access_token_secret.set("Enter Access Secret")
hash_tag.set("Enter Hash To Retweet")

ttk.Label(root, text="HERP DERP").grid(row=0, column=0, sticky=W)
strEntry = Entry(root, textvariable=consumer_key)
strEntry.grid(row=1, column=0, sticky=W)
strEntry = Entry(root, textvariable=consumer_secret)
strEntry.grid(row=1, column=0, sticky=W)
strEntry = Entry(root, textvariable=access_token)
strEntry.grid(row=2, column=0, sticky=W)
strEntry = Entry(root, textvariable=access_token_secret)
strEntry.grid(row=3, column=0, sticky=W)
strEntry = Entry(root, textvariable=hash_tag)
strEntry.grid(row=4, column=0, sticky=W)

intEntry = Entry(root, textvariable=time_to_sleep)
intEntry.grid(row=5, column=0, sticky=W)

save_settings_button = ttk.Button(root, text="Save Settings", command=lambda : set_credentials())
save_settings_button.grid(row=6, column=0, sticky=W)

load_settings_file_button = ttk.Button(root, text="Load Settings", command=lambda : load_settings_file())
load_settings_file_button.grid(row=6, column=1, sticky=W)

start_bot_button = ttk.Button(root, text="Start Bot", command=lambda : start_ze_shit(hash_tag.get(), time_to_sleep.get()))
start_bot_button.grid(row=6, column=2, sticky=W)


root.mainloop()