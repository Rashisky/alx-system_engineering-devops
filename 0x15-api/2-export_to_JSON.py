#!/usr/bin/python3
"""EXPORT TO JSON"""
import json
import requests
from sys import argv

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    user_name = requests.get(url + f'users/{argv[1]}').json().get('username')
    todos = requests.get(url + f'todos?userId={argv[1]}').json()

    data = [
        {"task": f'{r.get("title")}',
         "completed": eval(f'{r.get("completed")}'),
         "username": user_name
         } for r in todos
         ]

    json_data = {argv[1]: [items for items in data]}
    with open(f'{argv[1]}.json', 'w', encoding='utf-8') as file:
        json.dump(json_data, file)
