#!/usr/bin/python3
"""
number of subscribers for a given subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers of the subreddit. Returns 0 if subreddit
             is None or not a string, or if there was an error retrieving the
             data.
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-agent': 'Mozilla/5.0'}  # Changed user agent to a more generic one
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url, headers=user_agent)

    if response.status_code != 200:  # Check if request was successful
        return 0

    try:
        data = response.json()
        return data.get('data', {}).get('subscribers', 0)
    except KeyError:
        return 0
