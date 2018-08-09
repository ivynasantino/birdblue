import csv

def gera_coluna_id(nome_csv):
	linha_id = ['id_tt', 
				'sentimento', 
				'id_usuario', 
				'texto', 
				'data', 
				'retweet', 
				'retweet_num',
				'idioma']

	with open (nome_csv, 'a') as data:
		return csv.writer(data).writerow(linha_id)
		
def adicionaDados(tweets_dados, nome_csv):
	
	for (tt, tt_sentiment) in tweets_dados:
		inserir = [tt.id, 
				   tt_sentiment, 
				   tt.user.id, 
				   tt.text,
				   tt.created_at,
				   tt.retweeted,
				   tt.retweet_count,
				   tt.lang]
	
		with open (nome_csv, 'a') as data:
			writer = csv.writer(data)
			writer.writerows(inserir)
