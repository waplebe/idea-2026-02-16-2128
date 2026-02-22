import argparse
import sys
import os

def load_tasks():
    """Loads tasks from the todo.txt file."""
    tasks = []
    if os.path.exists("todo.txt"):
        try:
            with open("todo.txt", "r") as f:
                tasks = [line.strip() for line in f.readlines()]
        except Exception as e:
            print(f"Error loading tasks: {e}")
    return tasks

def save_tasks(tasks):
    """Saves tasks to the todo.txt file."""
    try:
        with open("todo.txt", "w") as f:
            for task in tasks:
                f.write(f"{task}\n")
    except Exception as e:
        print(f"Error saving tasks: {e}")

def mark_complete(task, tasks):
    """Marks a task as complete."""
    try:
        index = tasks.index(task)
        tasks[index] = "[x] " + tasks[index]
    except ValueError:
        print(f"Task '{task}' not found.")

def view_completed_tasks(tasks):
    """Views completed tasks."""
    completed_tasks = [task for task in tasks if task.startswith("[x]")]
    if completed_tasks:
        print("\nCompleted Tasks:")
        for task in completed_tasks:
            print(f"- {task}")
    else:
        print("\nNo completed tasks.")

def add_task(task, tasks):
    """Adds a task to the list."""
    tasks.append(task)

def clear_list(tasks):
    """Clears the todo list by deleting the todo.txt file."""
    try:
        os.remove("todo.txt")
        print("Todo list cleared.")
    except FileNotFoundError:
        print("Todo list is already empty.")
    except Exception as e:
        print(f"Error clearing list: {e}")

def main():
    parser = argparse.ArgumentParser(description="A simple command-line todo list.")
    parser.add_argument("task", nargs='*', help="The task to add or mark as complete.")
    parser.add_argument("--completed", action="store_true", help="View completed tasks.")
    parser.add_argument("--clear", action="store_true", help="Clear the todo list.")

    args = parser.parse_args()

    tasks = load_tasks()

    if not args.task:
        print("No tasks provided.")
        return

    for action in args.task:
        if action.startswith("complete"):
            task_to_complete = action[len("complete"):].strip()
            mark_complete(task_to_complete, tasks)
        elif action.startswith("add"):
            task_to_add = action[len("add"):].strip()
            add_task(task_to_add, tasks)
        elif action == "--clear":
            clear_list(tasks)
        else:
            print(f"Invalid action: {action}")

    print("Tasks:")
    for task in tasks:
        print(f"- {task}")

    if args.completed:
        view_completed_tasks(tasks)

    save_tasks(tasks)

if __name__ == "__main__":
    main()