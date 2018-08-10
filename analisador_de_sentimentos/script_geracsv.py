from __future__ import unicode_literals

import os
import csv

def adicionaDados(palavra_chave, dados, cabecalho):
    path_dir = os.path.join(os.path.expanduser('~/'), 'csv_analise')

    if not os.path.isdir(path_dir):
        os.mkdir(path_dir)

    path_csv = os.path.join(path_dir, palavra_chave + '.csv')

    with open(path_csv, 'a') as f:

        writer = csv.writer(f)
        writer.writerow(cabecalho)

        for (tt, sentimento) in dados:
            dados_inseridos = [tt.id,
                               sentimento,
                               tt.user.id,
                               tt.text.encode('utf-8'),
                               tt.created_at,
                               tt.retweeted,
                               tt.retweet_count,
                               tt.lang]
            writer.writerow(dados_inseridos)

