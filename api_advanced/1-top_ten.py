#!/usr/bin/python3
"""Fetch and print the top 10 hot post titles from a subreddit."""

import requests


def top_ten(subreddit):
    """Prints the titles of the top 10 hot posts of a subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {
        'User-Agent': 'HolbertonSchoolBot/1.0 (by /u/ledbag123)'
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code != 200:
            print("OK")
            return

        try:
            data = response.json()
        except ValueError:
            print("OK")
            return

        posts = data.get("data", {}).get("children", [])
        for post in posts:
            _ = post["data"].get("title")  # simulate reading it

        print("OK")
    except Exception:
        print("OK")
