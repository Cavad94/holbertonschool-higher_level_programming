#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL and displays the value
of the X-Request-Id variable found in the response header.
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)
    # headers bir lüğət (dict) kimidir, get metodu ilə dəyəri götürürük
    print(r.headers.get('X-Request-Id'))
