# coding: utf-8

import tweepy
import json


def trending_topics(api):
    pass


def tweets_palavra(api, palavra_chave):
    "Procura tweets sobre uma palavra_chave"
    tweets = []
    for tweet in api.search(palavra_chave):
        tweets.append(tweet.text)

    return tweets


def main():
    """Provem interação com a API do twitter"""
    with open('auth.json', 'r') as a:
        dic_aut = json.load(a)

    autenticacao = tweepy.OAuthHandler(dic_aut['chave_api'], dic_aut['senha_api'])
    autenticacao.set_access_token(dic_aut['token'], dic_aut['token_senha'])

    api = tweepy.API(autenticacao)

    palavra_chave = raw_input('Digite a palavra-chave: ')
    tweets = tweets_palavra(api, palavra_chave)

    print tweets

    return tweets


if __name__ == "__main__":
    main()

