#!/usr/bin/env
# coding:utf-8

from setuptools import setup

setup(name='analisador-sentimentos',
      version='0.1',
      description='Analisador de sentimentos do twitter',
      author='Ivyna Santino, Pedro Espíndula',
      author_email='ivyna.alves@ccc.ufcg.edu.br',
      url='',
      packages=['analisador-sentimentos'],
      install_requires=[
          'textblob',
          'tweepy'
          ],
      scripts=['bin/analise_sentiment'],
      )
