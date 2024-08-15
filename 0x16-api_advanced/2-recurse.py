#!/usr/bin/python3
"""
Using Reddit's API to recursively retrieve hot post titles.
"""

import requests


def recurse(subreddit, hot_list=None, after=None):
    """Returns a list of titles of all hot posts recursively."""
    if hot_list is None:
        hot_list = []

    user_agent = {'User-Agent': 'api_advanced-project'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {'after': after}

    try:
        response = requests.get(url, params=params, headers=user_agent,
                                allow_redirects=False)

        if response.status_code == 200:
            data = response.json().get("data", {})
            after = data.get("after")
            titles = [
                    post.get("data", {}).get("title")
                    for post in data.get("children", [])
                    ]

            hot_list.extend(titles)

            if after is not None:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return None
    except Exception:
        return None
