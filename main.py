import argparse
from tasks import add_cmd , list_cmd
parser = argparse.ArgumentParser(
    prog="task-cli",
    description="manage your tasks"
)
subparsers = parser.add_subparsers(dest="command")


add = subparsers.add_parser("add")
add.add_argument("description")
list = subparsers.add_parser("list")
args = parser.parse_args()

if args.command == "add":
    add_cmd(args.description) 
    print(f"task added {args.description}")



if args.command == "list":
    list_cmd()

