# launcher.py
import runpy
import subprocess


def main():
    subprocess.run(["echo", "Starting Application!"])
    # Directly run your module (like `python -m quest`)
    runpy.run_module("quest", run_name="__main__")


if __name__ == "__main__":
    main()
