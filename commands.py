import sys
import datetime
import json_utils

###############################
## Print helpers
###############################

def printTaskDetail(task):
    print(f"Task: {task['task']}")
    print(f"Date: {task['date']}")
    print(f"Done: {task['done']}")
    print(f"ID  : {task['id']}")

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
        # ...use max to always increment ID
        max_id = max(idx, max_id)
        # ...let's check for a duplicate task at the same time
        if entry['task'] == task_desc and entry['date'] == task_date:
            print("This task already exists!!")
            sys.exit()
    
    new_task_entry = {}
    new_task_entry['task'] = task_desc
    new_task_entry['date'] = task_date
    new_task_entry['done'] = False
    new_task_entry['id'] = max_id + 1
    
    all_tasks.append(new_task_entry)
    
    json_utils.saveTasksToJSON('tasks.json', all_tasks)
    
    #printTaskLine("Added new task: ", new_task_entry)
    print("Adding new task:")
    printTaskDetail(new_task_entry)
    
    return new_task_entry


###############################
## LIST all tasks from file
###############################

# takes filepath and a list_all bool 
# to switch between listing everything
# or only listing tasks that are done
def list(file_path, list_all):
    
    temp_tasks = json_utils.loadTaskFromJSON(file_path)

    if temp_tasks == []: # make sure there are even any tasks
        print("No tasks yet!! Can't list tasks")
        return None

    # here we are going to sort first by date, then 
    # by ID (which are assigned in ascending order)
    all_tasks = sorted(temp_tasks, key=lambda x: (x['date'], x['id']))

    todo_tasks = []
    
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
    
    if all_tasks == []: # make sure there are even any tasks
        print("No tasks yet!! Can't mark done...")
        return False
    
    # iterate all tasks until/if we find both
    # a matching ID and it's not already done
    
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
        
