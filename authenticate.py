import tweepy
import config_loader

auth_config: dict = config_loader.load_config()['auth']


def authenticate():
    auth = tweepy.OAuthHandler(consumer_key=auth_config['consumer_key'], consumer_secret=auth_config['consumer_secret'])
    auth.set_access_token(key=auth_config['access_key'], secret=auth_config['access_secret'])

    return tweepy.API(auth, wait_on_rate_limit=True)
