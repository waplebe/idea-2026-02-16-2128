import unittest
import main
from io import StringIO

class TestMain(unittest.TestCase):

    def setUp(self):
        self.captured_output = StringIO()

        # Redirect stdout to capture output
        self.original_stdout = sys.stdout
        sys.stdout = self.captured_output

    def tearDown(self):
        # Restore stdout
        sys.stdout = self.original_stdout

    def test_add_tasks(self):
        main.save_tasks(["task1", "task2"])
        self.assertEqual(self.captured_output.getvalue().strip(), "Tasks:\n- task1\n- task2\n")

    def test_complete_task(self):
        main.save_tasks(["task1"])
        main.save_tasks(["complete task1"])
        self.assertEqual(self.captured_output.getvalue().strip(), "Tasks:\n- task1\n")

    def test_view_completed_tasks(self):
        main.save_tasks(["task1", "[x] task2"])
        main.save_tasks(["--completed"])
        self.assertEqual(self.captured_output.getvalue().strip(), "Completed Tasks:\n- [x] task2\n")

    def test_no_tasks_provided(self):
        main.save_tasks([])
        main.save_tasks([])
        main.save_tasks([])
        main.save_tasks([])
        self.assertEqual(self.captured_output.getvalue().strip(), "No tasks provided.\n")

    def test_invalid_complete_task(self):
        main.save_tasks(["task1"])
        main.save_tasks(["complete task1"])
        self.assertEqual(self.captured_output.getvalue().strip(), "Task 'task1' not found.\n")

    def test_multiple_complete_tasks(self):
        main.save_tasks(["task1", "task2", "task3"])
        main.save_tasks(["complete task1", "complete task2"])
        self.assertEqual(self.captured_output.getvalue().strip(), "Tasks:\n- task1\n- task2\n- task3\n")

    def test_complete_nonexistent_task(self):
        main.save_tasks(["task1"])
        main.save_tasks(["complete task2"])
        self.assertEqual(self.captured_output.getvalue().strip(), "Task 'task2' not found.\n")

    def test_empty_todo_file(self):
        main.save_tasks([])
        main.save_tasks(["--completed"])
        self.assertEqual(self.captured_output.getvalue().strip(), "No completed tasks.\n")

    def test_task_with_leading_and_trailing_whitespace(self):
        main.save_tasks([" task1 "])
        main.save_tasks(["complete task1 "])
        self.assertEqual(self.captured_output.getvalue().strip(), "Tasks:\n- task1\n")

    def test_task_with_multiple_spaces(self):
        main.save_tasks(["task1   "])
        main.save_tasks(["complete task1   "])
        self.assertEqual(self.captured_output.getvalue().strip(), "Tasks:\n- task1\n")

    def test_task_with_special_characters(self):
        main.save_tasks(["task!@#$%^"])
        main.save_tasks(["complete task!@#$%^"])
        self.assertEqual(self.captured_output.getvalue().strip(), "Tasks:\n- task!@#$%^\n")