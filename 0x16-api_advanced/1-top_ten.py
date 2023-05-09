#!/usr/bin/python3
"""
a function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """ return the top 10 hot titles"""
    headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0)\
                    Gecko/20100101 Firefox/80.0'
            }

    req = requests.get('https://www.reddit.com/r/{}/.json'
                       .format(subreddit),
                       headers=headers,
                       params={'limit': 10})

    req = req.json()
    top = req.get('data', {}).get('children', None)

    if top is None or (len(top) > 0 and top[0].get('kind') != 't3'):
        print(None)
    else:
        for t in top:
            print(t.get('data', {}).get('title', None))
