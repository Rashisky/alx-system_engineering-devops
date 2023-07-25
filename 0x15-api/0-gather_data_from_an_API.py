#!/usr/bin/python3
"""Gather data from an API"""
import requests
import sys

if __name__ == '__main__':
    # url = 'https://jsonplaceholder.typicode.com/'
    # users = requests.get(url + f'users/{sys.argv[1]}').json()
    # todos = requests.get(url + f'todos?userId={sys.argv[1]}').json()

    # task_completed = [task.get('title') for task in todos
    #                   if task.get('completed') is True]
    # print("Employee {} is done with tasks({}/{}):"
    #       .format(users.get('name'), len(task_completed), len(todos)))
    # [print(f'\t {task}') for task in task_completed]

    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    completed = [t.get("title") for t in todos if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))
    [print("\t {}".format(c)) for c in completed]
