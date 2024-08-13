#!/usr/bin/python3
"""Function that queries the reddit API and returns
number of subscribers for a given reddit"""

import requests


def number_of_subscribers(subreddit):
    """Function that queries the reddit API and returns
    number of subscribers for a given reddit"""
    url = "http://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data.get('data').get('subscribers')
    else:
        return 0
