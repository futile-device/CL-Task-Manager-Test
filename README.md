# CL-Task-Manager-Test

## Commands

python task.py					lists all tasks that need doing
python task.py --all				lists all tasks including those done
python task.py --add "Description" 01-01-2026	adds a task with description and date
python task.py --done X				marks a task with assigned ID == X as being done

## Next Steps
- current pretty listing crops task description to 15 chars
- delete a task
- modify a task
- renumber IDs

## Issues
- currently always reloads JSON database and iterates every task, this will be inefficient as task list grows longer

