#!/usr/bin/python3
"""
Prints the titles of the first 10 hot posts
"""
import requests


def top_ten(subreddit):
    """returns titles of the first 10 hot posts"""
    params = {"limit": 10}
    headers = {"User-agent": "Andre"}
    res = requests.get("https://www.reddit.com/r/{}/hot.json".format(
        subreddit),
        headers=headers, allow_redirects=False, params=params)
    if res.status_code == 200:
        data = res.json()
        posts = data["data"]["children"]
        if data["data"]["dist"] == 0:
            print(None)
        else:
            for post in posts:
                print(post["data"]["title"])
    else:
        print(None)
