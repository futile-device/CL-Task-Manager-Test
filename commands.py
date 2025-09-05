import json_utils
import datetime

###############################
## Util helpers
###############################

def printTaskFull(task):
    print(f"task: {task['task']}")
    print(f"date: {task['date']}")
    print(f"done: {task['done']}")
    print(f"id  : {task['id']}")

def printTaskLine(msg, task):
    print(f"{msg}{task['task']} {task['date']} {task['done']} {task['id']}")

###############################
## ADD task to file
###############################

def add(file_path, task_desc, task_date):
    
    all_tasks = json_utils.loadTaskFromJSON(file_path)
    
    # ID Strategy: ever increasing sequence ie.,
    # assume that max(id0....idN) + 1 will unique

    max_id = -1
    for idx, entry in zip(range(len(all_tasks)), all_tasks):
        max_id = max(idx, max_id)
    
    new_task_entry = {}
    new_task_entry['task'] = task_desc
    new_task_entry['date'] = task_date
    new_task_entry['done'] = False
    new_task_entry['id'] = max_id + 1
    
    all_tasks.append(new_task_entry)
    
    json_utils.saveTasksToJSON('tasks.json', all_tasks)
    
    printTaskLine("Added new task: ", new_task_entry)
    
    return new_task_entry


###############################
## LIST all tasks from file
###############################

# takes filepath and option to only
# list/return tasks that need doing
def list(file_path, list_all):
    
    temp_tasks = json_utils.loadTaskFromJSON(file_path)

    all_tasks = sorted(temp_tasks, key=lambda x: (x['date'], x['id']))
    
    if all_tasks == []:
        print("No tasks yet!! Can't list tasks")
        return None
    
    todo_tasks = []
    
    # only_list_done = True only list done/False list all
    if list_all:
        for task in all_tasks: printTaskLine("Task: ", task)
        return all_tasks
    else: # only list tasks that need doing
        for task in all_tasks:
            if task['done'] != True: 
                printTaskLine("TODO: ", task)
                todo_tasks.append(task)
        return todo_tasks

    


###############################
## DONE mark task done
###############################

def done(file_path, id_done):
    
    all_tasks = json_utils.loadTaskFromJSON(file_path)
    
    if all_tasks == []:
        print("No tasks yet!! Can't mark done...")
        return False
    
    task_done = None
    for task in all_tasks:
        # printTaskLine("check: ", task)
        if task['id'] == id_done:
            if task['done'] == True: 
                print("Task already done!")
                return False
            task['done'] = True
            task_done = task
            break
    
    if task_done != None:
        printTaskLine("Marked done: ", task_done)
        json_utils.saveTasksToJSON('tasks.json', all_tasks)
        return True
    else:
        print(f"Cannot find task ID: {id_done}")
        return False
        
