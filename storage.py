import sqlite3
from pathlib import Path
from platformdirs import user_config_dir

app_config_dir = Path(user_config_dir("task-cli"))
app_config_dir.mkdir(parents=True, exist_ok=True)

file_path = app_config_dir / "tasks.db"


def get_db_connection():
    conn = sqlite3.connect(file_path)
    conn.row_factory = sqlite3.Row
    return conn


def make_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS tasks(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        desc TEXT NOT NULL,
        status TEXT DEFAULT 'todo',
        createdAt TEXT DEFAULT CURRENT_TIMESTAMP,
        updatedAt TEXT DEFAULT CURRENT_TIMESTAMP
        )
        """
    )


# def load_task():
#     if not file_path.exists():
#         return []
#     with file_path.open("r") as f:
#         content = f.read()
#         if not content.strip():
#             return []
#         try:
#             return json.loads(content)
#         except json.JSONDecodeError as e:
#             print(f"An error has occured tasks.json exists but isnt valid \nJSON:{e}")
#             print("Not touching the file so your data isnt lost your file is recoverable manually")
#             raise SystemExit(1)
#

# def save_task(tasks):
#     with file_path.open("w") as f:
#          json.dump(tasks,f,indent=2)
