import json
from pathlib import Path
from platformdirs import user_config_dir

app_config_dir = Path(user_config_dir("task-cli"))
app_config_dir.mkdir(parents=True, exist_ok=True)

file_path = app_config_dir / "tasks.json"

def load_task():
    if not file_path.exists():
        return []
    with file_path.open("r") as f:
        content = f.read()
        if not content.strip():
            return []
        try: 
            return json.loads(content)
        except json.JSONDecodeError as e:
            print(f"An error has occured tasks.json exists but isnt valid \nJSON:{e}")
            print("Not touching the file so your data isnt lost your file is recoverable manually")
            raise SystemExit(1)
 

def save_task(tasks):
    with file_path.open("w") as f:
         json.dump(tasks,f,indent=2)

