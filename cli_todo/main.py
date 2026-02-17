import argparse

def load_tasks():
    """Loads tasks from the todo.txt file."""
    try:
        with open("todo.txt", "r") as f:
            tasks = [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        tasks = []
    return tasks

def save_tasks(tasks):
    """Saves tasks to the todo.txt file."""
    with open("todo.txt", "w") as f:
        for task in tasks:
            f.write(f"{task}\n")

def main():
    parser = argparse.ArgumentParser(description="A simple command-line todo list.")
    parser.add_argument("task", nargs='*', help="The task to add or mark as complete.")
    parser.add_argument("--completed", action="store_true", help="View completed tasks.")

    args = parser.parse_args()

    tasks = load_tasks()

    if not args.task:
        print("No tasks provided.")
        return

    if any(args.task[0].startswith("complete") for args.task):
        # Handle complete commands
        for task in args.task:
            if task.startswith("complete"):
                task_to_complete = task[len("complete"):].strip()
                try:
                    index = tasks.index(task_to_complete)
                    tasks[index] = "[x] " + tasks[index]
                except ValueError:
                    print(f"Task '{task_to_complete}' not found.")
            else:
                # Add new tasks
                tasks.append(task)

    print("Tasks:")
    for task in tasks:
        print(f"- {task}")

    if args.completed:
        completed_tasks = [task for task in tasks if task.startswith("[x]")]
        if completed_tasks:
            print("\nCompleted Tasks:")
            for task in completed_tasks:
                print(f"- {task}")
        else:
            print("\nNo completed tasks.")

    save_tasks(tasks)

if __name__ == "__main__":
    main()