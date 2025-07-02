#!/usr/bin/python3
"""Fetches the number of subscribers for a subreddit.

Uses the Reddit API to retrieve the number of subscribers for a given
subreddit. If the subreddit is invalid, it returns 0.
"""

import requests
import sys


def number_of_subscribers(subreddit):
    """Return the number of subscribers for a given subreddit.

    Args:
        subreddit (str): Name of the subreddit

    Returns:
        int: Number of subscribers, or 0 if invalid
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "0-subs.py/0.1"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            return response.json().get("data", {}).get("subscribers", 0)
        return 0
    except Exception:
        return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-subs.py <subreddit>")
        sys.exit(1)
    print(number_of_subscribers(sys.argv[1]))
