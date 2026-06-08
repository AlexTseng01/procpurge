
# ProcPurge

ProcPurge is a command-line tool that helps end many processes and sub-processes in a fast, reliable way.

It uses partial strings to accurately match process names to their sub-processes, effectively eliminating the need to manually delete all relevant sub-processes.

## Features

- **Add a process** to a list of processes to end
- **Remove a process** from a list of processes to end
- **Purge all processes** from a list of processes to end


## Installation

1. **Clone the repository:** ```git clone https://github.com/AlexTseng01/procpurge.git```
2. **Set up virtual environment:** ```python -m venv venv```
3. **Enter virtual environment:** ```./venv/Scripts/Activate.ps1```
4. **Install required libraries:** ```pip install -r requirements.txt```
## Usage/Examples

1. ```python procpurge.py add minecraft```

2. ```python procpurge.py add xbox```

3. ```python procpurge.py remove webexhost```

4. ```python procpurge.py remove steam```

5. ```python procpurge.py purge```

## 🛠️ Command Line Options

ProcPurge accepts two positional arguments from the terminal: `command` and `name`.

| Argument | Action / Type | Required? | Description |
| :--- | :--- | :--- | :--- |
| **`command`** | `add` | **Yes** | **Command:** Appends a new keyword string to `processes.txt` |
| | `remove` | **Yes** | **Command:** Strips a specific keyword out of `processes.txt` |
| | `purge` | **Yes** | **Command:** Scans the system and kills all matched background tasks |
| **`name`** | *string* | Only for `add`/`remove` | The process keyword you want to target (e.g., `minecraft`, `xbox`) |