import argparse
from tasks import add_cmd  # list_cmd, mark_cmd, update_cmd, delete_cmd

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
list_cli.add_argument(
    "status", nargs="?", help="filters your tasks by status: todo, in-progress, done"
)

args = parser.parse_args()

if args.command == "add":
    add_cmd(args.description)

if args.command == "list":
    list_cmd(args.status)

if args.command == "mark":
    mark_cmd(args.id, args.status)

if args.command == "update":
    update_cmd(args.id, args.description)

if args.command == "delete":
    delete_cmd(args.id)
# debug
# print(args,type(args)) #
#
