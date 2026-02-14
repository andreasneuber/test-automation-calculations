# persistence.py
"""
File-based persistence for user input values
"""

import json
import os

# File to store user inputs
DATA_FILE = 'user_inputs.json'


def load_data():
    """
    Load user input data from JSON file.
    
    Returns:
        dict: Dictionary with all saved input values, or empty dict if file doesn't exist
    """
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            # If file is corrupted or can't be read, return empty dict
            return {}
    return {}


def save_data(data):
    """
    Save user input data to JSON file.
    
    Args:
        data (dict): Dictionary containing all input values to save
    """
    try:
        with open(DATA_FILE, 'w') as f:
            json.dump(data, f, indent=2)
    except IOError:
        # Silently fail if we can't write the file
        pass


def update_value(key, value):
    """
    Update a single value in the persistent storage.
    
    Args:
        key (str): The key to update
        value: The value to store
    """
    data = load_data()
    data[key] = value
    save_data(data)


def get_value(key, default=0):
    """
    Get a single value from persistent storage.
    
    Args:
        key (str): The key to retrieve
        default: Default value if key doesn't exist
        
    Returns:
        The stored value or default
    """
    data = load_data()
    return data.get(key, default)


def clear_all_data():
    """
    Clear all saved data by deleting the file.
    """
    if os.path.exists(DATA_FILE):
        try:
            os.remove(DATA_FILE)
        except IOError:
            pass
