#!/usr/bin/python3
"""
A sript that, uses a REST API, for a given employee ID, returns
information about his/her TODO list progress
and exports data in the JSON format.
"""
import json
import requests
from sys import argv


if __name__ == '__main__':
    user = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    ).json()

    todos = requests.get(
        'https://jsonplaceholder.typicode.com/todos/',
        params={'userId': argv[1]}
    ).json()

    val = []

    for todo in todos:
        val.append({
            "task": todo.get('title'),
            "completed": todo.get('completed'),
            "username": user.get('username')
        })

    dict_ = {
        user.get('id'): val
    }

    with open('{}.json'.format(argv[1]), 'w') as f:
        json.dump(dict_, f)
