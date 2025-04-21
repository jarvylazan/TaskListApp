import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from dotenv import load_dotenv
from app.db_layer import Database

# Load environment variables
load_dotenv()

@pytest.fixture
def db():
    db = Database(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

    # Recreate the tasks table before each test
    db.cursor.execute("DROP TABLE IF EXISTS tasks")
    db.create_table()

    yield db

    db.close()

def test_add_task(db):
    task_text = "Write unit tests"
    new_id = db.add_task(task_text)
    tasks = db.fetch_all_tasks()
    assert len(tasks) == 1
    assert tasks[0]["id"] == new_id
    assert tasks[0]["task_text"] == task_text

def test_update_task(db):
    task_id = db.add_task("Old Task")
    db.update_task("Updated Task", task_id)
    tasks = db.fetch_all_tasks()
    assert tasks[0]["task_text"] == "Updated Task"

def test_delete_task(db):
    task_id = db.add_task("Temporary Task")
    db.delete_task(task_id)
    tasks = db.fetch_all_tasks()
    assert len(tasks) == 0

def test_fetch_all_tasks(db):
    db.add_task("Task 1")
    db.add_task("Task 2")
    tasks = db.fetch_all_tasks()
    assert len(tasks) == 2
    assert tasks[0]["task_text"] == "Task 1"
    assert tasks[1]["task_text"] == "Task 2"