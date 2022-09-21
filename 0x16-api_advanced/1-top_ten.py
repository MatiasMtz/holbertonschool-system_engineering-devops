#!/usr/bin/python3
"""function that queries the Reddit API and prints the titles of the
first 10 hot posts listed for a given subreddit."""
import requests


def top_ten(subreddit):
    """prints top 10 hot posts"""
    url = "https://www.reddit.com/r/{}/.json?limit=10".format(subreddit)
    headers = {'user-agent': 'MyAPI/0.0.1'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        try:
            data = response.json().get("data")
            child = data.get("children")
            for each in child[:10]:
                print(each.get("data").get("title"))
        except Exception:
            print(None)
    else:
        print(None)
