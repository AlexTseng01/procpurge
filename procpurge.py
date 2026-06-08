import psutil

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
                        print(f"Ended {process}.")

            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                continue


if __name__ == "__main__":
    purge()