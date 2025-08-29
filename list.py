# list all tasks in a given JSON file

import json_utils

def fromJSON(file_path):
    all_tasks = json_utils.loadTaskFromJSON(file_path)
    if all_tasks == []:
        print("No tasks yet!!")
        return False
    for idx, entry in zip(range(len(all_tasks)), all_tasks):
        print(f"Task: {entry['Description']}")
        print(f"Date: {entry['Date']}")
        print(f"IDv : {entry['ID']}")
    
    