
from storage import save_task , load_task

def add_cmd(description):
    tasks = load_task()
    
    new_task = {
            "id":len(tasks) + 1,
            "description": description,
            "status": "todo"

    }
    tasks.append(new_task)
    save_task(tasks)

def list_cmd():
    tasks = load_task()
    for task in tasks:
        print(f"Task{task["id"]} {task["description"]}")

