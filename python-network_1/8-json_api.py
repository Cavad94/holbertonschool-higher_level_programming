#!/usr/bin/python3
"""
Takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter 'q'.
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]

    url = "http://0.0.0.0:5000/search_user"
    payload = {'q': q}

    try:
        r = requests.post(url, data=payload)
        json_content = r.json()

        if not json_content:
            print("No result")
        else:
            # Sətri bölərək E501 xətasının qarşısını alırıq
            print("[{}] {}".format(json_content.get('id'),
                                   json_content.get('name')))

    except ValueError:
        print("Not a valid JSON")
