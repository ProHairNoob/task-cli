# task-cli

```bash
# adding tasks
task-cli add Solve the bug
task added Solve the bug
# updating tasks
task-cli update 1 "Solve the bug in line:37"
task updated to: Solve the bug in line:37
# viewing tasks
task-cli list
ID Description              Status Last modified
1  Solve the bug in line:37  todo 2026-08-02 09:49:14
# changing a tasks status
task-cli mark 1 in-progress
# deleting tasks
task-cli delete 1
task deleted: Solve the bug in line:37 
# deleting all
task-cli delete
No id given  delete all tasks? (y/n) y
Deleting all tasks ...
# help usage
task-cli --help
Usage: task-cli [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  add     add a new task
  delete  delete a task
  list    view your tasks in a list
  mark    mark a task as one of: todo, in-progress, done
  update  change a tasks description
#Help usage by command
#task-cli list --help
Usage: task-cli list [OPTIONS] [FILTER]

  view your tasks in a list

Options:
  --status [todo|in-progress|done]
  --help                          Show this message and exit.
```


