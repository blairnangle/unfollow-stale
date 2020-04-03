from tweepy import API

from time_utils import current_epoch_minus_days, time_to_epoch


def unfollow_friend(user_id: int, no_tweets: bool, api: API, last_tweet=None) -> None:
    screen_name: str = api.get_user(user_id=user_id).__getattribute__('screen_name')
    api.destroy_friendship(screen_name=screen_name)

    if no_tweets:
        reason = 'They do not have any tweets, they may never have tweeted.'
    else:
        reason = 'They last tweeted on {date} at {time}.'.format(date=str(last_tweet.created_at).split()[0],
                                                                 time=str(last_tweet.created_at).split()[1])

    print('Unfollowed @{friend}. {reason}\n'.format(friend=screen_name, reason=reason))


def unfollow_stale_friends(days: int, api: API) -> None:
    unfollowed = 0

    friends_ids: list = api.friends_ids()

    for user_id in friends_ids:
        friends_tweets = api.user_timeline(user_id=user_id, count=1)
        if not friends_tweets:
            unfollow_friend(user_id=user_id, no_tweets=True, api=api)
            unfollowed += 1
            continue

        last_tweet = friends_tweets[0]

        epoch_last_tweet: int = time_to_epoch(str(last_tweet.created_at))

        if epoch_last_tweet < current_epoch_minus_days(days):
            unfollow_friend(user_id=user_id, no_tweets=False, api=api, last_tweet=last_tweet)
            unfollowed += 1

    print(
        'Unfollowed {unfollowed} accounts. You are now following {new_friends} accounts.'.format(unfollowed=unfollowed,
                                                                                                 new_friends=len(
                                                                                                     api.friends_ids())))
