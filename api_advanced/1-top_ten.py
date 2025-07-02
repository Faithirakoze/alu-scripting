#!/usr/bin/python3
"""Fetch and print the top 10 hot post titles from a subreddit."""

import requests
import sys


def top_ten(subreddit):
    """Read Reddit API and print top 10 hot post titles of a subreddit."""
    headers = {'user-agent': '/u/ledbag123 API Python for Holberton School'}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)

    client = requests.session()
    client.headers = headers

    r = client.get(url, allow_redirects=False)

    if r.status_code == 200:
        list_titles = r.json().get('data', {}).get('children', [])
        for post in list_titles[:10]:
            print(post['data'].get('title'))
    else:
        print("None")
