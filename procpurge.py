import psutil

# Appends a process to the process list
def append_proc(proc):
    with open("processes.txt", "a") as file:
        file.write(proc + "\n")

# Removes a process from the process list
def remove_proc(proc):
    with open("processes.txt", "r") as file:
        lines = file.readlines()

    with open("processes.txt", "w") as file:
        for line in lines:
            if proc != line.strip():
                file.write(line)

# Purge all tasks from the process list
def purge():
    None

if __name__ == "__main__":
    # append_proc("b")
    remove_proc("test")