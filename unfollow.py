from tweepy import Client

from time_utils import current_epoch_minus_days, time_to_epoch


def unfollow_stale_accounts(days: int, client: Client) -> None:
    my_id: int = client.get_me().data.id
    following_ids: [(str, str)] = [(user.data["id"], user.data["username"]) for user in client.get_users_following(id=my_id, max_results=1000, user_auth=True).data]

    unfollowed = 0
    for user_id, username in following_ids:
        response = client.get_users_tweets(id=user_id, max_results=5, user_auth=True, tweet_fields=["created_at"])
        if response.data is None:
            client.unfollow_user(target_user_id=user_id)
            print(f"Unfollowed @{username}. They have never tweeted.")
            unfollowed += 1
        else:
            most_recent_tweet_timestamp: str = response.data[0].data["created_at"]
            epoch_last_tweet: int = time_to_epoch(str(most_recent_tweet_timestamp))

            if epoch_last_tweet < current_epoch_minus_days(days):
                client.unfollow_user(target_user_id=user_id)
                print(f"Unfollowed @{username}. They last tweeted on {most_recent_tweet_timestamp.split('T')[0]}.")
                unfollowed += 1

    new_following_ids: [int] = [user.data["id"] for user in client.get_users_following(id=my_id, max_results=1000, user_auth=True).data]

    print(f"Unfollowed {unfollowed} accounts. You are now following {len(new_following_ids)} accounts.")
