import tweepy


def authenticate(consumer_key: str, consumer_secret: str, access_token: str, access_token_secret: str):
    auth = tweepy.OAuthHandler(consumer_key=consumer_key, consumer_secret=consumer_secret)
    auth.set_access_token(key=access_token, secret=access_token_secret)

    return tweepy.Client(
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        access_token=access_token,
        access_token_secret=access_token_secret
    )
