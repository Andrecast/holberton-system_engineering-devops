#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
    headers = {'User-Agent': 'Andre'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code == 200:
        data = res.json()
        return data['data']['subscribers']
    return 0
