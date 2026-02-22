# Simple CLI Todo List

This is a command-line tool for managing a todo list. It now includes the ability to mark tasks as complete and view completed tasks separately.

## Usage

*   **Add tasks:**
    ```bash
    python main.py task1 task2 task3
    ```
    This will print the list of tasks to the console and save them to `todo.txt`.

*   **Mark a task as complete:**
    ```bash
    python main.py complete task1
    ```
    This marks the specified task as complete and updates `todo.txt`. Completed tasks are prefixed with "[x]".

*   **View all tasks:**
    ```bash
    python main.py
    ```
    This prints all tasks to the console.

*   **View completed tasks:**
    ```bash
    python main.py --completed
    ```
    This prints only the completed tasks to the console.

*   **Clear the list:**
    ```bash
    python main.py --clear
    ```
    This deletes the `todo.txt` file, effectively clearing the todo list.

## Persistence

The todo list is persisted to a file named `todo.txt`. Each task is written on a new line. Completed tasks are prefixed with "[x]".  To view the list, run the script again. To clear the list, delete the `todo.txt` file or use the `--clear` flag.

## New Features

*   **Add Tasks:**  The script now supports adding tasks directly using the `add` command.  For example, `python main.py add buy groceries`.
*   **Clear List:** Added a `--clear` flag to remove all tasks from the todo list by deleting the `todo.txt` file.
*   **Clear List when Empty:** Added a test case to ensure the clear list functionality works correctly when the todo list is already empty.

## Testing

Comprehensive unit tests are included to ensure the functionality of the todo list.

## Examples

```bash
# Add some tasks
python main.py task1 task2 task3

# Mark "buy groceries" as complete
python main.py complete buy groceries

# View all tasks
python main.py

# View completed tasks
python main.py --completed

# Clear the list
python main.py --clear
```