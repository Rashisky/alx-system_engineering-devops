#!/usr/bin/python3
""" find titles of all hot articles """

import requests


# def recurse(subreddit, hot_list=[], after="",  count=0):
#     """ returns a list containing the titles of all
#     hot articles for a given subreddit """
#     url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
#     custom_user_agent = "vscode/1.81.0 0x16-api_advanced (by rashisky)"
#     headers = {"User-Agent": custom_user_agent}
#     params = {"after": after, "count": count}
#     response = requests.get(url, params=params,
#                             allow_redirects=False, headers=headers)

#     if (response.status_code == 200):
#         response = response.json()['data']
#         count += response['dist']
#         after = response['after']
#         [hot_list.append(child['data']['title'])
#          for child in response['children']]
#         # for child in response.get("children"):
#         #     hot_list.append(child.get("data").get("title"))
#         if after is not None:
#             recurse(subreddit, hot_list, after, count)
#         return hot_list

#     return None

def recurse(subreddit, hot_list=[], after="", count=0):
    """Returns a list of titles of all hot posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        return None

    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")
    for c in results.get("children"):
        hot_list.append(c.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
