
import datetime
import BotClass as bc
import config
from time import sleep



auth_obj = bc.authorization(config.consumer_key, config.consumer_secret, config.access_token, config.access_token_secret)

now = datetime.datetime.now()
todays_date = str(now.year) + '-' + str(now.month) + '-' + str(now.day)

ze_bot = bc.TwitterBot(todays_date , "#svpol", auth_obj)
ze_bot.start_retweeting()
