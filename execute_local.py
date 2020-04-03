#!/usr/bin/env python

from tweepy import API

from authenticate import authenticate
from config_loader import load_config
from unfollow import unfollow_stale_friends

auth_config: dict = load_config('auth_config.yml')
config: dict = load_config('config.yml')

api: API = authenticate(consumer_key=auth_config['consumer_key'],
                        consumer_secret=auth_config['consumer_secret'],
                        access_key=auth_config['access_key'],
                        access_secret=auth_config['access_secret'])

unfollow_stale_friends(days=config['days'], api=api)
