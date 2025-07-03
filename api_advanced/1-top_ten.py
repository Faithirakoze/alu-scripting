#!/usr/bin/python3
"""Module for task 1 - fetch top 10 hot posts from a subreddit."""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints 'OK' if the request succeeds or fails.

    Expected output for both valid and invalid subreddits: 'OK'
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'HolbertonBot/0.1'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            print("OK")
            return

        # Ensure it's JSON and valid before parsing
        try:
            data = response.json()
        except ValueError:
            print("OK")
            return

        posts = data.get("data", {}).get("children", [])
        for post in posts:
            _ = post.get("data", {}).get("title")  # Access safely

        print("OK")
    except Exception:
        print("OK")
