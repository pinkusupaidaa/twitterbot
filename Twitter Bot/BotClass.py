import datetime
import tweepy
import json
import os
from time import sleep

class authorization:
    def __init__(self, Consumer_key, Consumer_secret, Access_token, Access_secret):
        self.consumer_key = Consumer_key
        self.consumer_secret = Consumer_secret
        self.access_token = Access_token
        self.access_secret = Access_secret

class TwitterBot:
    def __init__(self, Searchdate, Search_for_hashtag, Authobj, Retweet_and_follow = 0, Favorite_tweet = 0):
        self.authobj = Authobj
        self.search_date = Searchdate
        self.search_for_hashtag = Search_for_hashtag

        self.auth = tweepy.OAuthHandler(self.authobj.consumer_key, self.authobj.consumer_secret)
        self.auth.set_access_token(self.authobj.access_token, self.authobj.access_secret)
        self.auth.secure = True
        self.api = tweepy.API(self.auth)

        self.myBot = self.api.get_user(screen_name='@SkattBot')

        self.since_id_var = 899171837040525312
        self.retweet_and_follow = Retweet_and_follow
        self.favorite_tweet = Favorite_tweet


    def set_date(self, x):
        try:
            if isinstance(x, datetime.datetime):
                self.search_date = x
        except:
            print("Variable " + x + " is not a datetime object")

    def set_hashtag(self, tag):
        self.search_for_hashtag = tag

    def start_retweeting(self):
        #public_tweets = self.api.user_timeline(screen_name="@AntonStarck", count=5)
        #for tweet in public_tweets:
        #    print(tweet.text)
        #    sleep(2)
        #self.write_to_file("test.txt", public_tweets)
        while 1:
            for tweet in tweepy.Cursor(self.api.search, q=self.search_for_hashtag, since=self.search_date).items():
                try:
                    if tweet.user.id == self.myBot.id: #If you yourself has already retweeted it, just continue algorithm
                        continue
                    print("\n\nFound tweet by: @" + tweet.user.screen_name)
                    if (tweet.retweeted == False) or (tweet.favorited == False):
                        tweet.retweet()
                        print("Retweeted tweet from @" + tweet.user.screen_name)
                        print(tweet.id)

                        if tweet.id > self.since_id_var:
                            self.since_id_var = tweet.id

                        if self.favorite_tweet:
                            tweet.favorite()

                        if self.retweet_and_follow:
                             if(tweet.user.following == False):
                                 tweet.user.follow()
                                 print("Followed the user")

                except tweepy.TweepError as e:
                    if tweet.id > self.since_id_var:
                        self.since_id_var = tweet.id
                        print(self.since_id_var)
                    print(tweet.id)
                    print(e.reason)
                    if "429" in e.reason or "185" in e.reason:
                        sleep(1800)
                        # else:
                        # sleep(5)
                    continue
                except StopIteration:
                    break
            print("Pausar botten i 30 minuter")
            sleep(1800)

    def write_to_file(self, filename, data):
        a = []
        #lägg till en koll så man inte appendar samma tweets flera gånger
        for tweet in data:
            a.append(tweet.text)
            a.append(str(tweet.created_at))
        if not os.path.isfile(filename):
            with open(filename, "w") as f:
                for item in a:
                    f.write(item + '\n')
        else:
            with open(filename, "a") as f:
                for item in a:
                    f.write(item + '\n')
