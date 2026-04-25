#!/usr/bin/python3
import os

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: Invalid input type for template. Expected string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: Invalid input type for attendees. Expected list of dictionaries.")
        return
    if not template:
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return
    for index, attendee in enumerate(attendees, start=1):
        processed_template = template
        keys = ["name", "event_title", "event_date", "event_location"]
        for key in keys:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            target = "{" + key + "}"
            processed_template = processed_template.replace(target, str(value))
        filename = "output_{}.txt".format(index)
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(processed_template)
        except Exception as e:
            print("Error writing to file {}: {}".format(filename, e))
