import subprocess
from pathlib import Path


class Orchestrator:

    def __init__(self, robot_tests_path="robot_tests"):
        self.robot_tests_path = Path(robot_tests_path)

    def run_robot_tests(self):
        result = subprocess.run(
            ["robot", str(self.robot_tests_path)],
            capture_output=True,
            text=True
        )

        print(result.stdout)
        print(result.stderr)

        return result.returncode == 0


if __name__ == "__main__":
    orchestrator = Orchestrator()
    success = orchestrator.run_robot_tests()

    if success:
        print("Execution completed successfully.")
    else:
        print("Execution failed.")

