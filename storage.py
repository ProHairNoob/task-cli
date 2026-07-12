import json
from pathlib import Path

file_path = Path("tasks.json")

def load_task():
    if not file_path.exists():
        return []
    with file_path.open("r") as f:
        return json.load(f)

def save_task(tasks):
    with file_path.open("w") as f:
         json.dump(tasks,f,indent=2)

