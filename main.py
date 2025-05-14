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
        print("")

    if command == "add":
        content = input("Enter task content: ")
        task.task(content)

    elif command == "update":
        pass
    elif command == "delete":
        pass
    elif command == "mark-in-progress":
        pass
    elif command == "mark-done":
        pass
    elif command == "list":
        pass

if __name__ == "__main__":
    welcome()
