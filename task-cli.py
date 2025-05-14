# library imports
import json
from commands import add

while True:
    def welcome():
        print("Welcome to the command line Task Tracker!")
        print("help - to see the list of commands")
        print("")
        input_command()

    def input_command():
        command = input("task-cli.py >" + " ")
        command_handler(command)

    def command_handler(command):
        if command == "help":
            print("")
            print("Available commands:")
            print("add - to add a new task")

    welcome()       
