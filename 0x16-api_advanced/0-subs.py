#!/usr/bin/python3
"""
  queries the reddit api and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """ Returns num of subscribers"""
    headers = {
        'User-Agent': 'linux;ubuntu; mbuke'
    }
    res = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers=headers,
        allow_redirects=False)
    if res.status_code != 200:
        return 0
    return res.json().get('data').get('subscribers')
