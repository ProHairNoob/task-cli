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
        id INTEGER PRIMARY KEY,
        desc TEXT NOT NULL,
        status TEXT CHECK (status IN ('todo','in-progress','done'))DEFAULT 'todo',
        createdAt TEXT DEFAULT CURRENT_TIMESTAMP,
        updatedAt TEXT DEFAULT CURRENT_TIMESTAMP
        )
        """
    )
