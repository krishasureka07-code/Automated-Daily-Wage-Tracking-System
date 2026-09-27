"""
worker_manager.py
Handles worker registration, input validation, and skill categorization.
"""
from storage import WORKERS_FILE, WORKER_HISTORY_FILE, load_data, save_data
def generate_worker_id(workers):
    """Generates an incremental unique identifier (e.g., W-101)."""
    if not workers:
        return "W-101"
    last_id = workers[-1]["worker_id"]
    next_num = int(last_id.split("-")[1]) + 1
    return f"W-{next_num}"
def skill_from_experience(years):
    """Classifies skill level from relevant work experience."""
    years = float(years)
    if years < 0:
        raise ValueError("Experience cannot be negative.")
    if years <= 1:
        return "Unskilled"
    if years <= 3:
        return "Semi-Skilled"
    return "Skilled"

def register_worker(name, experience_years, daily_rate):
    """
    Registers a new worker profile after validating inputs.
    Validates non-empty name and positive wage rates.
    """
    cleaned_name = name.strip()
    if not cleaned_name:
        return False, "Worker name cannot be empty."
    try:
        daily_rate_val = float(daily_rate)
    except ValueError:
        return False, "Daily rate must be a valid numerical value."
    if daily_rate_val <= 0:
        return False, "Daily base rate must be greater than zero."
    try:
        experience_val = float(experience_years)
    except (ValueError, TypeError):
        return False, "Work experience must be a valid number of years."
    if experience_val < 0:
        return False, "Work experience cannot be negative."
    formatted_skill = skill_from_experience(experience_val)

    workers = load_data(WORKERS_FILE)
    worker_id = generate_worker_id(workers)
    worker_record = {
        "worker_id": worker_id,
        "name": cleaned_name.title(),
        "experience_years": experience_val,
        "skill_level": formatted_skill,
        "daily_rate": daily_rate_val,
        "standard_hours": 8.0,
    }
    workers.append(worker_record)
    save_data(WORKERS_FILE, workers)

    history = load_data(WORKER_HISTORY_FILE)
    history.append({**worker_record, "status": "ACTIVE", "registered_on": ""})
    save_data(WORKER_HISTORY_FILE, history)
    return True, f"Worker registered successfully with ID: {worker_id}"
def unregister_worker(worker_id):
    """Unregisters a worker while keeping historical shift records intact."""
    workers = load_data(WORKERS_FILE)
    target_id = worker_id.strip().upper()
    for index, worker in enumerate(workers):
        if worker["worker_id"] == target_id:
            removed = workers.pop(index)
            save_data(WORKERS_FILE, workers)
            history = load_data(WORKER_HISTORY_FILE)
            found = False
            for record in history:
                if record.get("worker_id") == target_id:
                    record["status"] = "UNREGISTERED"
                    found = True
                    break
            if not found:
                history.append({**removed, "status": "UNREGISTERED", "registered_on": ""})
            save_data(WORKER_HISTORY_FILE, history)
            return True, f"Worker {removed['name']} ({target_id}) has been unregistered. Historical shift records were kept."
    return False, "Worker ID not found."

def find_worker(worker_id):
    """Searches and returns a worker record by worker_id."""
    workers = load_data(WORKERS_FILE)
    target_id = worker_id.strip().upper()
    for worker in workers:
        if worker["worker_id"] == target_id:
            return worker
    return None
def get_all_skills():
    """Uses a Python Set to extract unique registered skills."""
    workers = load_data(WORKERS_FILE)
    return sorted(list({w["skill_level"] for w in workers}))