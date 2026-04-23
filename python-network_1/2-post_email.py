#!/usr/bin/python3
"""
Takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays the body of the response.
"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    values = {'email': email}
    
    # Məlumatı URL-encoded formatına salırıq (məs: email=test%40gmail.com)
    data = urllib.parse.urlencode(values)
    # Məlumatı bayt formatına çeviririk (POST üçün mütləqdir)
    data = data.encode('ascii')
    
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
