import tweepy

chave_api = ""
senha_api = ""

token = ""
token_senha = ""

autenticacao = tweepy.OAuthHandler(chave_api, senha_api)
autenticacao.set_acess_token(token, token_senha)

api = tweepy.API(autenticacao)
