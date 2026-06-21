import psutil
import sys
import argparse

# Adds a process PID to the purge list
def add_pid(pid):
    try:
        with open("processes.txt", "r") as file:
            lines = file.read().splitlines()
    except FileNotFoundError:
        lines = []

    if pid in lines:
        print(f"'{pid}' already exists in the purge list")
        return
    
    with open("processes.txt", "a") as file:
        file.write(pid + "\n")

# Removes a process PID from the purge list
def remove_pid(pid):
    try:
        with open("processes.txt", "r") as file:
            lines = file.read().splitlines()

        if pid not in lines:
            print(f"'{pid}' not found")
            return
        
        with open("processes.txt", "w") as file:
            for line in lines:
                if pid != line:
                    file.write(line + "\n")
    except FileNotFoundError:
        print("The purge list is empty")
    except UnboundLocalError:
        print("The purge list is empty")

# Lists all PIDs in the purge list
def list_pid():
    try:
        with open("processes.txt", "r") as file:
            for line in file.readlines():
                print(line.strip())
    except FileNotFoundError:
        print("The purge list is empty")

# Lists all action commands
def list_actions():
    print(
        "add\n" + 
        "remove\n" + 
        "processes\n" + 
        "actions\n" + 
        "purge"
    )

# Purge all PIDs from the purge list
def purge():
    with open("processes.txt", "r") as file:
        target_pids = [int(line.strip()) for line in file if line.strip().isdigit()]
        
        for pid in psutil.process_iter(['pid']):
            try:
                if pid.info['pid'] in target_pids:
                    pid.kill()
                    print(f"Purged pid={pid}")
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                continue

# Main
def main(command, name):
    ACTION_MAP = {
        "add": add_pid,
        "remove": remove_pid,
        "pids": list_pid,
        "actions": list_actions,
        "purge": purge
    }

    action_name = ACTION_MAP[command]

    if command == "purge" or command == "pids" or command == "actions":
        action_name()
    else:
        if not name:
            print(f"Error: '{command}' requires a process name parameter")
            sys.exit(1)
        action_name(name)

# Parser
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ProcPurge")
    parser.add_argument("command", choices=["add", "remove", "pids", "actions", "purge"], help="Actions to execute")
    parser.add_argument("name", nargs="?", default=None, help="Process target name")
    args = parser.parse_args()
    main(args.command, args.name)