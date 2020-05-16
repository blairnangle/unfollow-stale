# Unfollow Stale

Script to unfollow Twitter accounts that have gone a specified number of days without tweeting.

Makes use of the [Twitter API](https://developer.twitter.com/en/docs/api-reference-index) and 
[Tweepy](https://www.tweepy.org).

## Prerequisites

* [Python 3](https://www.python.org/downloads/)
* [pip](https://pypi.org/project/pip/) (included by default with Python versions >= 3.4)
* [venv](https://docs.python.org/3/library/venv.html) (included by default with Python versions >= 3.3)

## Installation

* Create a virtual environment:

```bash
$ python3 -m venv .venv
```
* Activate the virtual environment:

```bash
$ source .venv/bin/activate
```

* Install requirements:

```bash
$ pip install -r requirements.txt
```

## Usage

### Obtaining Authentication Tokens

You will need to create a Twitter App to generate authentication keys and tokens. Navigate to 
[Twitter Apps](https://developer.twitter.com/en/apps/create), sign in with your Twitter credentials and create a new 
app:

![Create Twitter App](create-twitter-app.png)

Accept the terms, go to "Keys and tokens" and generate an access token and secret key.

### Configuring

Add your keys and tokens from your Twitter app to `config.yml`:

```yaml
auth:
  consumer_key: 'your consumer key'
  consumer_secret: 'your consumer secret'
  access_key: 'your access key'
  access_secret: 'your access secret'
days: 365  # Accounts with their most recent tweet further in the past than this will be unfollowed
```

### Executing

To run the script (the virtual environment needs to have been activated using [above instructions](#installation)):

```bash
$ ./execute.py
```
