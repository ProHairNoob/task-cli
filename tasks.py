import click
import sqlite3
from storage import get_db_connection


@click.command(name="add", help="add a new task")
@click.argument("desc", type=str, metavar="description")
def add_cmd(desc):
    if not desc or desc.isspace():
        print("error: your task cannot be empty")
        raise SystemExit(1)
    desc = desc.strip()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (desc) VALUES (?)", (desc,))
    conn.commit()
    conn.close()
    print(f"task added {desc}")


@click.command(name="list", help="view your tasks in a list")
def list_all_tasks():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    if len(tasks) == 0:
        print("No tasks available bird chirp ...")
        raise SystemExit(1)
    for task in tasks:
        print(
            f"ID: {task['id']} TASK: {task['desc']} STATUS: {task['status']} CREATEDAT: {task['createdAt']} UPDATEDAT: {task['updatedAt']}"
        )


@click.command(name="update", help="change a tasks description")
@click.argument("id", type=int, metavar="id")
@click.argument("desc", type=str, metavar="description")
def update_cmd(desc, id):
    if not desc or desc.isspace():
        print("error: your task cannot be empty")
        raise SystemExit(1)
    desc = desc.strip()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE tasks SET desc = ?, updatedAt = CURRENT_TIMESTAMP WHERE id = ?",
        (desc, id),
    )
    if cursor.rowcount == 0:
        print("error: invalid id")
        raise SystemExit(1)

    print(f"task updated to: {desc}")
    conn.commit()
    conn.close()


@click.command(name="delete", help="delete a task")
@click.argument("id", type=int, metavar="id")
def delete_cmd(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT desc FROM tasks WHERE id = ?", (id,))
    desc = cursor.fetchone()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (id,))
    if cursor.rowcount == 0:
        print("error: invalid id")
        raise SystemExit(1)
    print(f"task deleted: {desc['desc']}")
    conn.commit()
    conn.close()


@click.command(name="mark", help="mark a task as one of: todo, in-progress, done")
@click.argument("id", type=int, metavar="id")
@click.argument("status", type=str, metavar="status")
def mark_cmd(status, id):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "UPDATE tasks set status = ?,updatedAt = CURRENT_TIMESTAMP WHERE id = ?",
            (status, id),
        )
        conn.commit()
    except sqlite3.IntegrityError as error:
        if "CHECK constraint failed" in str(error):
            print("error: please choose one of todo in-progress done")
            raise SystemExit(1)
    else:
        if cursor.rowcount == 0:
            print("error: invalid id")
            raise SystemExit(1)
        else:
            print(f"marked task as: {status}")

    conn.close()
