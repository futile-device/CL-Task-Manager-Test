
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
    
    # first check if file exists and if not make a new one

    if not os.path.exists(file_path):
        # File does not exist, create it with an empty JSON object
        with open(file_path, 'w') as json_tasks:
            json.dump({}, json_tasks)
        print(f"'{file_path}' created tasks.json as it did not exist.")
    else:
        # print(f"'{file_path}' already exists.")
        pass
        
    # now load the tasks checking for JSON errors

    all_tasks_data = []

    try:
        with open(file_path, 'r') as f:
            all_tasks_data = json.load(f)
        print("Tasks loaded succesfully...")
        # print("Content of the JSON file:", all_tasks_data)
    except json.JSONDecodeError:
        print(f"Error decoding JSON from '{file_path}'. File might be empty or corrupted.")
        # need to handle here for when the json is corrupt!
        all_tasks_data = []
        
        
        
        
    # check if any data exists - if not this is our first task

    if not all_tasks_data:
        print("No tasks: initialising data storage")
        all_tasks_data = [] # assign empty data
    else:
        # print("Tasks already exist")
        # print(all_tasks_data)
        pass

    return all_tasks_data