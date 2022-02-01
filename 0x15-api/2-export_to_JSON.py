#!/usr/bin/python3
""" writes the result of req in json file """
import json
import requests
import sys

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    user = requests.get(base_url + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(base_url + "todos",
                         params={"userId": user_id}).json()

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: [{
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": username
        } for todo in todos]}, jsonfile)
