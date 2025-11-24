import arguably
from sfvcs.commands.checkout import checkout_snapshot
from sfvcs.commands.init import init_repo, VCS_DIR
from sfvcs.commands.log import show_commits
from sfvcs.commands.snapshot import create_snapshot
from sfvcs.commands.stage import track_file
from sfvcs.commands.status import show_status
from sfvcs.utils.decorators import safe_command
from sfvcs.utils.ui import success, info


@arguably.command
@safe_command
def init():
    """Initialize a new repository."""
    init_repo()
    success(f"✅ Initialized empty VCS repository in {VCS_DIR}")

@arguably.command
@safe_command
def add(file: str):
    """Track a new file."""
    track_file(file)
    success(f"Now tracking '{file}'.")

@arguably.command
@safe_command
def commit(message: str):
    """Commit changes."""
    snapshot = create_snapshot(message)
    success("Changes committed successfully.")
    info(f"{snapshot.id[:5]} -> {snapshot.metadata.message}")

@arguably.command
@safe_command
def status():
    """Show repository status."""
    msg = show_status()
    info(msg)

@arguably.command
@safe_command
def log():
    """Show commit history."""
    show_commits()

@arguably.command
@safe_command
def checkout(commit_id: str):
    """Restore file to a specific commit."""
    checkout_snapshot(commit_id)
    success(f"Checked out commit {commit_id}.")


def main():
    arguably.run()

# Run the CLI when executing main.py
if __name__ == "__main__":
    main()
