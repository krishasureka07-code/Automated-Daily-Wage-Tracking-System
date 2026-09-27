"""
storage.py
Handles persistent JSON file operations with absolute path resolution.
"""
import json
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
WORKERS_FILE = os.path.join(DATA_DIR, "workers.json")
SHIFTS_FILE = os.path.join(DATA_DIR, "shifts.json")
WORKER_HISTORY_FILE = os.path.join(DATA_DIR, "worker_history.json")
def ensure_storage_ready():
    """Creates the data directory if it does not exist."""
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR, exist_ok=True)
def load_data(file_path):
    """
    Safely reads records from a JSON file.
    Returns an empty list if the file is missing or corrupted.
    """
    ensure_storage_ready()
    if not os.path.exists(file_path):
        return []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError):
        return []
def save_data(file_path, data):
    """Persists an in-memory data list into the designated JSON file."""
    ensure_storage_ready()
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)