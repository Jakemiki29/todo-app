"""Simple command-line To-Do application.

This script provides a menu-driven CLI that allows users to:
- Add tasks
- View tasks
- Delete tasks
- Quit the application

Tasks are stored in a Python list for the duration of the program run.
"""


def display_welcome() -> None:
    """Print a welcome message for users."""
    print("\nWelcome to the To-Do List CLI App!")


def display_menu() -> None:
    """Display the main menu options."""
    print("\nPlease choose an option:")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Quit")


def add_task(tasks: list[str]) -> None:
    """Add a new task to the list after validating input."""
    task = input("Enter a task to add: ").strip()
    if not task:
        print("Task cannot be empty. Please try again.")
        return

    tasks.append(task)
    print(f"Task added: {task}")


def view_tasks(tasks: list[str]) -> None:
    """Display all tasks or notify the user when there are none."""
    if not tasks:
        print("No tasks to view.")
        return

    print("\nYour Tasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


def delete_task(tasks: list[str]) -> None:
    """Delete a task by number with robust error handling."""
    if not tasks:
        print("No tasks available to delete.")
        return

    view_tasks(tasks)

    try:
        raw_choice = input("Enter the task number to delete: ").strip()
        task_number = int(raw_choice)
        if task_number < 1 or task_number > len(tasks):
            raise IndexError
    except ValueError:
        print("Invalid input. Please enter a valid whole number.")
    except IndexError:
        print("That task does not exist. Please choose a valid task number.")
    else:
        removed_task = tasks.pop(task_number - 1)
        print(f"Task deleted: {removed_task}")
    finally:
        print("Delete operation complete.")


def handle_menu_choice(choice: str, tasks: list[str]) -> bool:
    """Route the selected menu option.

    Returns:
        bool: True to continue running, False to quit.
    """
    if choice == "1":
        add_task(tasks)
    elif choice == "2":
        view_tasks(tasks)
    elif choice == "3":
        delete_task(tasks)
    elif choice == "4":
        print("Goodbye!")
        return False
    else:
        print("Invalid menu choice. Please select an option from 1 to 4.")

    return True


def run_todo_app() -> None:
    """Run the main loop for the To-Do CLI application."""
    tasks: list[str] = []
    display_welcome()

    keep_running = True
    while keep_running:
        display_menu()

        try:
            choice = input("Enter your choice (1-4): ").strip()
            if not choice:
                raise ValueError("empty")
        except ValueError:
            print("Invalid input. Please enter a menu number from 1 to 4.")
        else:
            keep_running = handle_menu_choice(choice, tasks)
        finally:
            # This line makes loop flow explicit and demonstrates finally usage.
            pass


if __name__ == "__main__":
    run_todo_app()
