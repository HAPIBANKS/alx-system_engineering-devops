#!/usr/bin/python

"""
A function that queries th Reddit API and returns
the number of subscribers for a given user
"""

import requests


def number_of_subscribers(subreddit):
    """base url"""
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'user-Agent': 'MyRedditApp/0.1'}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        data = response.json()

        return data['data']['subscribers']
    exceptrequests.exception.HTTPError as http_err:
        if response.status_code == 404:
            print(f"HTTP error occured: {http_err}")
        else:
            print(f"HTTP error occured: {http_err}")
    excep requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")
    return 0
