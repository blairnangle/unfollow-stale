import tweepy


def authenticate(consumer_key: str, consumer_secret: str, access_key: str, access_secret: str):
    auth = tweepy.OAuthHandler(consumer_key=consumer_key, consumer_secret=consumer_secret)
    auth.set_access_token(key=access_key, secret=access_secret)

    return tweepy.API(auth, timeout=900, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
