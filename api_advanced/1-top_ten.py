#!/usr/bin/python3
"""
This script queries the Reddit API
and prints the titles of the first 10 hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts
    listed for a given subreddit."""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': '/u/Faith1 API Python'}
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code == 200:
        posts = r.json()["data"]["children"]
        for post in posts[:10]:
            print(post["data"]["title"])
    else:
        return (print("None"))
