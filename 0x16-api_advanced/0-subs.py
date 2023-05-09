#!/usr/bin/python3
"""
function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """ return the number of subscribers"""
    headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0)\
                    Gecko/20100101 Firefox/80.0'
            }
    req = requests.get('https://www.reddit.com/r/{}/about.json'
                       .format(subreddit),
                       headers=headers,
                       allow_redirects=False)

    if req.status_code != 200:
        return (0)

    req = req.json()
    d = req.get('data', {})
    return (d.get('subscribers', 0))
