import datetime
from storage import save_task , load_task

time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

def add_cmd(description):
    if description == "" or description.isspace():
         print("Your task cannot be empty")
         exit()
    tasks = load_task()
    ids = [task["id"] for task in tasks]
    if ids == []:
        ids.append(0)
    new_task = {
            "id":max(ids) + 1,
            "description": description,
            "status": "todo",
            "updatedAt": time,
            "createdAt": time
    }
    tasks.append(new_task)
    save_task(tasks)

def update_cmd(id,text):
    tasks = load_task()
    found_id = False
    for task in tasks:
        if task["id"] == id: 
            task["description"] = text
            task["updatedAt"] = time
            found_id = True
    if found_id == False:
        print("invalid id")
    save_task(tasks)

def delete_cmd(id):
    tasks = load_task()
    new_task = []
    found_id = False
    for task in tasks:
        if id == task["id"]:
            found_id = True
            print("deleted task")
        if task["id"] != id:
            new_task.append(task)            
            
                
    if found_id == False:
        print("invalid id")

    save_task(new_task)
            

def mark_cmd(id,status):
    tasks = load_task()
    found_id = False
    for task in tasks:
        if task["id"] == id:
            found_id = True
            if status == "done":
                print("marked task as done")
                task["status"] = "done"
                task["updatedAt"] = time
            elif status == "todo": 
                print("marked task as todo")
                task["status"] = "todo"
                task["updatedAt"] = time
            elif status == "in-progress":
                print("marked task as in progress")
                task["status"] = "in-progress"           
                task["updatedAt"] = time   
            else:
                print("invalid status")
    if found_id == False:
        print("invalid id")
    save_task(tasks)
    

def list_cmd(arg):
    tasks = load_task()
    for task in tasks:
        if arg is None:
            print(f"ID: {task["id"]} Task: {task["description"]} Created: {task["createdAt"]} Last Updated: {task["updatedAt"]} ")
        if arg == "done" and task.get("status") == "done":
            print(f"ID: {task["id"]} Task: {task["description"]} Created: {task["createdAt"]} Last Updated: {task["updatedAt"]} Status: {task["status"]}")
        if arg == "todo" and task.get("status") == "todo":
            print(f"ID: {task["id"]} Task: {task["description"]} Created: {task["createdAt"]} Last Updated: {task["updatedAt"]} Status: {task["status"]}")
        if arg == "in-progress" and task.get("status") == "in-progress":
            print(f"ID: {task["id"]} Task: {task["description"]} Created: {task["createdAt"]} Last Updated: {task["updatedAt"]} Status: {task["status"]}")
