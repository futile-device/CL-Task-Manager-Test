####################################
## TASK MANAGER
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
group = parser.add_mutually_exclusive_group()
group.add_argument('--add', type=str, nargs=2, help='Add task with description and due date DD-MM-YYYY')
group.add_argument('--done', type=int, help='Mark task ID as complete')
# parser.add_argument('--all', type=bool, help='List all tasks') # maybe next add way to list all or only done


args = parser.parse_args()


if args.add:
    
    # print("Add command")
    
    # check: a) is date in correct format
    # and b) the task is not in the past
    
    try:

        # this will throw an error if invalid date
        task_date = datetime.strptime(args.add[1], '%d-%m-%Y') 

        # for now only comparing date, not hour
        if task_date.date() >= datetime.today().date(): 
            cmd.add('tasks.json', args.add[0], args.add[1])
        else:
            print("Task date needs to be today or in the future")  
                
    except:
        print("Invalid date, make sure it's in DD-MM-YYYY format")

    quit()

# DONE
elif args.done:
    # print("Done command")
    cmd.done('tasks.json', args.done)
    quit()


else:
    # print("List command")
    all_tasks = cmd.list('tasks.json', False) # True list todo/False list
    quit()


