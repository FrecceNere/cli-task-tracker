# command imports
from commands import task

def welcome():
    print("Welcome to the command line Task Tracker!")
    print("help - to see the list of commands")
    print("")
    input_command()

def input_command():
    while True:
        command = input("task-cli.py >" + " ")
        command_handler(command)

def command_handler(command):
    if command == "help":
        print("")
        print("Available commands:")
        print("add - to add a new task")
        print("update - to update an existing task")
        print("delete - to delete an existing task")
        print("")

    if command == "add":
        content = input("Enter task content: ")
        task.add(content)

    elif command == "update":
        task_id = input("Enter task ID to update: ")
        content = input("Enter new task content: ")
        task.update(task_id, content)
    elif command == "delete":
        task_id = input("Enter task ID to delete: ")
        task.delete(task_id)
    elif command == "mark-in-progress":
        task_id = print("Enter task ID to mark in progress: ")
        task.mark_in_progress(task_id)
    elif command == "mark-done":
        pass
    elif command == "list":
        pass

if __name__ == "__main__":
    welcome()
