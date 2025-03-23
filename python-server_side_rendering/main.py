#!/usr/bin/env python3
"""
Main script to test the invitation generation functionality.
"""

from task_00_intro import generate_invitations

def main():
    # Read the template from a file
    try:
        with open('template.txt', 'r') as file:
            template_content = file.read()
    except FileNotFoundError:
        print("Error: template.txt not found")
        return
    except IOError as e:
        print(f"Error reading template file: {str(e)}")
        return

    # List of attendees
    attendees = [
        {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
        {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
        {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
    ]

    # Call the function with the template and attendees list
    generate_invitations(template_content, attendees)

if __name__ == "__main__":
    main() 