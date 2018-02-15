import tweepy
from time import sleep
import RPi.GPIO as GPIO
from random_words import RandomWords

from Keys import *

GPIO.setmode(GPIO.BCM)
GPIO.setup(20,GPIO.IN,pull_up_down=GPIO.PUD_UP)


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCES_TOKEN, ACCES_SECRET)
api = tweepy.API(auth)
while True:
    if GPIO.input(20) == False:
        rw = RandomWords()
        word = rw.random_word()
        for tweet in tweepy.Cursor(api.search, q=word).items(1):
            try:
                print('\nRetweet Bot found tweet by @' + tweet.user.screen_name + '.'+ 'Attempting to retweet')
                print('random word is:' + word)
                tweet.retweet()
                print('retweet published succesfully.')            
        
                sleep (1)
        
            except tweepy.TweepError as error:
                print('\nError. Retweet not succesful. Reason:')
                print(error.reason)
        
        
            except StopIteration:
                break