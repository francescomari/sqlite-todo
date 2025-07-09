import sqlite3
import sys

DB_NAME = "todos.db"


def init_db():
    db = sqlite3.connect(DB_NAME)
    try:
        db.execute("""
            CREATE TABLE IF NOT EXISTS todos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                description TEXT NOT NULL,
                completed INTEGER NOT NULL DEFAULT 0
            )
        """)
    finally:
        db.close()


def add_todo(description):
    db = sqlite3.connect(DB_NAME)
    try:
        db.execute("INSERT INTO todos (description) VALUES (?)", (description,))
        db.commit()
        print("Added todo:", description)
    finally:
        db.close()


def list_todos():
    db = sqlite3.connect(DB_NAME)
    try:
        cursor = db.execute("SELECT id, description, completed FROM todos ORDER BY id")
        todos = cursor.fetchall()
        if not todos:
            print("No todos found.")
            return
        for tid, desc, completed in todos:
            status = "x" if completed else " "
            print(f"[{status}] {tid}: {desc}")
    finally:
        db.close()


def complete_todo(todo_id):
    db = sqlite3.connect(DB_NAME)
    try:
        cursor = db.execute("UPDATE todos SET completed = 1 WHERE id = ?", (todo_id,))
        if cursor.rowcount == 0:
            print(f"Todo with id {todo_id} not found.")
        else:
            print(f"Todo {todo_id} marked as complete.")
        db.commit()
    finally:
        db.close()


def delete_todo(todo_id):
    db = sqlite3.connect(DB_NAME)
    try:
        cursor = db.execute("DELETE FROM todos WHERE id = ?", (todo_id,))
        if cursor.rowcount == 0:
            print(f"Todo with id {todo_id} not found.")
        else:
            print(f"Todo {todo_id} deleted.")
        db.commit()
    finally:
        db.close()


def print_usage():
    print("Usage:")
    print('  python todo.py add "description"')
    print("  python todo.py list")
    print("  python todo.py complete <id>")
    print("  python todo.py delete <id>")


def main():
    init_db()

    if len(sys.argv) < 2:
        print_usage()
        return

    match sys.argv[1]:
        case "add" if len(sys.argv) >= 3:
            description = " ".join(sys.argv[2:])
            add_todo(description)
        case "list":
            list_todos()
        case "complete" if len(sys.argv) == 3:
            try:
                todo_id = int(sys.argv[2])
                complete_todo(todo_id)
            except ValueError:
                print("Invalid id.")
        case "delete" if len(sys.argv) == 3:
            try:
                todo_id = int(sys.argv[2])
                delete_todo(todo_id)
            except ValueError:
                print("Invalid id.")
        case _:
            print_usage()


if __name__ == "__main__":
    main()
