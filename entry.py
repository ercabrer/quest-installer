import subprocess
import sys

# Define the environment name and the script you want to run
env_name = "quest"
script_name = "launcher.py"

# Construct the command
command = f"conda run -n {env_name} python {script_name}"

# Run the command using subprocess
try:
    subprocess.run(command, shell=True, check=True)
except subprocess.CalledProcessError as e:
    print(f"Error running script: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
