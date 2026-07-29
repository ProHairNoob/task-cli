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
Usage: main.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  add     add a new task
  delete  delete a task
  list    view your tasks in a list
  mark    mark a task as one of: todo, in-progress, done
  update  change a tasks description
```


