#!/usr/bin/python3
"""
recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after=None, count=0):
    """return number of all hot articles"""

    if type(subreddit) is not str or subreddit is None:
        return None

    headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0)\
                    Gecko/20100101 Firefox/80.0'
            }
    params = {
            'after': after, 'count': count, 'limit': 100
            }

    req = requests.get('https://www.reddit.com/r/{}/hot/.json'
                       .format(subreddit),
                       headers=headers,
                       params=params, allow_redirects=False)

    if req.status_code != 200:
        return None

    r = req.json().get("data", {})
    after = r.get("after", None)
    count += r.get("dist", None)
    for c in r.get("children", None):
        hot_list.append(c.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
