# To-Do CLI App

A simple Python command-line to-do list application.

## Features

- Add tasks
- View tasks
- Delete tasks
- Quit the app
- Input validation and error handling (`try`, `except`, `else`, `finally`)

## Requirements

- Python 3.12+

## Run the App

From the project folder:

```powershell
Set-Location "c:/Users/Jake/OneDrive/Coding-Temple/todo-app"
C:/Users/Jake/OneDrive/Coding-Temple/todo-app/.venv/bin/python.exe todo_cli.py
```

If your environment differs, use your local Python executable:

```powershell
python todo_cli.py
```

## How to Use

When prompted, enter one of these menu options:

- `1` Add task
- `2` View tasks
- `3` Delete task
- `4` Quit

## Example Interaction

```text
Welcome to the To-Do List CLI App!

Please choose an option:
1. Add task
2. View tasks
3. Delete task
4. Quit
Enter your choice (1-4): 1
Enter a task to add: Buy groceries
Task added: Buy groceries

Please choose an option:
1. Add task
2. View tasks
3. Delete task
4. Quit
Enter your choice (1-4): 2

Your Tasks:
1. Buy groceries
```

## Edge Cases Covered

- Invalid menu selection
- Empty input on menu
- No tasks to view
- No tasks to delete
- Delete with non-numeric input
- Delete with out-of-range task number
