#!/usr/bin/python3
"""
   Scrapes the reddit api for top ten hot topics
"""
import requests


def top_ten(subreddit):
    """ Prints top ten hot topics on a subreddit"""
    params = {
        "limit": 10
    }
    headers = {
        "User-Agent": "linux; ubunt; mbuke"
    }
    res = requests.get("https://www.reddit.com/r/{}/hot.json"
                       .format(subreddit),
                       params=params,
                       headers=headers)
    if res.status_code != 200:
        print('None')
        return
    topics = res.json().get('data').get('children')
    [print(t.get('data').get('title')) for t in topics]
