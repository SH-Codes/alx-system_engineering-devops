#!/usr/bin/python3

"""prints the titles of the first 10 hot posts listed for a given subreddit
"""

from requests import get


def top_ten(subreddit):

    """
    Function that queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit.
    """

    if subreddit is None or not isinstance(subreddit, str):
        print("None")
        return

    user_agent = {'User-agent': 'Microsoft Edge Version 124.0.2478.67'}
    params = {'limit': 10}
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)

    try:
        response = get(url, headers=user_agent, params=params)
        # Check if the request was successful
        if response.status_code != 200:
            print("None")
            return

        results = response.json()
        my_data = results.get('data', {}).get('children', [])

        if not my_data:
            print("None")
            return

        for item in my_data:
            print(item.get('data', {}).get('title', 'No Title'))
    except Exception:
        print("None")
