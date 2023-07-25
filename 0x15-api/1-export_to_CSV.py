#!/usr/bin/python3
"""Gather data from an API"""
import csv
import requests
from sys import argv

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    user_name = requests.get(url + f'users/{argv[1]}').json().get('username')
    todos = requests.get(url + f'todos?userId={argv[1]}').json()

    task_completed = [task.get('title') for task in todos
                      if task.get('completed') is True]

    with open(f'{argv[1]}.cv', 'w', encoding='utf-8') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        [writer.writerow([argv[1], user_name, r.get('completed'),
                          r.get('title')]) for r in todos]
