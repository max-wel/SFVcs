import json
import os

from sfvcs.commands.init import get_vcs_dir
from sfvcs.utils.errors import RepoNotInitializedError, NoChangesError
from sfvcs.utils.ref import REF_FILE


def verify_tracked_file(file_name: str):
    if not os.path.exists(get_vcs_dir()):
        raise RepoNotInitializedError("Repository not initialized. Run `vcs init` first.")

    if os.path.exists(REF_FILE):
        raise NoChangesError("A file is already being tracked.")

    if not os.path.exists(file_name):
        raise FileNotFoundError(f"File '{file_name}' does not exist.")

    if not os.path.isfile(file_name):
        raise ValueError(f"'{file_name}' is not a valid file.")

    try:
        with open(file_name, "r", encoding="utf-8") as f:
            f.read(512)
    except UnicodeDecodeError:
        raise ValueError("Only text files can be tracked.")

def track_file(file_name: str):
    verify_tracked_file(file_name)
    ref = {
        "index": file_name
    }

    with open(f"{REF_FILE}", "w") as f:
        json.dump(ref, f, indent=2)