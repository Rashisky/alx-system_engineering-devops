#!/usr/bin/python3
"""Gather data from an API"""

from sys import argv
import requests

url = 'https://jsonplaceholder.typicode.com/'
users = requests.get(url + f'users/{argv[1]}').json()
todos = requests.get(url + f'todos?userId={argv[1]}').json()

task_completed = [task['title'] for task in todos if task['completed']]

print(f"Employee {users['name']} is done with tasks\
      ({len(task_completed)}/{len(todos)}):")
[print(f'\t {task}') for task in task_completed]
