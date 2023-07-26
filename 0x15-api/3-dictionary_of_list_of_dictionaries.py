#!/usr/bin/python3
"""Dictionary of list of dictionaries"""
import json
import requests

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    users = requests.get(url + 'users').json()
    todos = requests.get(url + 'todos').json()

    data = {}

    for task in todos:
        if task['userId'] in data.keys():
            for user_name in users:
                if (user_name['id'] == task['userId']):
                    user = user_name['username']
            values = {
                "username": user,
                "task": task['title'],
                "completed": task['completed']
            }
            data[task['userId']].append(values)
        else:
            for user_name in users:
                if (user_name['id'] == task['userId']):
                    user = user_name['username']
            values = {
                "username": user,
                "task": task['title'],
                "completed": task['completed']
            }
            data[task['userId']] = [values]

    with open('todo_all_employees.json', 'w') as file:
        json.dump(data, file)
