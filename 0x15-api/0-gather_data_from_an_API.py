#!/usr/bin/python3
""" Gather data from an API  """

if __name__ == "__main__":
    from requests import get
    from sys import argv, exit

    try:
        id = argv[1]
        isInt = int(id)
    except Exception:
        exit()

    userUrl = "https://jsonplaceholder.typicode.com/users?id=" + id
    todoUrl = "https://jsonplaceholder.typicode.com/todos?userId=" + id

    rUser = get(userUrl)
    rTodo = get(todoUrl)

    try:
        jsonUser = rUser.json()
        jsonTodo = rTodo.json()

    except ValueError:
        print("Not a valid JSON")

    if jsonUser and jsonTodo:
        EMPLOYEE_NAME = jsonUser[0].get('name')
        TOTAL_NUMBER_OF_TASKS = len(jsonTodo)
        NUMBER_OF_DONE_TASKS = sum(item.get("completed")
                                   for item in jsonTodo if item)

        print("Employee {} is done with tasks({}/{}):"
              .format(EMPLOYEE_NAME,
                      NUMBER_OF_DONE_TASKS,
                      TOTAL_NUMBER_OF_TASKS))
        for todo in jsonTodo:
            TASK_TITLE = todo.get('title')
            if todo.get("completed"):
                print("\t {}".format(TASK_TITLE))
