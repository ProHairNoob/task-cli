import argparse
from tasks import (
    add_cmd,
    list_all_tasks,
    update_cmd,
    delete_cmd,
    mark_cmd,
)
from storage import make_db

# Initializing database
make_db()

# Initializing parsers
parser = argparse.ArgumentParser(prog="task-cli", description="manage your tasks")
subparsers = parser.add_subparsers(dest="command")

add = subparsers.add_parser("add", help="adds a new task")
add.add_argument("description", help="description of your task")

update = subparsers.add_parser("update", help="changes your tasks description")
update.add_argument("id", type=int, help="tasks ID")
update.add_argument("description", help="description of your task")

delete = subparsers.add_parser("delete", help="delete a task")
delete.add_argument("id", type=int, help="tasks ID")

mark = subparsers.add_parser("mark", help="change a tasks status")
mark.add_argument("id", type=int, help="tasks ID")
mark.add_argument("status", help="one of: todo, in-progress, done")

list_cli = subparsers.add_parser("list", help="shows your tasks in a list")

args = parser.parse_args()

if args.command == "add":
    add_cmd(args.description)

if args.command == "list":
    list_all_tasks()

if args.command == "mark":
    mark_cmd(args.status, args.id)

if args.command == "update":
    update_cmd(args.description, args.id)

if args.command == "delete":
    delete_cmd(args.id)
# debug
# print(args,type(args)) #
