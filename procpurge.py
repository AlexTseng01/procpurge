import psutil
import sys
import argparse

# Appends a process to the process list
def append_proc(process):
    with open("processes.txt", "a") as file:
        file.write(process + "\n")

# Removes a process from the process list
def remove_proc(process):
    with open("processes.txt", "r") as file:
        lines = file.readlines()

    with open("processes.txt", "w") as file:
        for line in lines:
            if process != line.strip():
                file.write(line)

# Purge all tasks from the process list
def purge():
    with open("processes.txt", "r") as file:
        target_processes = [line.strip().lower() for line in file if line.strip()]
        
        for process in psutil.process_iter(['pid', 'name']):
            try:
                process_name = process.info['name']

                if process_name:
                    if any(target in process_name.lower() for target in target_processes):
                        process.kill()
                        print(f"Ended {process_name}")

            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                continue

# Main
def main(command, name):
    ACTION_MAP = {
        "add": append_proc,
        "remove": remove_proc,
        "purge": purge
    }

    action_name = ACTION_MAP[command]

    if command == "purge":
        action_name()
    else:
        if not name:
            print(f"Error: '{command}' requires a process name parameter")
            sys.exit(1)
        action_name(name)

# Parser
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ProcPurge")
    parser.add_argument("command", choices=["add", "remove", "purge"], help="Actions to execute")
    parser.add_argument("name", nargs="?", default=None, help="Process target name")
    args = parser.parse_args()
    main(args.command, args.name)