import subprocess
import sys
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
TASK_SCRIPTS = sorted((PROJECT_ROOT / "code").glob("Task_*.py"))


class TaskProgramSmokeTests(unittest.TestCase):
    def test_all_pdf_programs_run(self):
        self.assertEqual(
            len(TASK_SCRIPTS),
            19,
            "Expected one program for each PDF task from 02 through 20",
        )
        for task_script in TASK_SCRIPTS:
            with self.subTest(task=task_script.name):
                result = subprocess.run(
                    [sys.executable, str(task_script)],
                    cwd=PROJECT_ROOT,
                    capture_output=True,
                    text=True,
                    timeout=90,
                    check=False,
                )
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
