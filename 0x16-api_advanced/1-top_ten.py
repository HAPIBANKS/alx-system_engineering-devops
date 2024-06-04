#!/usr/bin/python3

"""
a function that queries the Reddit API and prints
the titles of the first 10 hot posts listed.
"""
import requests
from sys import argv


def top_ten(subreddit):

    """
        print the title of the first ten posts for a subreddit
    """
    user = {'User-Agent': 'Lizzie'}
    url = requests.get('https://www.reddit.com/r/{}/hot/.json?limit=10'
                       .format(subreddit), headers=user).json()
    try:
        for post in url.get('data').get('children'):
            print(post.get('data').get('title'))
    except Exception:
        print(None)


if __name__ == "__main__":
    top_ten(argv[1])
