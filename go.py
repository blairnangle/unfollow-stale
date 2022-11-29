#!/usr/bin/env python

import os
from tweepy import Client
from authenticate import authenticate
from unfollow import unfollow_stale_accounts

client: Client = authenticate(consumer_key=os.getenv("CONSUMER_KEY"),
                              consumer_secret=os.getenv("CONSUMER_KEY_SECRET"),
                              access_token=os.getenv("ACCESS_TOKEN"),
                              access_token_secret=os.getenv("ACCESS_TOKEN_SECRET"))

unfollow_stale_accounts(days=365, client=client)
