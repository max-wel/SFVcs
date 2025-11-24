import json
import os

from sfvcs.commands.init import get_vcs_dir
from sfvcs.utils.errors import RepoNotInitializedError, FileNotTrackedError

REF_FILE = f"{get_vcs_dir()}vcs_ref.json"

def update_head(commit_id):
    with open(REF_FILE, "r+") as f:
        ref = json.load(f)
        ref["head"] = commit_id
        f.seek(0)
        json.dump(ref, f, indent=2)
        f.truncate()


def get_ref():
    if not os.path.exists(get_vcs_dir()):
        raise RepoNotInitializedError("Repository not initialized. Run `vcs init` first.")
    if not os.path.exists(REF_FILE):
        raise FileNotTrackedError("No file being tracked")
    with open(REF_FILE) as f:
        return json.load(f)
