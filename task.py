####################################
## TASK MaNaGER
#####################################

# import our libs
import json_utils
import commands as cmd

# import external libs
import argparse
from datetime import datetime

# running task.py with no args   ==> list all tasks yet to be done
# --add "My Task" 12/12/2025     ==> adds a new task
# --done 2                       ==> marks ID 2 done

parser = argparse.ArgumentParser(description='Task Manager')
parser.add_argument('--add', type=str, nargs=2, help='Add task with description and due date DD-MM-YYYY')
parser.add_argument('--done', type=int, help='Mark task ID as complete')
# parser.add_argument('--all', type=bool, help='List all tasks') # maybe next add way to list all or only done


args = parser.parse_args()

# LIST
if args.add == None and args.done == None:
    # print("List command")
    all_tasks = cmd.list('tasks.json', False) # True list todo/False list
    quit()

# DONE
if args.add == None and args.done != None:
    # print("Done command")
    cmd.done('tasks.json', args.done)
    quit()

# ADD
if args.add != None and args.done == None:
    # print("Add command")
    # check if date is right format ab/using try/catch
    try:
        date_object = datetime.strptime(args.add[1], '%d-%m-%Y') 
    except:
        print("Date needs to be in DD-MM-YYYY format")
        quit()
    
    cmd.add('tasks.json', args.add[0], args.add[1])
    quit()

