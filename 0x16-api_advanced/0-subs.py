#!/usr/bin/python3
""" finds the number of subscribers """

import requests
from sys import argv


def number_of_subscribers(subreddit):
    """ returns total number of subscribers """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    custom_user_agent = "vscode/1.81.0 0x16-api_advanced (by rashisky)"
    headers = {"User-Agent": custom_user_agent}
    response = requests.get(url, allow_redirects=False, headers=headers)

    if (response.status_code == 200):
        response = response.json()
        return response['data']['subscribers']

    return 0
