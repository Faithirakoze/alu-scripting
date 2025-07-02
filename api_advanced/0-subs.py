#!/usr/bin/python3
"""Module that fetches the number of subscribers for a given subreddit.

This script queries the Reddit API for the given subreddit and returns
the total number of subscribers. If the subreddit is invalid, it returns 0.
"""

import requests
import sys


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a subreddit using Reddit's API."""
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


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Please pass an argument for the subreddit to search.")
        sys.exit(1)

    subreddit = sys.argv[1]
    count = number_of_subscribers(subreddit)
    print(count)
    sys.exit(0)
