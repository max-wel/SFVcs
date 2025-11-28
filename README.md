# SFVcs
A Git-like Version Control System with Delta Compression

SFVcs is a lightweight version control system inspired by Git.  
It stores file versions using delta compression, meaning only the differences between versions are saved.  
This reduces storage usage while still allowing efficient version history and restoration.

---

## Features
- Initialize a new repository  
- Track files  
- Commit changes with metadata  
- Show repository status  
- View commit history  
- Restore files to previous versions  
- Delta-based storage for efficient history management  

---

## How It Works
Instead of storing complete file copies, SFVcs uses `bsdiff4` to generate compact binary diffs (deltas).  
This enables storage-efficient version history while still allowing full file reconstruction at any point.

---

## Installation

Install SFVcs using pipx:

```bash
pipx install "git+https://git@github.com/max-wel/SFVcs.git"
```

## Usage
- **Initialize a repository**  
sfvcs init

- **Track a file**  
sfvcs add file.txt

- **Commit changes**  
sfvcs commit "Your commit message"

- **Show status**  
sfvcs status

- **Show commit history**  
sfvcs log

- **Restore a file to a specific commit**  
sfvcs checkout <commit-id>

## How It Works

SFVcs stores versioned data inside a custom content-addressed storage system located in:
```
.vcs/  
   objects/        # Stored commits, snapshots, and deltas  
   vcs_ref.json    # Tracked file information and HEAD pointer
```

Delta Storage

File contents are hashed.

Only deltas between versions are stored.

Full file reconstruction is achieved by applying deltas in sequence.

**Dependencies**

bsdiff4 – delta generation & patching

arguably – lightweight CLI framework

rich (optional) – colored terminal output

**Development Setup**

- Clone the repo:
```
git clone https://github.com/max-wel/SFVcs.git  
cd SFVcs
```

- Create and activate a virtual environment:
```
python -m venv .venv
source .venv/bin/activate    # Linux / macOS
.venv\Scripts\activate       # Windows
```
- Install in editable mode:
```
pip install -e .
```

- Test the CLI:
```
sfvcs --help
```