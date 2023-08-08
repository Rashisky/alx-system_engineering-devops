#!/usr/bin/python3
""" finds the top 10 titles """

import requests
from sys import argv


def top_ten(subreddit):
    """ returns top 10 hot titles """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    custom_user_agent = "vscode/1.81.0 0x16-api_advanced (by rashisky)"
    headers = {"User-Agent": custom_user_agent}
    response = requests.get(url, allow_redirects=False, headers=headers)

    if (response.status_code == 200):
        print(response.status_code)
        response = response.json()['data']['children']
        for i in range(10):
            print(response[i]['data']['title'])

    print("None")
