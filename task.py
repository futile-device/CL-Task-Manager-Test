###################################
# Task Utility
#
# Accepts command line arguments:
# Commands: add, list, delete
# Task -> multi word description
# Due Date ->  in DD/MM/YYYY format
# Generate a unique ID
# Store in JSON file
#
#####################################

# import our libs
import json_utils
import commands as cmd

# import external libs
import argparse
import datetime


##############################
##
##  Parse Arguments
##
##############################

# TODO: I know there is a more elegant way to handle this
# what I'd like is --add "My Task" 10/12/2003 where 
# the --add is a cmd, and argpars forces nargs2 with typing
# but his was taking me too long to crack :(

parser = argparse.ArgumentParser(description='Task Manager')
parser.add_argument('--add', type=str, nargs=2, help='Add task with description and due date DD-MM-YYYY')
parser.add_argument('--done', type=int, help='Mark task ID as complete')
# parser.add_argument('--cmd', type=str, action = 'store', dest = 'cmd', help = 'Task manager command')
# parser.add_argument('--task', type=str, action = 'store', dest = 'task', help = 'Task description')
# # parser.add_argument('--date', type=str, action = 'store', dest = 'date', help = 'Task due date DD-MM-YYYY')
# parser.add_argument('--date', type=lambda s: datetime.datetime.strptime(s, '%d-%m-%Y'),  help='Task due date DD-MM-YYYY')

# Parse the arguments
args = parser.parse_args()

##############################
##
##  Handle Arguments
##
##############################

# Check commands

if args.add == None and args.done == None:
    print("List command")
    all_tasks = cmd.list('tasks.json')
    quit()

if args.add == None and args.done != None:
    print("Done command")
    quit()
    
if args.add != None and args.done == None:
    print("Add command")
    cmd.add('tasks.json', args.add[0], args.add[1])
    quit()

##############################
##
##  Handle Errors/Args
##
##############################

# descr errs: absence of quotes, no task desrc
# date errs: no date, wrong date format

if args.date == None:
    print("Please provide a task descriptio and due date!")
    parser.print_help()
    quit()




##############################
##
##  Load Previous Tasks
##
##############################

all_tasks_data = json_utils.loadTaskFromJSON("tasks.json") # TODO: handle different file paths from cmd line
# print(all_tasks_data)


##############################
##
##  Create New Task
##
##############################

new_task_desc = args.task
new_task_date = args.date.isoformat()
new_task_id   = -1  # use later so -1 to indicate no ID yet
new_task_entry = {}
new_task_entry['description'] = new_task_desc
new_task_entry['date'] = new_task_date
new_task_entry['id'] = new_task_id 

# print(new_task_entry)

# TODO: handle multiple entries, either same descr or same date?
# TODO: Handle sane dates: is it in the future? in the year 2300 etc
# TODO: Handle ID with startegy eg., sort by date, hash unique etc
# here's where I would start by iterating through current entries etc

number_tasks = len(all_tasks_data)

# ID Strategy: ever increasing sequence ie.,
# since tasks may get deleted, we can 
# assume that max(id0....idN) + 1 will unique

max_id = 0
for idx, entry in zip(range(number_tasks), all_tasks_data):
    max_id = max(idx, max_id)

new_task_id = max_id + 1
new_task_entry['id'] = new_task_id 

print("Adding new task")
print(f"Task: {new_task_desc}")
print(f"Date: {new_task_date}")
print(f"IDv : {new_task_id}")

all_tasks_data.append(new_task_entry)


# show me debug

# for entry in all_tasks_data:
#     print(entry)




##############################
##
##  Save Tasks
##
##############################

json_utils.saveTasksToJSON('tasks.json', all_tasks_data)
    

# no oargs just list only not done by date and id
# done command marked done