import json


def task(content):
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
            if not isinstance(tasks, list):
                tasks = []
    except (FileNotFoundError, json.JSONDecodeError):
        tasks = []
    
    new_task = {
        "id": len(tasks) + 1,
        "task": content
    }
    tasks.append(new_task)
    
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)
    
    print(f"Task '{content}' added successfully ID ({new_task['id']})")