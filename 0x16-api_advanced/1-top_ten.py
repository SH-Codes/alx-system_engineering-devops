#!/usr/bin/python3

<<<<<<< HEAD
"""Prints the titles of the first 10 hot posts listed for a given subreddit"""
=======
"""
Prints the titles of the first 10 hot posts listed for a given subreddit.
"""
>>>>>>> a46235057e8e5a21cf47637b5deb5dfbdeec9827

from requests import get


def top_ten(subreddit):
    """
<<<<<<< HEAD
    Function that queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit
=======
    Queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit.
>>>>>>> a46235057e8e5a21cf47637b5deb5dfbdeec9827
    """
    if subreddit is None or not isinstance(subreddit, str):
        print("None")
        return

    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    params = {'limit': 10}
<<<<<<< HEAD
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json'
    
    try:
        response = get(url, headers=user_agent, params=params, timeout=10)
        # Check for valid response
        if response.status_code != 200:
            print("None")
            return
        
        results = response.json()
        my_data = results.get('data', {}).get('children', [])

        if not my_data:
            print("None")
            return
        
        for post in my_data:
            print(post.get('data', {}).get('title', "None"))
    except Exception as e:
=======
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)

    try:
        response = get(
                url, headers=user_agent, params=params, allow_redirects=False
                )

        if response.status_code != 200:
            print("None")
            return

        results = response.json()
        my_data = results.get('data', {}).get('children', [])

        for item in my_data:
            print(item.get('data', {}).get('title', 'None'))

    except Exception:
>>>>>>> a46235057e8e5a21cf47637b5deb5dfbdeec9827
        print("None")
