import datetime
from storage import get_db_connection

time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")


def add_cmd(description):
    if not description or description.isspace():
        print("Your task cannot be empty")
        exit()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (desc) VALUES (?)", (description,))
    conn.commit()
    conn.close()
    print(f"task added {description}")


def list_all_tasks():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    for task in tasks:
        print(
            f"ID: {task['id']} TASK: {task['desc']} STATUS: {task['status']} CREATEDAT: {task['createdAt']} UPDATEDAT: {task['updatedAt']}"
        )


def update_cmd(desc, id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET desc = ? WHERE id = ?", (desc, id))
    if cursor.rowcount == 0:
        print("error: invalid id or description identical")
        exit()
    conn.commit()
    conn.close()


def delete_cmd(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("")
    conn.commit()


# def delete_cmd(id):
#     tasks = load_task()
#     new_task = []
#     found_id = False
#     for task in tasks:
#         if id == task["id"]:
#             found_id = True
#             print("deleted task")
#         if task["id"] != id:
#             new_task.append(task)
#
#     if found_id == False:
#         print("invalid id")
#     save_task(new_task)
#
#
# def mark_cmd(id, status):
#     tasks = load_task()
#     found_id = False
#     for task in tasks:
#         if task["id"] == id:
#             found_id = True
#             if status == "done":
#                 print("marked task as done")
#                 task["status"] = "done"
#                 task["updatedAt"] = time
#             elif status == "todo":
#                 print("marked task as todo")
#                 task["status"] = "todo"
#                 task["updatedAt"] = time
#             elif status == "in-progress":
#                 print("marked task as in progress")
#                 task["status"] = "in-progress"
#                 task["updatedAt"] = time
#             else:
#                 print("invalid status")
#     if found_id == False:
#         print("invalid id")
#     save_task(tasks)
#
#
# def list_cmd(arg):
#     tasks = load_task()
#     for task in tasks:
#         if arg is None:
#             print(
#                 f"ID: {task['id']} Task: {task['description']} Created: {task['createdAt']} Last Updated: {task['updatedAt']} "
#             )
#         if arg == "done" and task.get("status") == "done":
#             print(
#                 f"ID: {task['id']} Task: {task['description']} Created: {task['createdAt']} Last Updated: {task['updatedAt']} Status: {task['status']}"
#             )
#         if arg == "todo" and task.get("status") == "todo":
#             print(
#                 f"ID: {task['id']} Task: {task['description']} Created: {task['createdAt']} Last Updated: {task['updatedAt']} Status: {task['status']}"
#             )
#         if arg == "in-progress" and task.get("status") == "in-progress":
#             print(
#                 f"ID: {task['id']} Task: {task['description']} Created: {task['createdAt']} Last Updated: {task['updatedAt']} Status: {task['status']}"
#             )
