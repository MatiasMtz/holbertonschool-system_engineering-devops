#!/usr/bin/python3
""" Program that Gather data from an API and Export to JSON """
import json
from typing import List
import requests
from sys import argv

if __name__ == "__main__":
    """ Program Entry point """
    employeeId = argv[1]
    todoUrl = 'https://jsonplaceholder.typicode.com/todos'
    userUrl = 'https://jsonplaceholder.typicode.com/users'
    payload1 = {'userId': employeeId}
    payload2 = {'id': employeeId}

    todoRequest = requests.get(todoUrl, params=payload1)
    userRequest = requests.get(userUrl, params=payload2)

    totalTasks = todoRequest.json()
    userData = userRequest.json()
    employeeName = userData[0].get('username')
    dictList = []
    userTasks = {}

    with open('{}.json'.format(employeeId), 'w') as json_file:
        for task in totalTasks:
            taskData = {}
            taskData['task'] = task.get('title')
            taskData['completed'] = task.get('completed')
            taskData['username'] = employeeName
            dictList.append(taskData)
        userTasks[employeeId] = dictList
        info = json.dumps(userTasks)
        json_file.write(info)
