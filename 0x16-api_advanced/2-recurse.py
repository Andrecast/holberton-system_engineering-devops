#!/usr/bin/python3
"""
Prints the titles of all hot articles
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """returns titles of all hot articles"""
    params = {"after": after}
    headers = {"User-agent": "Andre"}
    data = requests.get("https://www.reddit.com/r/{}/hot.json".format(
        subreddit),
        headers=headers, allow_redirects=False, params=params)
    if data.status_code == 200:
        data = data.json()
        posts = data["data"]["children"]
        after = data["data"]["after"]
        if after is None:
            return hot_list
        else:
            hot_list.append(posts[0]["data"]["title"])
            return recurse(subreddit, hot_list, after)
    else:
        return None