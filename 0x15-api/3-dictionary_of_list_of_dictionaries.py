#!/usr/bin/python3
""" Program that Gather data from an API and Export to JSON
 all tasks from all employees"""
import json
import requests

if __name__ == "__main__":
    """ Program Entry point """
    employeeId = 1
    todoUrl = 'https://jsonplaceholder.typicode.com/todos'
    userUrl = 'https://jsonplaceholder.typicode.com/users'

    allUsers = requests.get(userUrl).json()

    userTasks = {}

    for employeeId in range(1, len(allUsers) + 1):
        todoRequest = requests.get(todoUrl, params={'userId': employeeId})
        userRequest = requests.get(userUrl, params={'id': employeeId})

        totalTasks = todoRequest.json()
        user_data = userRequest.json()
        dictList = []
        employeeName = user_data[0].get('username')

        for task in totalTasks:
            taskData = {}
            taskData['task'] = task.get('title')
            taskData['completed'] = task.get('completed')
            taskData['username'] = employeeName
            dictList.append(taskData)
        userTasks[employeeId] = dictList

    with open('todo_all_employees.json', 'w') as json_file:
        data = json.dumps(userTasks)
        json_file.write(data)
