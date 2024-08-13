#!/usr/bin/python3
"""
A Script that, uses a REST API, for a given employee ID, returns
information about his/her TODO list progress
exporting data in the CSV format.
"""
import csv
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

    lines = []
    for todo in todos:
        lines.append([user.get('id'), user.get('username'),
                     todo.get('completed'), todo.get('title')])

    with open('{}.csv'.format(user['id']), 'w') as f:
        csv_writer = csv.writer(f, delimiter=',')

        for line in lines:
            csv_writer.writerow(line)
