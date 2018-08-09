# coding: utf-8

import tweepy
import json

# API.trends_available()
def tweets_tts(api):
    "Procura tweets baseados nos TTs"
    pass


# API.search(kw[, lang][, locale][, rpp][, page][, since_id][, geocode][, show_user])
def tweets_palavra(api, palavra_chave):
    "Procura tweets sobre uma palavra_chave"
    tweets = []
    for tweet in api.search(palavra_chave):
        tweets.append(tweet.text)

    return tweets


def autenticacao(dic_aut):
	autenticacao = tweepy.OAuthHandler(dic_aut['chave_api'], dic_aut['senha_api'])
	autenticacao.set_access_token(dic_aut['token'], dic_aut['token_senha'])

	return autenticacao
	
def main():
    """Provem interação com a API do twitter"""
    with open('auth.json', 'r') as a:
        dic_aut = json.load(a)

    api = tweepy.API(autenticacao(dic_aut))

    palavra_chave = raw_input('Digite a palavra-chave: ')
    tweets = tweets_palavra(api, palavra_chave)

    print tweets


if __name__ == "__main__":
    main()
