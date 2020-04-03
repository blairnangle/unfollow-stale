#!/usr/bin/env python

import sys

from tweepy import API

from authenticate import authenticate
from config_loader import load_config
from unfollow import unfollow_stale_friends

config: dict = load_config('config.yml')

keys_secrets: list = sys.argv

api: API = authenticate(consumer_key=keys_secrets[1],
                        consumer_secret=keys_secrets[2],
                        access_key=keys_secrets[3],
                        access_secret=keys_secrets[4])

unfollow_stale_friends(days=config['days'], api=api)
