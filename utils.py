import json


# Function to read data from a JSON file
def load_data(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


# Function to save data to a JSON file
def save_data(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)


# Helper functions
def get_next_id(items):
    return max(item['id'] for item in items) + 1 if items else 1


def find_item_by_id(items, item_id):
    return next((item for item in items if item['id'] == item_id), None)


def save_and_respond(save_file, items, item, status_code=200, headers=None):
    save_data(save_file, items)
    return item, status_code, headers
