# coding: utf-8

import json
import os
import tweepy

def auth_creator():
    auth = {"chave_api":"",
            "senha_api":"",
            "token":"",
            "token_senha":""}

    default_path = os.path.join(os.path.expanduser('~/'), '.analisador_de_sentimentos')

    if not os.path.isdir(default_path):
        os.mkdir(default_path)

    auth_path = os.path.join(default_path, 'auth.json')

    for k,_ in auth.items():
        entry = raw_input(k + ': ')
        auth[k] = entry

    with open(auth_path, 'w') as f:
        json.dump(f, auth)

def auth_retriever():
    default_path = os.path.join(os.path.expanduser('~/'), '.analisador_de_sentimentos')
    auth_path = os.path.join(default_path, 'auth.json')

    if not os.path.isdir(default_path) or not os.path.isfile(auth_path):
        auth_creator()

    with open(auth_path, 'r') as f:
        return json.load(f)

def auth_object_creator():
    dic_auth = auth_retriever()
    auth_object = tweepy.OAuthHandler(dic_auth['chave_api'], dic_auth['senha_api'])
    auth_object.set_access_token(dic_auth['token'], dic_auth['token_senha'])

    return auth_object

