#!/usr/bin/python3

import requests


def recurse(subreddit, hot_list=None, after=None):
    """
    Recursively queries the Reddit API and returns a list containing the titles
    of all hot articles for a given subreddit.

    :param subreddit: The subreddit to query.
    :param hot_list: A list that accumulates the titles of hot posts.
    :param after: The "after" parameter for pagination.
    :return: A list of titles, or None if the subreddit is invalid or empty.
    """
    if hot_list is None:
        hot_list = []

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"limit": 100, "after": after}

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            after = data.get('data', {}).get('after')

            if not posts:
                return None

            for post in posts:
                hot_list.append(post.get('data', {}).get('title', 'No Title'))

            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return None
    except Exception:
        return None
