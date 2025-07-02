#!/usr/bin/python3
"""
This script queries the Reddit API and returns the number of subscribers
for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a valid subreddit,
      otherwise returns 0"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "0-subs.py/0.1"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            return response.json().get("data", {}).get("subscribers", 0)
        else:
            return 0

    except Exception:
        return 0
