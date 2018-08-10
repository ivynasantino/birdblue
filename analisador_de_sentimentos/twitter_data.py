# coding: utf-8


from __future__ import print_function, unicode_literals

from textblob import TextBlob
import tweepy
import json
from auth_handler import auth_object_creator

# API.trends_available()
def tweets_tts(api):
    "Procura tweets baseados nos TTs"
    pass


# API.search(kw[, lang][, locale][, rpp][, page][, since_id][, geocode][, show_user])
def tweets_palavra(api, palavra_chave):
    "Procura tweets sobre uma palavra_chave"
    tweets = []
    for tweet in api.search(palavra_chave):
        sentiment = TextBlob(tweet.text).sentiment.polarity
        tupla_tweet = (tweet, sentiment)
        tweets.append(tupla_tweet)

    return tweets


def api_creator():
    return tweepy.API(auth_object_creator())

