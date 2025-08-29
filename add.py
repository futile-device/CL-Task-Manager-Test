import json_utils

# add a new task to JSON db
def toJSON(file_path, task_desc, task_date):
    
    all_tasks = json_utils.loadTaskFromJSON(file_path)
    
    # ID Strategy: ever increasing sequence ie.,
    # assume that max(id0....idN) + 1 will unique

    task_id = 0
    for idx, entry in zip(range(len(all_tasks)), all_tasks):
        max_id = max(idx, task_id)
    
    new_task_entry = {}
    new_task_entry['description'] = task_desc
    new_task_entry['date'] = task_date
    new_task_entry['done'] = False
    new_task_entry['id'] = task_id 
    
    all_tasks.append(new_task_entry)
    
    json_utils.saveTasksToJSON('tasks.json', all_tasks)
    
    return new_task_entry
    