#!/usr/bin/python3
"""getting data from an api
"""

import requests
from sys import argv


def get_user_data(user_id):
    endpoint = "https://jsonplaceholder.typicode.com/"
    try:
        user_response = requests.get(
            endpoint + "users/{}".format(user_id), verify=False)
        # Raise an error for HTTP status codes indicating failure
        user_response.raise_for_status()
        user = user_response.json()

        todo_response = requests.get(
            endpoint +
            "todos?userId={}".format(user_id),
            verify=False)
        # Raise an error for HTTP status codes indicating failure
        todo_response.raise_for_status()
        todo = todo_response.json()

        return user, todo

    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return None


if __name__ == '__main__':
    if len(argv) != 2:
        print("Usage: python script.py <user_id>")
        exit(1)

    user_id = argv[1]
    user_data = get_user_data(user_id)
    if user_data:
        user, todo = user_data
        completed_tasks = [task['title']
                           for task in todo if task.get('completed')]
        print("Employee {} is done with tasks({}/{}):".format(user.get('name'),
              len(completed_tasks), len(todo)))
        for task in completed_tasks:
            print("\t", task)
