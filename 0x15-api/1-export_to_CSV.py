#!/usr/bin/python3
"""Program that Gather data from an API and export it to CSV"""
import csv
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

    with open('{}.csv'.format(employeeId), mode='w') as employee_file:
        employeeWriter = csv.writer(employee_file, delimiter=',',
                                    quotechar='"', quoting=csv.QUOTE_ALL)
        for task in totalTasks:
            employeeWriter.writerow(["{}".format(employeeId), "{}".
                                    format(employeeName), "{}".
                                    format(task.get('completed')),
                                    "{}".format(task.get('title'))])
