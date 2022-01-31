#!/usr/bin/python3
""" fetches users with respective todos
    @param:
       employeeID: int , represents the user id
"""

import requests
import sys

base_url = "https://jsonplaceholder.typicode.com"
todos = requests.get(base_url + "/users/{}/todos".format(sys.argv[1])).json()
done = {}

for todo in todos:
    done.setdefault(todo["userId"], [])
    if todo["completed"]:
        done[todo["userId"]].append(todo["title"])

for id, completed in done.items():
    username = requests.get(base_url + "/users/{}".format(id)).json()["name"]
    print("Employee {} is done with tasks({}/20):"
          .format(username, len(completed)))
    for c in completed:
        print("    {}".format(c))
