#!/usr/bin/python3
"""Gather data from an API"""

if __name__ == '__main__':
    import requests
    import sys

    url = 'https://jsonplaceholder.typicode.com/'
    users = requests.get(url + f'users/{sys.argv[1]}').json()
    todos = requests.get(url + f'todos?userId={sys.argv[1]}').json()

    task_completed = [task.get('title', '') for task in todos
                      if task.get('completed', '')]

    print(f"Employee {users.get('name', '')} is done with tasks\
({len(task_completed)}/{len(todos)}):")
    [print(f'\t {task}') for task in task_completed]
