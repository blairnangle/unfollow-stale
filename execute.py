#!/usr/bin/env python

import config_loader
from unfollow import unfollow_stale_friends

config: dict = config_loader.load_config()

unfollow_stale_friends(config['days'])
