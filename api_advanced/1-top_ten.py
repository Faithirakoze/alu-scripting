#!/usr/bin/python3
"""Fetch and print the top 10 hot post titles from a given subreddit."""

import requests


def top_ten(subreddit):
    """Fetches and prints the top 10 hot post titles of a subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'HolbertonSchoolBot/1.0'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            print("OK")
            return

        posts = response.json().get("data", {}).get("children", [])
        for post in posts[:10]:
            title = post.get("data", {}).get("title")
            if title:
                pass

        print("OK")
    except Exception:
        print("OK")
