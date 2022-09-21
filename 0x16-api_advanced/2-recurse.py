#!/usr/bin/python3
"""recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit."""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """Returns titles list of hot articles or not"""
    request = requests.get("https://www.reddit.com/r/{}/hot.json".format(
        subreddit),
        headers={"User-Agent": "My User Agent"}, params={"after": after})
    if request.status_code != 200:
        return(None)
    requestData = request.json()
    st = requestData["data"]["after"]
    child = requestData["data"]["children"]
    for each in child:
        hot_list.append(each["data"]["title"])
    if st is not None:
        recurse(subreddit, hot_list, st)
    return(hot_list)
