#!/usr/bin/python

"""
A function that queries th Reddit API and returns
the number of subscribers for a given user
"""

import requests


def number_of_subscribers(subreddit):
    """Use GET request to find number of subscribers to `subreddit`"""
    r = get("https://www.reddit.com/r/{}/about.json".format(subreddit),
            params={"raw_json": 1},
            headers={"User-Agent": "Andrew from Holberton"},
            allow_redirects=False)
    try:
        r.raise_for_status()
    except:
        return 0
    else:
        num_subscribers = r.json().get('data').get('subscribers')
        if num_subscribers is None:
            return 0
        return num_subscribers
