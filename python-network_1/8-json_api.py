#!/usr/bin/python3
"""
Takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter 'q'.
"""
import requests
import sys


if __name__ == "__main__":
    # Əgər arqument verilməyibsə, q-nü boş string edirik
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]

    url = "http://0.0.0.0:5000/search_user"
    payload = {'q': q}

    try:
        r = requests.post(url, data=payload)
        # JSON-u təhlil etməyə çalışırıq
        json_content = r.json()

        if not json_content:
            print("No result")
        else:
            print("[{}] {}".format(json_content.get('id'), json_content.get('name')))

    except ValueError:
        # Əgər r.json() uğursuz olarsa (JSON formatı səhvdirsə)
        print("Not a valid JSON")
