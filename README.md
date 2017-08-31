# twitterbot
A very simple bot that uses tweepy. It retweets and favorites the tweet based on hashtag (just retweet at the moment). 
It's still under development and I just recently added a very simple GUI (TkInter)that lets you
enter all the keys and access tokens and saves them to a file located in the same folder as the project. 
So when you start up the program you can just load in the keys and access tokens. The idea is that you
should be able to load in settings from different twitter accounts and run multiple bots.
You can also run multiple bots on just one twitter account. Just change the hashtag you want it to retweet and press "start bot".
It starts a new thread running that process.

For now you cant stop individual threads (bots) from running. You will have to shut down the program to kill the threads.
