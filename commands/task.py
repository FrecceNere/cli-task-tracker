import json


def add(content):
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
            if not isinstance(tasks, list):
                tasks = []
    except (FileNotFoundError, json.JSONDecodeError):
        tasks = []
    
    new_task = {
        "id": len(tasks) + 1,
        "task": content,
        "status": status
    }
    tasks.append(new_task)
    
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)
    
    print(f"Task '{content}' added successfully ID ({new_task['id']})")

def update(task_id, content):
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No tasks found.")
        return
    
    for task in tasks:
        if task["id"] == int(task_id):
            task["task"] = content
            break
    else:
        print(f"Task with ID {task_id} not found.")
        return
    
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)
    
    print(f"Task ID ({task_id}) updated successfully to '{content}'")


def delete(task_id):
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No tasks found.")
        return
    
    initial_length = len(tasks)
    tasks = [task for task in tasks if task["id"] != int(task_id)]
    
    if len(tasks) == initial_length:
        print(f"Task with ID {task_id} not found.")
        return
    
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)
    
    print(f"Task ID {task_id} deleted successfully.")

def mark_in_progress(task_id):
    pass