#!/usr/bin/python3
"""Exports data in the JSON format"""
import json
import requests
import sys

if __name__ == "__main__":
    id = sys.argv[1]
    userUrl = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    todoUrl = "https://jsonplaceholder.typicode.com/users/{}/todos".format(id)

    userData = requests.get(userUrl).json()
    todo = requests.get(todoUrl).json()

    with open('{}.json'.format(id), 'w') as json_file:
        tasks = []
        for t in todo:
            tasks.append({"task": t.get("title"),
                          "completed": t.get("completed"),
                          "username": userData.get("username")})
        data = {"{}".format(id): tasks}
        json.dump(data, json_file)
