#!/usr/bin/python3
"""
Write a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
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

    dones = []
    for todo in todos:
        if todo['completed'] is True:
            dones.append(todo['title'])
    print('Employee {} is done with tasks({}/{}):'.format(
        user['name'], len(dones), len(todos)))
    for done in dones:
        print('\t {}'.format(done))
