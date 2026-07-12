import argparse
from tasks import add_cmd , list_cmd ,mark_cmd
parser = argparse.ArgumentParser(
    prog="task-cli",
    description="manage your tasks"
)
subparsers = parser.add_subparsers(dest="command")

mark = subparsers.add_parser("mark")
mark.add_argument("id", type=int)
mark.add_argument("status")

add = subparsers.add_parser("add")
add.add_argument("description")

list = subparsers.add_parser("list")
list.add_argument("status",nargs="?" )

args = parser.parse_args()

if args.command == "add":
    add_cmd(args.description) 
    print(f"task added {args.description}")


if args.command == "list":
    list_cmd(args.status)

if args.command == "mark":
    mark_cmd(args.id,args.status)
#debug
#print(args,type(args)) #
#
