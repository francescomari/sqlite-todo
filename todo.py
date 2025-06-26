import sqlite3
import sys

DB_NAME = "todos.db"


def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        c = conn.cursor()
        c.execute(
            """
            CREATE TABLE IF NOT EXISTS todos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                description TEXT NOT NULL,
                completed INTEGER NOT NULL DEFAULT 0
            )
        """
        )
        conn.commit()


def add_todo(description):
    with sqlite3.connect(DB_NAME) as conn:
        c = conn.cursor()
        c.execute("INSERT INTO todos (description) VALUES (?)", (description,))
        conn.commit()
        print("Added todo:", description)


def list_todos():
    with sqlite3.connect(DB_NAME) as conn:
        c = conn.cursor()
        c.execute("SELECT id, description, completed FROM todos ORDER BY id")
        todos = c.fetchall()
        if not todos:
            print("No todos found.")
            return
        for tid, desc, completed in todos:
            status = "x" if completed else " "
            print(f"[{status}] {tid}: {desc}")


def complete_todo(todo_id):
    with sqlite3.connect(DB_NAME) as conn:
        c = conn.cursor()
        c.execute("UPDATE todos SET completed = 1 WHERE id = ?", (todo_id,))
        if c.rowcount == 0:
            print(f"Todo with id {todo_id} not found.")
        else:
            print(f"Todo {todo_id} marked as complete.")
        conn.commit()


def delete_todo(todo_id):
    with sqlite3.connect(DB_NAME) as conn:
        c = conn.cursor()
        c.execute("DELETE FROM todos WHERE id = ?", (todo_id,))
        if c.rowcount == 0:
            print(f"Todo with id {todo_id} not found.")
        else:
            print(f"Todo {todo_id} deleted.")
        conn.commit()


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
