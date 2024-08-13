#!/usr/bin/python

"""
A function that queries th Reddit API and returns
the number of subscribers for a given user
"""

import requests


def number_of_subscribers(subreddit):
    """base url"""
    try:
        response = requests.get(
            'https://www.reddit.com/r/{}/about.json'.format(subreddit),
            params={"raw_json": 1},
            headers={"User-Agent": "Posiayo from Alx"},
            allow_redirects=False)
        response.raise_for_status()
        number_of_sub = response.json().get('data', {}).get('subscribers')
        if number_of_sub is None:
            return 0
        return nuber_of_sub
    except requests.exceptions.RequestException:
        return 0
