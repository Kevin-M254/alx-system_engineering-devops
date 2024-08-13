#!/usr/bin/python3
"""function that queries reddit API and prints the
top ten posts on a given reddit"""


import requests


def top_ten(subreddit):
    """function that queries a reddit API and prints
    the top ten posts on a given subreddit"""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(url, headers=headers,
                                allow_redirects=False)
        if response.status_code == 200:
            children = response.json().get('data').get('children')
            for i in range(10):
                print(children[i].get('data').get('title'))
            else:
                print("None")
    except Exception:
        print("None")
