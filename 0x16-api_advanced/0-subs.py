#!/usr/bin/python3

"""
a function that queries the Reddit API and returns the number of subscribers.
"""

from requests import get


def number_of_subscribers(subreddit):
    """Return the number of subscribers for a given subreddit."""

    url = get("https://www.reddit.com/r/{}/about.json".format(subreddit)
              params={"raw_json": 1},
              headers={"user-Agent": "HAPI from ALX"},
              allow_redirects=False)

    try:
        url.raise_for_status()
    except:
        return 0
    else:
        numb_of_sub = url.json().get('data').get('subscribers')
        if numb_of_sub is None:
            return 0
        return numb_of_sub
