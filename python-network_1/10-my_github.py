#!/usr/bin/python3
"""
Takes GitHub credentials (username and personal access token)
and uses the GitHub API to display the user id.
"""
import requests
import sys
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/user"

    # Basic Authentication tələbi üçün auth parametrindən istifadə edirik
    r = requests.get(url, auth=HTTPBasicAuth(username, password))
    
    try:
        # JSON cavabını lüğətə çevirib 'id' açarını götürürük
        print(r.json().get('id'))
    except ValueError:
        print("None")
