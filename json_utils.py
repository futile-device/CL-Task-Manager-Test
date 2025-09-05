
# JSON storage utilities for task manager

import os
import json

# checks and loads tasks from JSOM
def saveTasksToJSON(file_path, tasks):
    # Write updated data back to file
    with open(file_path, 'w') as f:
        json.dump(tasks, f, indent=3)

# checks and loads tasks from JSOM
def loadTaskFromJSON(file_path):
    
    # first check if json file exists and if so load it

    all_tasks_data = []

    if not os.path.exists(file_path):
        # File does not exist, will be created when adding new task
        print(f"JSON tasks file does not exist: '{file_path}'")
    else:
        try:
            with open(file_path, 'r') as f:
                all_tasks_data = json.load(f)
                print("Tasks loaded succesfully...")

        except json.JSONDecodeError:
            print(f"Error decoding JSON from '{file_path}'. File might be empty or corrupted.")
            # need to handle here for when the json is corrupt! For now quit

    return all_tasks_data