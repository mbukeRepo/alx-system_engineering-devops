#!/usr/bin/python3
""" fetches todos """

import requests
import sys

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"
    todos = requests.get(base_url + "/users/{}/todos"
                         .format(sys.argv[1])).json()
    username = requests.get(base_url + "/users/{}"
                            .format(sys.argv[1])).json().get("name")
    print(username)
    completed = [todo.get("title") for todo in todos if todo.get("completed")]
    print("Employee {} is done with tasks({}/{}):".format(
        username, len(completed), len(todos)))
    [print("\t {}".format(c)) for c in completed]
