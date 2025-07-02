#!/usr/bin/python3
"""
Reddit Subscriber Counter

This script defines a function to query the Reddit API and return
the number of subscribers for a given subreddit.

If the subreddit is invalid or cannot be accessed, it returns 0.
"""

import requests


def number_of_subscribers(subreddit):
   """
    Queries the Reddit API and returns the number of subscribers
    for the specified subreddit.

    Args:
        subreddit (str): The subreddit name (e.g., "python").

    Returns:
        int: The number of subscribers, or 0 if the subreddit is invalid.
    """
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
