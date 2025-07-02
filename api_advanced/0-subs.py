#!/usr/bin/python3
"""Returns the number of subscribers
 for a given subreddit using Reddit's API."""

import requests


def number_of_subscribers(subreddit):
    """Queries Reddit API to get number of subscribers of a subreddit."""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': '/u/Faith1 API Python'}
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code == 200:
        return r.json()["data"]["subscribers"]
    return 0
