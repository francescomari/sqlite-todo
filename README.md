# Introduction to Databases and SQLite

## Application Description

A simple command-line todo list app that lets you add, list, complete, and delete tasks using a local SQLite database.

### How to Use

Run commands like:

- `python todo.py add "Buy groceries"`
- `python todo.py list`
- `python todo.py complete <id>`
- `python todo.py delete <id>`

The database is created automatically. See above for details.

## What is a Database?

- A database is an organized collection of data.
- Databases help store, manage, and retrieve data efficiently.
- Why use a database instead of a simple file?
  - Databases allow for structured data storage (tables, columns).
  - They support searching, sorting, and filtering data quickly.
  - Databases handle multiple users and prevent data corruption.
  - They provide security and backup features.

## What is a Relational Database? What is SQLite?

- A relational database organizes data into tables (like spreadsheets).
- Each table has rows (records) and columns (fields).
- Tables can be related to each other using keys.
- SQLite is a lightweight, file-based relational database.
  - No server required; the database is stored in a single file.
  - Great for small applications, prototyping, and learning.

## Creating Tables and Defining Columns

- Tables are created using SQL (Structured Query Language).
- Columns have types (INTEGER, TEXT, BOOLEAN, etc.) and constraints (PRIMARY KEY, NOT NULL).

```sql
CREATE TABLE todos (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    completed BOOLEAN NOT NULL DEFAULT 0
);
```

## CRUD Operations (Create, Read, Update, Delete)

**Create**: Add new records to a table.

```sql
INSERT INTO todos (title, completed) VALUES ('Buy milk', 0);
```

**Read**: Retrieve records from a table.

```sql
SELECT * FROM todos;
```

**Update**: Modify existing records.

```sql
UPDATE todos SET completed = 1 WHERE id = 1;
```

**Delete**: Remove records from a table.

```sql
DELETE FROM todos WHERE id = 1;
```

## Further Reading

- [Python sqlite3 module documentation](https://docs.python.org/3/library/sqlite3.html)
- [Official SQLite documentation](https://sqlite.org/docs.html)
