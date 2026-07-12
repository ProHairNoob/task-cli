
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

def mark_cmd(id,status):
    tasks = load_task()
    id_check = False
    for task in tasks:
        if task["id"] == id:
            id_check = True
            if status == "done":
                print("marked task as done")
                task["status"] = "done"
            elif status == "todo": 
                print("marked task as todo")
                task["status"] = "todo"
            elif status == "in-progress":
                print("marked task as in progress")
                task["status"] = "in-progress"           
            else:
                print("invalid status")
    if id_check == False:
        print("invalid id")
    save_task(tasks)
    

def list_cmd(arg):
    tasks = load_task()
    for task in tasks:
        if arg is None:
            print(f"Task: {task["id"]} {task["description"]}")
        if arg == "done" and task.get("status") == "done":
            print(f"Task: {task["id"]} {task["description"]} {task["status"]}")
        if arg == "todo" and task.get("status") == "todo":
            print(f"Task: {task["id"]} {task["description"]} {task["status"]}")
        if arg == "in-progress" and task.get("status") == "in-progress":
            print(f"Task: {task["id"]} {task["description"]} {task["status"]}")
