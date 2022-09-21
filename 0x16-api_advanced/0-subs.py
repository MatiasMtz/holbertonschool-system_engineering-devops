#!/usr/bin/python3
"""function that queries the Reddit API and returns the number of
subscribers or 0"""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    user_Agent = 'My User Agent'

    headers = {"User-Agent": user_Agent}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
