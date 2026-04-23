#!/bin/bash
# Sends a POST request to a URL with email and subject variables, and displays the body
curl -s -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
