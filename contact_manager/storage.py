import json
import os

FILE_NAME = "contacts.json"

def load_contacts():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def save_contacts(contacts):
    with open(FILE_NAME, 'w') as file:
        json.dump(contacts, file, indent=4)
