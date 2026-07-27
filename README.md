# task-cli

```bash
# adding tasks
task-cli add "Solve the bug"
task added Solve the bug
# updating tasks
task-cli update 1 "Solve the bug in line:37"
task updated
# viewing tasks
task-cli list
ID: 1 Task: solve the bug Created: 2026-07-17 20:33 Last Updated: 2026-07-17 20:33 
# changing a tasks status
task-cli mark 1 in-progress
# deleting tasks
task-cli delete 1
deleted task
# help usage
task-cli --help
usage: task-cli [-h] {add,update,delete,mark,list} ...

manage your tasks

positional arguments:
  {add,update,delete,mark,list}
    add                 adds a new task
    update              changes your tasks description
    delete              delete a task
    mark                change a tasks status
    list                shows your tasks in a list

options:
  -h, --help            show this help message and exit
```


